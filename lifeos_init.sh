#!/usr/bin/env bash
set -euo pipefail

ROOT="$HOME/Documents/LifeOS"
mkdir -p "$ROOT"

# ---------- PARA STRUCTURE ----------
mkdir -p "$ROOT/Projects/Active" "$ROOT/Projects/Completed"
mkdir -p "$ROOT/Projects/Active/Self-Improvement" \
         "$ROOT/Projects/Completed/Self-Improvement"

mkdir -p "$ROOT/Areas/Family" \
         "$ROOT/Areas/House" \
         "$ROOT/Areas/Yard" \
         "$ROOT/Areas/Food" \
         "$ROOT/Areas/Home_School" \
         "$ROOT/Areas/Faith"

mkdir -p "$ROOT/Resources" \
         "$ROOT/Resources/Books" \
         "$ROOT/Resources/Articles" \
         "$ROOT/Resources/Videos" \
         "$ROOT/Resources/Courses" \
         "$ROOT/Resources/Templates"

mkdir -p "$ROOT/Journal/Daily" "$ROOT/Journal/Weekly" "$ROOT/Journal/Monthly"
mkdir -p "$ROOT/Habits" "$ROOT/Metrics" "$ROOT/Logs"
mkdir -p "$ROOT/People/Personal" "$ROOT/People/Professional"
mkdir -p "$ROOT/Extensions" "$ROOT/Archives"
mkdir -p "$ROOT/MOCs"

# ---------- META/TAGS ----------
cat >"$ROOT/People/Personal/tags.md" <<'EOF'
# Meta Tags

## Tag Conventions
- **Status** – status/IN-PROGRESS, status/EDITING, status/PUBLISHED
- **Temporal** – @today, @tomorrow, @this-week, @next-week
- **Theme** – theme/mindfulness, theme/stoicism, theme/CBT, theme/habit-stacking
- **Idea** – idea/xyz, idea/abc
- **Hang Tags** – #12-note-taking
- **To Kome** – TK/ (unfinished or to-revise notes)
EOF

# ---------- MOCs ----------
cat >"$ROOT/MOCs/Family.md" <<'EOF'
# Family MOC

- [[Wife]]
- [[Son A]]
- [[Son B]]
- [[Father]]

> *Relationship note:* The family is the core of my personal values and informs my daily actions.
EOF

cat >"$ROOT/MOCs/Projects.md" <<'EOF'
# Projects MOC

- [[Project Alpha]]
- [[Project Beta]]
- [[Self-Improvement]]
- [[Career Development]]

> *Note:* Projects are action-oriented and have start/end dates.
EOF

cat >"$ROOT/MOCs/Skills.md" <<'EOF'
# Skills MOC

- [[Python]]
- [[Public Speaking]]
- [[Mindfulness]]
- [[Relationship Skills]]

> *Note:* Skills are the building blocks of personal growth.
EOF

echo "✔️ Life OS skeleton created at: $ROOT"
