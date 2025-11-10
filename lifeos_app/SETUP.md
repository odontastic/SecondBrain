# LifeOS Application - Setup Guide

## Quick Start (3 Steps)

### Step 1: Install Dependencies
```bash
cd /home/austin/Documents/LifeOS/lifeos_app
pip install -r requirements.txt
```

### Step 2: Initialize Database
```bash
python scripts/init_db.py
```

### Step 3: Run the Application
```bash
python app.py
```

Then open your browser to: **http://localhost:5000**

---

## What You'll See

### Dashboard
- Overview of your Projects, Areas, and Tasks
- Quick statistics
- Today's plan preview

### Daily Plan
- Morning, afternoon, and evening planning
- Kickstarters (inspirational quotes)
- Faith-focused goals
- Prioritized tasks
- Links to review templates

### Projects, Areas, Resources, Archives
- Browse and view all your PARA-organized content
- Click any item to see full details

### Tasks (GTD)
- View tasks organized by context (@Computer, @Home, etc.)
- Inbox for quick capture
- GTD workflow integration

### History & Growth
- Track your progress over time
- Statistics and insights
- Historical plans and reflections

### Administration
- System configuration
- Template management
- Personal profile review

---

## Troubleshooting

### If you get import errors:
Make sure you're running from the `lifeos_app` directory:
```bash
cd /home/austin/Documents/LifeOS/lifeos_app
python app.py
```

### If the database isn't created:
Run the init script manually:
```bash
python scripts/init_db.py
```

### If you can't access the web interface:
- Check that port 5000 is available
- Try accessing via: http://127.0.0.1:5000
- Check terminal for error messages

---

## Next Steps

1. **Explore the interface** - Navigate through all views
2. **Start using Daily Plan** - Fill in your morning plan
3. **Add tasks** - Use the GTD task management
4. **Review Projects** - Check your active projects
5. **Customize** - Adjust settings in Admin panel

---

## Customization Ideas

- Modify CSS in `static/css/style.css` for different colors
- Add features in `app.py` routes
- Extend database schema in `app/database.py`
- Add templates in `templates/` directory

---

## Support

This is your first application! Everything is designed to be:
- **Readable** - Code is well-commented
- **Modifiable** - Easy to change and extend
- **FOSS** - All open source components
- **Simple** - No complex dependencies

Enjoy building your LifeOS!

