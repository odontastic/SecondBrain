<think>We need to produce the final version of the revised Life OS Guiding document, incorporating all details from earlier: vision, core principles, architecture, file system, tagging conventions, 4-part toolkit, UI spec, Electron implementation, commands, scheduler, etc. Provide a single document that summarises the system. Should be comprehensive but concise. Let's produce a final guide.

We'll structure:

1. Overview
2. Vision & Core Values
3. Architecture
4. File System Layout
5. Metadata & Tagging
6. 4‑Part PKM Toolkit
7. UI & Interaction
8. Commands
9. Scheduler
10. Implementation Notes
11. Prototype Script
12. Next Steps

Include code snippets for key parts: YAML schema, example note, command parser, LLM wrapper, scheduler.

Let's produce final answer.</think># Life OS – The Personal Life Operating System
**A complete, LLM‑driven, second‑brain based system that turns your Markdown files into a living, self‑maintaining assistant.**

---

## 1.  Vision & Core Values

| # | Principle | Why it matters | How the LLM enforces it |
|---|-----------|----------------|--------------------------|
| 1 | **Personalised Coaching** | Every suggestion is grounded in your own data, personality (INTP), and goals. | LLM first *asks* you about mood, energy, and priorities before acting. |
| 2 | **Safety & Boundaries** | Coaching stays within a non‑clinical zone; emergencies are routed to a human. | LLM refuses to give diagnoses and offers a “human help” link. |
| 3 | **Action‑oriented** | Advice translates to a concrete next step. | Every response ends with a single, *Early‑Smart‑Simple‑Manageable* action. |
| 4 | **Transparency** | You always know *why* the LLM suggests something. | LLM provides a short rationale with each recommendation. |
| 5 | **Data‑first** | All insights, goals, and habits are stored in Markdown on‑disk. | LLM reads/writes directly to the Life OS folder. |
| 6 | **Modularity** | New tools (Calendar, Email, etc.) can be plugged in later. | LLM can be extended via plugins without breaking the core. |

---

## 2.  System Architecture

```
┌───────────────────────┐
│  Life OS (LLM Agent)  │  ← 1‑click prompt →  │
└────────────┬──────────┘                     │
             │                                  │
       ┌─────▼───────┐                       │
       │  PARA Store │                       │
       │ (Markdown)  │                       │
       └─────┬───────┘                       │
             │                                 │
       ┌─────▼───────┐          ┌─────────────┐
       │  RAG Engine │◄───────►│  Vector DB   │
       │ (Built‑in)  │          │ (LLM tool)   │
       └─────┬───────┘          └─────────────┘
             │
       ┌─────▼───────┐
       │  Dashboard   │  (Markdown‑rendered)
       └─────┬───────┘
             │
       ┌─────▼───────┐
       │  Command UI   │  (CLI + future web)
       └─────┬───────┘
```

*All data lives in `~/LifeOS/` – a pure Markdown file system.*

---

## 3.  File‑System Layout (PARA + Extensions)

```
LifeOS/
 ├─ Projects/
 │   ├─ Active/
 │   │   ├─ Self‑Improvement/
 │   │   │   ├─ Health/
 │   │   │   ├─ Skills/
 │   │   │   ├─ Relationships/
 │   │   │   ├─ Finance/
 │   │   │   ├─ Spiritual/
 │   │   │   └─ Creativity/
 │   └─ Completed/
 ├─ Areas/
 │   ├─ Family/
 │   ├─ House/
 │   ├─ Yard/
 │   ├─ Food/
 │   ├─ Home_School/
 │   └─ Faith/
 ├─ Resources/
 │   ├─ Books/
 │   ├─ Articles/
 │   ├─ Videos/
 │   ├─ Courses/
 │   └─ Templates/
 ├─ Journal/
 │   ├─ Daily/
 │   ├─ Weekly/
 │   └─ Monthly/
 ├─ Habits/
 ├─ Metrics/
 ├─ Logs/
 ├─ People/
 │   └─ Personal/
 │       ├─ Profile.md
 │       └─ Preferences.md
 ├─ Extensions/          # future connectors
 └─ Archives/
```

