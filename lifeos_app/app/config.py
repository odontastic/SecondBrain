"""
Configuration for LifeOS app
"""

from pathlib import Path

# Base directory (LifeOS root)
BASE_DIR = Path(__file__).parent.parent.parent

# Data directory for database
DATA_DIR = BASE_DIR / "lifeos_app" / "data"

# PARA directories
PARA_DIR = BASE_DIR

