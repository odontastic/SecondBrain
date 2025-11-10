"""
Read and parse PARA markdown files
"""

from pathlib import Path
import re
from datetime import datetime

def read_para_files(directory):
    """Read all markdown files from a PARA directory"""
    files = []
    dir_path = Path(directory)
    
    if not dir_path.exists():
        return []
    
    for file_path in dir_path.glob("*.md"):
        if file_path.name.startswith('.'):
            continue
        
        try:
            content = file_path.read_text(encoding='utf-8')
            
            # Basic parsing
            file_info = {
                'filename': file_path.name,
                'path': str(file_path),
                'content': content,
                'title': extract_title(content),
                'metadata': extract_metadata(content),
            }
            
            files.append(file_info)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            continue
    
    return files

def extract_title(content):
    """Extract title from markdown (first # heading)"""
    lines = content.split('\n')
    for line in lines:
        if line.strip().startswith('# '):
            return line.strip()[2:].strip()
    return "Untitled"

def extract_metadata(content):
    """Extract metadata from markdown frontmatter or content"""
    metadata = {}
    
    # Look for frontmatter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter = parts[1]
            for line in frontmatter.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    metadata[key.strip()] = value.strip()
    
    # Look for key patterns in content
    lines = content.split('\n')
    for i, line in enumerate(lines):
        # Look for completion date
        if 'completion date' in line.lower() or 'target completion' in line.lower():
            # Try to find date
            date_match = re.search(r'(\d{1,2}[/-]\d{1,2}[/-]\d{4}|\w+\s+\d{1,2},?\s+\d{4})', line, re.IGNORECASE)
            if date_match:
                metadata['target_date'] = date_match.group(1)
        
        # Look for status
        if line.strip().startswith('**Status:**'):
            metadata['status'] = line.split(':', 1)[1].strip()
    
    return metadata

def parse_markdown_project(file_path):
    """Parse a project markdown file into structured data"""
    content = file_path.read_text(encoding='utf-8')
    
    project = {
        'filename': file_path.name,
        'title': extract_title(content),
        'content': content,
    }
    
    # Extract goal
    goal_match = re.search(r'\*\*Goal:\*\*\s*(.+?)(?:\n|$)', content)
    if goal_match:
        project['goal'] = goal_match.group(1).strip()
    
    # Extract completion date
    date_match = re.search(r'\*\*Target Completion Date:\*\*\s*(.+?)(?:\n|$)', content)
    if date_match:
        project['target_date'] = date_match.group(1).strip()
    
    # Extract status
    status_match = re.search(r'\*\*Status:\*\*\s*(.+?)(?:\n|$)', content)
    if status_match:
        project['status'] = status_match.group(1).strip()
    
    return project

def parse_markdown_area(file_path):
    """Parse an area markdown file into structured data"""
    content = file_path.read_text(encoding='utf-8')
    
    area = {
        'filename': file_path.name,
        'title': extract_title(content),
        'content': content,
    }
    
    # Extract status
    status_match = re.search(r'\*\*Status:\*\*\s*(.+?)(?:\n|$)', content)
    if status_match:
        area['status'] = status_match.group(1).strip()
    
    return area