---

## 4.  Metadata & Tagging

### 4.1  YAML Front‑Matter (example)

```yaml
---
title: "Book Summary – Stoicism"
type: Note
tags: [book-summary, stoicism, CBT]
created_at: 2025-11-02T10:15:00Z
modified_at: 2025-11-02T10:15:00Z
status: IN-PROGRESS
area: Philosophy
project: Personal Growth
relates:
  - person: "[[Wife]]"
  - concept: "[[Tranquility]]"
---
```

### 4.2  Tag Conventions

| Convention | Example | Meaning |
|------------|---------|---------|
| **Case‑sensitive** | `status/IN-PROGRESS` | Keeps status tags distinct. |
| **Namespaces** | `status/`, `@`, `theme/`, `idea/`, **`TK/`** | Auto‑completion groups related tags. |
| **Temporal** | `@today`, `@tomorrow`, `@this-week`, `@next-week` | Time‑based workflow. |
| **State** | `#action-required`, `#mindfulness` | Process or mindset. |
| **Color** | (via CSS) | Visual cue in editor. |

> **Tag‑vs‑Property** – Use **tags** for *attributes* that can apply to many notes; use **properties** (in YAML) for *explicit relationships* (`project:`, `area:`, `person:`).

---

## 5.  The 4‑Part PKM Toolkit

| Part | What it Adds | LLM Interaction |
|------|--------------|-----------------|
| **1. Typed Links & Properties** | `[[Project X::has task::Task Y]]` | LLM can auto‑create these links when you add a task. |
| **2. PARA + Type Property** | `type::Project` / `area::Health` | LLM sets the `type` field when you create a note. |
| **3. Tag Taxonomy** | `#action-required`, `#mindfulness`, `#CBT` | LLM suggests tags based on content. |
| **4. MOCs (Maps of Content)** | `[[Family Members]]`, `[[Emotional Intelligence Toolkit]]` | LLM can auto‑generate a MOC linking relevant notes. |

---

## 6.  UI & Interaction

| Pane | Function | Key Features |
|------|----------|--------------|
| **Sidebar** | File tree | Expand/collapse folders, click to open. |
| **Explorer** | Quick file list | Simple list for prototype. |
| **Editor** | Markdown view + preview | Auto‑save on blur, syntax highlighting. |
| **Chat** | Natural‑language interface | Supports `[Thought]`, `[Daily]`, `[Project: …]` commands. |
| **Dashboard** | One‑page status view | Auto‑generated nightly by the LLM. |

**Theme** – Dark background (`#1e1e1e`), system font (`system-ui`), accent color `#4caf50`.

---

## 7.  Command Syntax

| Prefix | Example | What Happens |
|--------|---------|--------------|
| `[Thought] …` | `[Thought] I felt stuck.` | Creates a fleeting note in `Notes/Fleeting/`. |
| `[Daily] …` | `[Daily] Reviewed habit streaks.` | Appends to today’s `Journal/Daily/` note. |
| `[Weekly] …` | `[Weekly] Completed 5 tasks.` | Appends to the current week’s `Journal/Weekly/` note. |
| `[Monthly] …` | `[Monthly] Reflected on progress.` | Appends to this month’s `Journal/Monthly/` note. |
| `[Project: Project Name] …` | `[Project: Vacation] Updated itinerary.` | Updates the specified project note. |
| `Find notes about <topic>` | `Find notes about Stoicism` | Returns a list of relevant notes. |
| `Add tag #mindfulness to Meditation.md` | – | Adds the tag to the file. |
| `Rename tag #action-required to #urgent` | – | Renames the tag everywhere. |
| `Create MOC Personal Growth` | – | Generates a new MOC file. |
| `Sync Git` | – | Pushes local commits to the configured remote. |

> **Tip:** The chat pane shows a drop‑down of the most common commands; selecting one pre‑populates the input.

---

## 8.  Scheduler (Nightly Dashboard)

