"""
Database management for LifeOS
"""

import sqlite3
from pathlib import Path

# Get data directory from app config
from app.config import DATA_DIR

def get_db():
    """Get database connection"""
    db_path = DATA_DIR / "lifeos.db"
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row  # Return rows as dictionaries
    return conn

def init_db():
    """Initialize database with schema"""
    db = get_db()
    
    # Projects table
    db.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            goal TEXT,
            target_date DATE,
            status TEXT DEFAULT 'active',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Areas table
    db.execute("""
        CREATE TABLE IF NOT EXISTS areas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            status TEXT DEFAULT 'active',
            standard TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Tasks table (GTD)
    db.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            project_id INTEGER,
            area_id INTEGER,
            context TEXT,
            priority INTEGER DEFAULT 0,
            due_date DATE,
            completed BOOLEAN DEFAULT 0,
            inbox BOOLEAN DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            completed_at TIMESTAMP,
            FOREIGN KEY (project_id) REFERENCES projects(id),
            FOREIGN KEY (area_id) REFERENCES areas(id)
        )
    """)
    
    # Daily plans
    db.execute("""
        CREATE TABLE IF NOT EXISTS daily_plans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE NOT NULL UNIQUE,
            one_thing TEXT,
            morning_plan TEXT,
            afternoon_plan TEXT,
            evening_plan TEXT,
            faith_goal TEXT,
            energy_level INTEGER,
            completed BOOLEAN DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Journal entries
    db.execute("""
        CREATE TABLE IF NOT EXISTS journal_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE NOT NULL,
            type TEXT NOT NULL,
            content TEXT,
            insights TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # History log
    db.execute("""
        CREATE TABLE IF NOT EXISTS history_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE NOT NULL,
            type TEXT NOT NULL,
            content TEXT,
            category TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    db.commit()
    db.close()
    print("Database initialized successfully!")

