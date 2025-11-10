#!/usr/bin/env python3
"""
LifeOS Application
A comprehensive personal Life Operating System
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
import sqlite3
from pathlib import Path
from datetime import datetime, date
import json

# Import our modules
try:
    from app.database import init_db, get_db
    from app.file_reader import read_para_files
    from app.utils import parse_markdown_project, parse_markdown_area
except ImportError:
    # If running from app.py directly
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent))
    from app.database import init_db, get_db
    from app.file_reader import read_para_files
    from app.utils import parse_markdown_project, parse_markdown_area

# Configuration
BASE_DIR = Path(__file__).parent.parent  # LifeOS root directory
DATA_DIR = BASE_DIR / "lifeos_app" / "data"
PARA_DIR = BASE_DIR  # Where Projects/, Areas/, etc. are

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lifeos-secret-key-change-in-production'
app.config['BASE_DIR'] = BASE_DIR
app.config['DATA_DIR'] = DATA_DIR
app.config['PARA_DIR'] = PARA_DIR

# Initialize database on first run
DATA_DIR.mkdir(parents=True, exist_ok=True)
if not (DATA_DIR / "lifeos.db").exists():
    init_db()

@app.route('/')
def dashboard():
    """Main dashboard view"""
    # Read PARA files
    projects = read_para_files(PARA_DIR / "Projects")
    areas = read_para_files(PARA_DIR / "Areas")
    
    # Get stats from database
    db = get_db()
    
    # Count active projects
    active_projects = [p for p in projects if p.get('status') != 'completed']
    
    # Count tasks
    today = date.today()
    cursor = db.execute(
        "SELECT COUNT(*) FROM tasks WHERE completed = 0 AND due_date <= ?",
        (today,)
    )
    tasks_due_today = cursor.fetchone()[0]
    
    cursor = db.execute(
        "SELECT COUNT(*) FROM tasks WHERE completed = 1 AND DATE(completed_at) = ?",
        (today,)
    )
    tasks_completed_today = cursor.fetchone()[0]
    
    # Get today's plan
    cursor = db.execute(
        "SELECT * FROM daily_plans WHERE date = ?",
        (today,)
    )
    today_plan = cursor.fetchone()
    
    return render_template('dashboard.html',
                         projects=active_projects[:5],  # Top 5 for dashboard
                         areas=areas[:5],
                         tasks_due_today=tasks_due_today,
                         tasks_completed_today=tasks_completed_today,
                         today_plan=today_plan,
                         today=today)

@app.route('/daily')
def daily_plan():
    """Daily planning view"""
    today = date.today()
    db = get_db()
    
    # Get today's plan
    cursor = db.execute(
        "SELECT * FROM daily_plans WHERE date = ?",
        (today,)
    )
    plan = cursor.fetchone()
    
    # Get today's tasks
    cursor = db.execute(
        """SELECT * FROM tasks 
           WHERE (due_date = ? OR due_date IS NULL) AND completed = 0
           ORDER BY priority DESC, created_at""",
        (today,)
    )
    tasks = cursor.fetchall()
    
    # Get kickstarters from Resources
    kickstarters_file = PARA_DIR / "Resources" / "inspirational_kickstarters.md"
    kickstarters = []
    if kickstarters_file.exists():
        # Simple extraction of kickstarters
        with open(kickstarters_file, 'r', encoding='utf-8') as f:
            content = f.read()
            # Extract lines that might be kickstarters (basic parsing)
            lines = [l.strip() for l in content.split('\n') if l.strip() and not l.strip().startswith('#')]
            kickstarters = lines[:5]  # First 5 as examples
    
    return render_template('daily_plan.html',
                         plan=plan,
                         tasks=tasks,
                         kickstarters=kickstarters,
                         today=today)

@app.route('/projects')
def projects():
    """Projects view"""
    projects = read_para_files(PARA_DIR / "Projects")
    return render_template('projects.html', projects=projects)

def get_or_create_project_in_db(project_data):
    """
    Sync a markdown project to database and return its database ID.
    Creates the project if it doesn't exist, updates if it does.
    """
    db = get_db()
    
    # Try to find existing project by name (from title)
    cursor = db.execute(
        "SELECT id FROM projects WHERE name = ?",
        (project_data.get('title', project_data.get('filename', 'Unknown')),)
    )
    existing = cursor.fetchone()
    
    if existing:
        project_id = existing['id']
        # Update project info in database
        db.execute("""
            UPDATE projects 
            SET description = ?, goal = ?, target_date = ?, status = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (
            project_data.get('content', '')[:500],  # Truncate long content
            project_data.get('goal'),
            project_data.get('target_date'),
            project_data.get('status', 'active'),
            project_id
        ))
        db.commit()
    else:
        # Create new project in database
        cursor = db.execute("""
            INSERT INTO projects (name, description, goal, target_date, status)
            VALUES (?, ?, ?, ?, ?)
        """, (
            project_data.get('title', project_data.get('filename', 'Unknown')),
            project_data.get('content', '')[:500],  # Truncate long content
            project_data.get('goal'),
            project_data.get('target_date'),
            project_data.get('status', 'active')
        ))
        db.commit()
        project_id = cursor.lastrowid
    
    return project_id