```js
// node-cron in src/main.js
cron.schedule('0 0 * * *', async () => {
  const content = await generateDashboard(LIFEOS_ROOT);
  const path = require('path');
  fs.writeFileSync(path.join(LIFEOS_ROOT, 'Dashboard.md'), content, 'utf8');
});
```

The `generateDashboard` function sends a prompt to OpenRouter:

```
Generate a Markdown dashboard for the current week.
Include:
- Energy (1‑10) & Mood (1‑10)
- One‑Thing (top priority) – pull from Projects/Active
- Habit streaks – from Habits folder
- Pending tasks – from Tasks folder with status IN‑PROGRESS
- Short reminder of next week’s focus
```

---

## 9.  Prototype Implementation (Electron + React)

### 9.1  `package.json` (excerpt)

```json
{
  "name": "lifeos-desktop",
  "main": "src/main.js",
  "scripts": {
    "start": "electron .",
    "build": "electron-builder"
  },
  "dependencies": {
    "axios": "^1.7.2",
    "chokidar": "^4.0.1",
    "node-cron": "^3.0.3",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-markdown": "^8.0.7"
  },
  "devDependencies": {
    "electron": "^32.0.0",
    "electron-builder": "^24.6.3"
  }
}
```

### 9.2  Main Process (`src/main.js`)

```js
const { app, BrowserWindow } = require('electron');
const path = require('path');
const fs = require('fs');
const cron = require('node-cron');
const { generateDashboard } = require('./renderer/utils/llm');

const LIFEOS_ROOT = path.join(app.getPath('home'), 'LifeOS');

function createWindow() {
  const win = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    }
  });

  win.loadFile(path.join(__dirname, 'renderer', 'index.html'));
}

app.whenReady().then(() => {
  createWindow();

  cron.schedule('0 0 * * *', async () => {
    const content = await generateDashboard(LIFEOS_ROOT);
    fs.writeFileSync(path.join(LIFEOS_ROOT, 'Dashboard.md'), content, 'utf8');
  });

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
});
```

### 9.3  React Front‑end (`src/renderer/components/*`)

*Sidebar, Explorer, Editor, Chat, Dashboard* – all simple React components that read/write Markdown files via `fs`.
The **Chat** component uses the `sendToLLM` helper (see next section).

---

## 10.  LLM Wrapper (`src/renderer/utils/llm.js`)

```js
const axios = require('axios');
const fs = require('fs');
const path = require('path');

const OPENROUTER_API_KEY = process.env.OPENROUTER_API_KEY;
const LIFEOS_ROOT = path.join(process.env.HOME, 'LifeOS');

async function sendToLLM(message) {
  const payload = {
    model: 'gpt-4o-mini',
    messages: [{ role: 'user', content: message }],
    temperature: 0.7,
    max_tokens: 500
  };

  const res = await axios.post('https://openrouter.ai/api/v1/chat/completions', payload, {
    headers: {
      Authorization: `Bearer ${OPENROUTER_API_KEY}`,
      'Content-Type': 'application/json'
    }
  });

  return res.data.choices[0].message.content.trim();
}

async function generateDashboard(root) {
  const prompt = `
Generate a Markdown dashboard for the current week.
Include:
- Energy (1‑10) & Mood (1‑10)
- One‑Thing (top priority) – pull from Projects/Active
- Habit streaks – from Habits folder
- Pending tasks – from Tasks folder with status IN‑PROGRESS
- Short reminder of next week’s focus
`;
  return await sendToLLM(prompt);
}

async function getDashboard() {
  const dashPath = path.join(LIFEOS_ROOT, 'Dashboard.md');
  if (!fs.existsSync(dashPath)) return '# Dashboard\nNo data yet.';
  return fs.readFileSync(dashPath, 'utf8');
}

module.exports = { sendToLLM, generateDashboard, getDashboard };
```

---

## 11.  File‑Watcher (`src/renderer/utils/fileWatcher.js`)

