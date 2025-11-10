#!/usr/bin/env python3
"""
Initialize LifeOS database
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.database import init_db

if __name__ == '__main__':
    print("Initializing LifeOS database...")
    init_db()
    print("Database initialized successfully!")