@app.route('/projects/<filename>')
def project_detail(filename):
    """Individual project detail"""
    project_file = PARA_DIR / "Projects" / filename
    if not project_file.exists():
        return "Project not found", 404
    
    project = parse_markdown_project(project_file)
    
    # Sync project to database to get ID for task queries
    project_id = get_or_create_project_in_db(project)
    project['db_id'] = project_id  # Store for reference
    
    # Get related tasks using database ID
    db = get_db()
    cursor = db.execute(
        "SELECT * FROM tasks WHERE project_id = ? AND completed = 0 ORDER BY priority DESC, due_date",
        (project_id,)
    )
    tasks = cursor.fetchall()
    
    return render_template('project_detail.html', project=project, tasks=tasks)

@app.route('/areas')
def areas():
    """Areas view"""
    areas = read_para_files(PARA_DIR / "Areas")
    return render_template('areas.html', areas=areas)

def get_or_create_area_in_db(area_data):
    """
    Sync a markdown area to database and return its database ID.
    Creates the area if it doesn't exist, updates if it does.
    """
    db = get_db()
    
    # Try to find existing area by name (from title)
    cursor = db.execute(
        "SELECT id FROM areas WHERE name = ?",
        (area_data.get('title', area_data.get('filename', 'Unknown')),)
    )
    existing = cursor.fetchone()
    
    if existing:
        area_id = existing['id']
        # Update area info in database
        db.execute("""
            UPDATE areas 
            SET description = ?, status = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (
            area_data.get('content', '')[:500],  # Truncate long content
            area_data.get('status', 'active'),
            area_id
        ))
        db.commit()
    else:
        # Create new area in database
        cursor = db.execute("""
            INSERT INTO areas (name, description, status)
            VALUES (?, ?, ?)
        """, (
            area_data.get('title', area_data.get('filename', 'Unknown')),
            area_data.get('content', '')[:500],  # Truncate long content
            area_data.get('status', 'active')
        ))
        db.commit()
        area_id = cursor.lastrowid
    
    return area_id

@app.route('/areas/<filename>')
def area_detail(filename):
    """Individual area detail"""
    area_file = PARA_DIR / "Areas" / filename
    if not area_file.exists():
        return "Area not found", 404
    
    area = parse_markdown_area(area_file)
    
    # Sync area to database to get ID (for potential future task linking)
    area_id = get_or_create_area_in_db(area)
    area['db_id'] = area_id  # Store for reference
    
    # Get related tasks using database ID
    db = get_db()
    cursor = db.execute(
        "SELECT * FROM tasks WHERE area_id = ? AND completed = 0 ORDER BY priority DESC, due_date",
        (area_id,)
    )
    tasks = cursor.fetchall()
    
    return render_template('area_detail.html', area=area, tasks=tasks)

@app.route('/resources')
def resources():
    """Resources view"""
    resources = read_para_files(PARA_DIR / "Resources")
    return render_template('resources.html', resources=resources)

@app.route('/archives')
def archives():
    """Archives view"""
    archives = read_para_files(PARA_DIR / "Archives")
    return render_template('archives.html', archives=archives)

@app.route('/tasks')
def tasks():
    """GTD Task Management view"""
    db = get_db()
    
    # Get tasks by context
    contexts = {}
    cursor = db.execute("""
        SELECT DISTINCT context FROM tasks 
        WHERE completed = 0 AND context IS NOT NULL
        ORDER BY context
    """)
    context_list = [row[0] for row in cursor.fetchall()]
    
    for context in context_list:
        cursor = db.execute("""
            SELECT * FROM tasks 
            WHERE context = ? AND completed = 0
            ORDER BY priority DESC, due_date
        """, (context,))
        contexts[context] = cursor.fetchall()
    
    # Get tasks without context
    cursor = db.execute("""
        SELECT * FROM tasks 
        WHERE (context IS NULL OR context = '') AND completed = 0
        ORDER BY priority DESC, due_date
    """)
    contexts['No Context'] = cursor.fetchall()
    
    # Get inbox items
    cursor = db.execute("""
        SELECT * FROM tasks 
        WHERE inbox = 1 AND completed = 0
        ORDER BY created_at DESC
    """)
    inbox = cursor.fetchall()
    
    return render_template('tasks.html', contexts=contexts, inbox=inbox)

@app.route('/admin')
def admin():
    """Administration panel"""
    return render_template('admin.html')

@app.route('/history')
def history():
    """History and growth tracking"""
    db = get_db()
    
    # Get recent history
    cursor = db.execute("""
        SELECT * FROM history_log 
        ORDER BY created_at DESC 
        LIMIT 50
    """)
    recent_history = cursor.fetchall()
    
    # Get statistics
    cursor = db.execute("SELECT COUNT(*) FROM tasks WHERE completed = 1")
    total_completed = cursor.fetchone()[0]
    
    cursor = db.execute("SELECT COUNT(*) FROM projects WHERE status = 'completed'")
    projects_completed = cursor.fetchone()[0]
    
    return render_template('history.html', 
                         recent_history=recent_history,
                         total_completed=total_completed,
                         projects_completed=projects_completed)

if __name__ == '__main__':
    print("Starting LifeOS Application...")
    print(f"Data directory: {DATA_DIR}")
    print(f"PARA directory: {PARA_DIR}")
    print("Open http://localhost:5000 in your browser")
    app.run(debug=True, host='0.0.0.0', port=5000)