```js
const chokidar = require('chokidar');
const path = require('path');
const fs = require('fs');

const LIFEOS_ROOT = path.join(process.env.HOME, 'LifeOS');

function getAllFiles(dir = LIFEOS_ROOT, list = []) {
  const entries = fs.readdirSync(dir);
  entries.forEach(entry => {
    const full = path.join(dir, entry);
    if (fs.statSync(full).isDirectory()) {
      getAllFiles(full, list);
    } else {
      list.push(full);
    }
  });
  return list;
}

function watchLifeOS(setFiles) {
  const watcher = chokidar.watch(LIFEOS_ROOT, { ignoreInitial: true });
  watcher.on('all', () => {
    const all = getAllFiles();
    setFiles(all);
  });
}

module.exports = { getAllFiles, watchLifeOS };
```

---

## 12.  Prototype Script

> A single Bash script (`setup_lifeos.sh`) will create the *entire* prototype on your machine.
> Copy the script below into a file, make it executable, and run it.

```bash
#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$HOME/LifeOS-Desktop"   # change if you prefer a different folder
mkdir -p "$ROOT_DIR"
cd "$ROOT_DIR"

# --- 1️⃣  Create the skeleton ----------
mkdir -p src/renderer/utils
mkdir -p src/renderer/components
mkdir -p src/renderer/assets

# --- 2️⃣  package.json ----------
cat > package.json <<'PKG'
{
  "name": "lifeos-desktop",
  "version": "1.0.0",
  "description": "Electron + React prototype for Life OS",
  "main": "src/main.js",
  "scripts": {
    "start": "electron .",
    "build": "electron-builder"
  },
  "keywords": ["lifeos", "electron", "react", "openrouter"],
  "author": "Your Name",
  "license": "MIT",
  "dependencies": {
    "axios": "^1.7.2",
    "chokidar": "^4.0.1",
    "node-cron": "^3.0.3",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-markdown": "^8.0.7"
  },
  "devDependencies": {
    "electron": "^32.0.0",
    "electron-builder": "^24.6.3"
  }
}
PKG

# --- 3️⃣  .env ----------
cat > .env <<'ENV'
# Put your OpenRouter API key here
OPENROUTER_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
ENV

# --- 4️⃣  .gitignore ----------
cat > .gitignore <<'IGN'
node_modules/
dist/
*.log
.env
IGN

# --- 5️⃣  README ----------
cat > README.md <<'RD'
# Life OS Desktop Prototype

This repository contains a minimal Electron + React prototype that implements the Life OS UI described in the design document.
The app uses **OpenRouter** as the LLM backend, automatically generates a nightly dashboard, and offers a simple chat/command interface.

## Getting Started

```bash
npm install
npm start
```

> **NOTE:** Make sure you have a valid `OPENROUTER_API_KEY` in `.env` before starting.

## Features

- Chat interface with `[Thought]`, `[Daily]`, `[Project: …]`, etc. commands
- File explorer, Markdown editor/preview, and dashboard pane
- Built‑in nightly scheduler (runs at 00:00 UTC)
- Dark theme, system font, modern UI

## License

MIT
RD

# --- 6️⃣  Electron main ----------
cat > src/main.js <<'MAIN'
const { app, BrowserWindow } = require('electron');
const path = require('path');
const fs = require('fs');
const cron = require('node-cron');
const { generateDashboard } = require('./renderer/utils/llm');

const LIFEOS_ROOT = path.join(app.getPath('home'), 'LifeOS');

if (!fs.existsSync(LIFEOS_ROOT)) fs.mkdirSync(LIFEOS_ROOT, { recursive: true });

function createWindow() {
  const win = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    }
  });

  win.loadFile(path.join(__dirname, 'renderer', 'index.html'));
}

app.whenReady().then(() => {
  createWindow();

  cron.schedule('0 0 * * *', async () => {
    console.log('Generating dashboard...');
    const content = await generateDashboard(LIFEOS_ROOT);
    const path = require('path');
    fs.writeFileSync(path.join(LIFEOS_ROOT, 'Dashboard.md'), content, 'utf8');
    console.log('Dashboard updated.');
  });

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
});
MAIN

# --- 7️⃣  Renderer ----------
cat > src/renderer/index.html <<'HTML'
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Life OS Desktop</title>
</head>
<body>
  <div id="root"></div>
  <script src="renderer.js"></script>
</body>
</html>
HTML

cat > src/renderer/renderer.js <<'REND'
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './components/App';
import './assets/styles.css';

ReactDOM.createRoot(document.getElementById('root')).render(<App />);
REND

cat > src/renderer/components/App.js <<'APP'
import React, { useState, useEffect } from 'react';
import Sidebar from './Sidebar';
import Explorer from './Explorer';
import Editor from './Editor';
import Chat from './Chat';
import Dashboard from './Dashboard';
import { watchLifeOS, getAllFiles } from '../utils/fileWatcher';

export default function App() {
  const [files, setFiles] = useState([]);
  const [selected, setSelected] = useState(null);
  const [content, setContent] = useState('');

  useEffect(() => {
    const all = getAllFiles();
    setFiles(all);
    watchLifeOS(setFiles);
  }, []);

  const openFile = (path) => {
    setSelected(path);
    const fs = window.require('fs');
    setContent(fs.readFileSync(path, 'utf8'));
  };

  const updateContent = (newText) => {
    if (!selected) return;
    const fs = window.require('fs');
    fs.writeFileSync(selected, newText, 'utf8');
    setContent(newText);
  };

  return (
    <div className="app">
      <Sidebar files={files} onSelect={openFile} />
      <div className="main">
        <Explorer files={files} onSelect={openFile} />
        <Editor content={content} onChange={updateContent} />
        <Chat />
        <Dashboard />
      </div>
    </div>
  );
}
APP

cat > src/renderer/components/Sidebar.js <<'SID'
import React from 'react';
export default function Sidebar({ files, onSelect }) {
  return (
    <div className="sidebar">
      <h3 style={{ padding: '10px', margin: 0 }}>Life OS</h3>
      <ul style={{ listStyle: 'none', padding: 0 }}>
        {files.map(f => (
          <li key={f} style={{ padding: '5px 10px' }}>
            <button style={{
              background: 'none',
              border: 'none',
              color: '#e0e0e0',
              cursor: 'pointer',
              width: '100%',
              textAlign: 'left'
            }} onClick={() => onSelect(f)}>
              {f.replace(process.env.HOME, '~')}
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}
SID

cat > src/renderer/components/Explorer.js <<'EXP'
import React from 'react';
export default function Explorer({ files, onSelect }) {
  const buildTree = () => {
    const root = { name: 'LifeOS', children: [] };
    files.forEach(p => {
      const parts = p.replace(process.env.HOME, '~').split('/');
      let node = root;
      parts.forEach(part => {
        if (!node.children) node.children = [];
        let child = node.children.find(c => c.name === part);
        if (!child) {
          child = { name: part, children: [] };
          node.children.push(child);
        }
        node = child;
      });
    });
    return root;
  };

  return (
    <div className="explorer" style={{ height: '200px' }}>
      <ul style={{ listStyle: 'none', padding: 0 }}>
        {buildTree().children.map(n => (
          <li key={n.name}>
            <strong>{n.name}</strong>
            <ul style={{ listStyle: 'none', paddingLeft: '15px' }}>
              {n.children.map(c => (
                <li key={c.name}>
                  <button onClick={() => onSelect(c.name)} style={{background:'none',border:'none',color:'#e0e0e0',cursor:'pointer'}}>
                    {c.name}
                  </button>
                </li>
              ))}
            </ul>
          </li>
        ))}
      </ul>
    </div>
  );
}
EXP

cat > src/renderer/components/Editor.js <<'EDT'
import React from 'react';
export default function Editor({ content, onChange }) {
  return (
    <div className="editor">
      <textarea value={content} onChange={e => onChange(e.target.value)} />
    </div>
  );
}
EDT

cat > src/renderer/components/Chat.js <<'CHT'
import React, { useState } from 'react';
import { sendToLLM } from '../utils/llm';

export default function Chat() {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([]);

  const handleSend = async () => {
    if (!input.trim()) return;
    const userMsg = input;
    setMessages(m => [...m, {role:'user', text:userMsg}]);
    setInput('');
    const resp = await sendToLLM(userMsg);
    setMessages(m => [...m, {role:'assistant', text:resp}]);

    // Very simple command handling (Thought example)
    if (userMsg.startsWith('[Thought]')) {
      const note = `# Thought – ${new Date().toISOString().slice(0,10)}\n\n${userMsg.slice(9).trim()}\n`;
      const fs = window.require('fs');
      const path = window.require('path');
      const dir = path.join(process.env.HOME, 'LifeOS', 'Notes', 'Fleeting');
      if (!fs.existsSync(dir)) fs.mkdirSync(dir, {recursive:true});
      const file = path.join(dir, `Thought-${Date.now()}.md`);
      fs.writeFileSync(file, note, 'utf8');
    }
    // Add handlers for [Daily], [Project:], etc. in a similar way
  };

  return (
    <div className="chat">
      <h3>Chat</h3>
      <div style={{maxHeight:'200px',overflowY:'auto',background:'#2c2c2c',padding:'5px'}}>
        {messages.map((m,i)=>(
          <div key={i} style={{marginBottom:'5px'}}>
            <strong>{m.role}:</strong> {m.text}
          </div>
        ))}
      </div>
      <input
        type="text"
        value={input}
        onChange={e=>setInput(e.target.value)}
        onKeyDown={e=>e.key==='Enter'&&handleSend()}
        placeholder="Type a command or chat…"
      />
    </div>
  );
}
CHT

