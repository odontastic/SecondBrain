#!/bin/bash
# LifeOS Application Startup Script

echo "=== LifeOS Application ==="
echo ""

# Check if we're in the right directory
if [ ! -f "app.py" ]; then
    echo "Error: Please run this script from the lifeos_app directory"
    echo "Current directory: $(pwd)"
    exit 1
fi

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not found"
    exit 1
fi

# Check if dependencies are installed
if ! python3 -c "import flask" 2>/dev/null; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
fi

# Initialize database if needed
if [ ! -f "data/lifeos.db" ]; then
    echo "Initializing database..."
    python3 scripts/init_db.py
fi

# Start the application
echo ""
echo "Starting LifeOS Application..."
echo "Open http://localhost:5000 in your browser"
echo "Press Ctrl+C to stop"
echo ""
python3 app.py