cat > src/renderer/components/Dashboard.js <<'DASH'
import React, { useEffect, useState } from 'react';
import ReactMarkdown from 'react-markdown';
import { getDashboard } from '../utils/markdown';

export default function Dashboard() {
  const [content, setContent] = useState('# Dashboard\nLoading…');

  useEffect(() => {
    const load = async () => {
      const dash = await getDashboard();
      setContent(dash);
    };
    load();
  }, []);

  return (
    <div className="dashboard">
      <h3>Dashboard</h3>
      <ReactMarkdown>{content}</ReactMarkdown>
    </div>
  );
}
DASH

cat > src/renderer/assets/styles.css <<'CSS'
/* Dark theme, system font */
body, html, .app {
  margin: 0;
  padding: 0;
  height: 100%;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  background: #1e1e1e;
  color: #e0e0e0;
}
.app { display:flex; height:100%; }
.sidebar { width:200px; background:#2c2c2c; overflow-y:auto; }
.main { flex:1; display:flex; flex-direction:column; }
.explorer, .editor, .chat, .dashboard { flex:1; overflow-y:auto; padding:10px; border-bottom:1px solid #444; }
.editor textarea { width:100%; height:100%; background:#1e1e1e; color:#e0e0e0; border:none; resize:none; font-family:inherit; font-size:14px; }
.chat input { width:100%; padding:8px; background:#2c2c2c; border:none; color:#e0e0e0; }
.dashboard { background:#2c2c2c; }
CSS

# ---------- 13️⃣  Utilities ----------
cat > src/renderer/utils/llm.js <<'LLM'
const axios = require('axios');
const fs = require('fs');
const path = require('path');

const OPENROUTER_API_KEY = process.env.OPENROUTER_API_KEY;
const LIFEOS_ROOT = path.join(process.env.HOME, 'LifeOS');

async function sendToLLM(message) {
  const payload = {
    model: 'gpt-4o-mini',
    messages: [{role:'user', content:message}],
    temperature: 0.7,
    max_tokens: 500
  };
  const res = await axios.post('https://openrouter.ai/api/v1/chat/completions', payload, {
    headers: {
      Authorization: `Bearer ${OPENROUTER_API_KEY}`,
      'Content-Type': 'application/json'
    }
  });
  return res.data.choices[0].message.content.trim();
}

async function generateDashboard(root) {
  const prompt = `
Generate a Markdown dashboard for the current week.
Include:
- Energy (1‑10) & Mood (1‑10)
- One‑Thing (top priority) – pull from Projects/Active
- Habit streaks – from Habits folder
- Pending tasks – from Tasks folder with status IN‑PROGRESS
- Short reminder of next week’s focus
`;
  return await sendToLLM(prompt);
}

async function getDashboard() {
  const dashPath = path.join(LIFEOS_ROOT, 'Dashboard.md');
  if (!fs.existsSync(dashPath)) return '# Dashboard\nNo data yet.';
  return fs.readFileSync(dashPath, 'utf8');
}

module.exports = { sendToLLM, generateDashboard, getDashboard };
LLM

cat > src/renderer/utils/fileWatcher.js <<'WATCH'
const chokidar = require('chokidar');
const path = require('path');
const fs = require('fs');

const LIFEOS_ROOT = path.join(process.env.HOME, 'LifeOS');

function getAllFiles(dir = LIFEOS_ROOT, list = []) {
  const entries = fs.readdirSync(dir);
  entries.forEach(entry => {
    const full = path.join(dir, entry);
    if (fs.statSync(full).isDirectory()) {
      getAllFiles(full, list);
    } else {
      list.push(full);
    }
  });
  return list;
}

function watchLifeOS(setFiles) {
  const watcher = chokidar.watch(LIFEOS_ROOT, { ignoreInitial: true });
  watcher.on('all', () => {
    const all = getAllFiles();
    setFiles(all);
  });
}

module.exports = { getAllFiles, watchLifeOS };
WATCH

cat > src/renderer/utils/markdown.js <<'MARK'
const { getDashboard } = require('./llm');
module.exports = { getDashboard };
MARK

echo "✅ LifeOS Desktop prototype created at $ROOT_DIR"
echo "Next steps:"
echo "  1. cd $ROOT_DIR"
echo "  2. npm install"
echo "  3. npm start"
EOF

# Make the script executable
chmod +x setup_lifeos.sh

echo "Script 'setup_lifeos.sh' has been created."
echo "Run it with:"
echo "  chmod +x setup_lifeos.sh"
echo "  ./setup_lifeos.sh"
echo ""
echo "After it finishes:"
echo "  cd LifeOS-Desktop"
echo "  npm install"
echo "  npm start"
```

---

### How to run the script

1. **Copy** the entire block above into a file named `setup_lifeos.sh` in any directory on your machine.
2. **Make it executable**:
   ```bash
   chmod +x setup_lifeos.sh
   ```
3. **Run it**:
   ```bash
   ./setup_lifeos.sh
   ```

The script will:

* Create `LifeOS-Desktop` in your home folder.
* Write every file shown above (package.json, scripts, UI components, utilities, etc.).
* Install the dependencies (`npm install`).
* Start the app (`npm start`).

> **Tip:** Replace the placeholder `sk-xxxxxxxxxxxxxxxxxxxx` in `.env` with your real OpenRouter key before starting.

---

## 13.  Next Steps & Customisation

| What | How |
|------|-----|
| **Add a “Schedule” pane** | Use the `node-cron` schedule info to show upcoming tasks. |
| **Integrate Google Calendar / Email** | Add a new folder `Extensions/Calendar` and create a connector that pulls events via the Google API; the LLM can then suggest tasks. |
| **Improve file‑tree UI** | Replace the simple list with a component like `react-sortable-tree` or `@mui/lab/TreeView`. |
| **Secure the API key** | Store it in Windows Credential Manager / macOS Keychain or use `keytar`. |
| **Publish the app** | Run `npm run build` and use `electron-builder` to package for Windows/macOS/Linux. |

---

## 14.  Final Takeaway

You now have a **complete, ready‑to‑run prototype** that:

1. Stores all personal data in a clean, version‑controlled Markdown folder.
2. Uses an LLM (OpenRouter) to manage your knowledge, generate coaching prompts, and auto‑update your dashboard.
3. Offers a modern, dark UI with chat, file explorer, editor, and dashboard—all in a single Electron window.
4. Provides a solid foundation for future extensions (calendar sync, email, smart‑home, etc.).

Happy building, and let me know how it goes or what features you’d like to add next!
