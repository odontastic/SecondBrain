#!/usr/bin/env bash
set -euo pipefail

ROOT="$HOME/Documents/LifeOS"
mkdir -p "$ROOT"

# PARA structure
mkdir -p "$ROOT/Projects/Active" "$ROOT/Projects/Completed"
mkdir -p "$ROOT/Projects/Active/Self-Improvement"/{Health,Skills,Relationships,Finance,Spiritual,Career,Creativity}
mkdir -p "$ROOT/Areas"/{Family,House,Yard,Food,Home_School,Faith}
mkdir -p "$ROOT/Resources"/{Books,Articles,Videos,Courses,Templates}
mkdir -p "$ROOT/Journal"/{Daily,Weekly,Monthly}
mkdir -p "$ROOT"/{Habits,Metrics,Logs,MOCs,Archives,Extensions}
mkdir -p "$ROOT/People"/{Personal,Professional}

# Initialize git
cd "$ROOT"
git init
git config user.name "Life OS"
git config user.email "lifeos@localhost"

# Create meta/tags.md
cat >"$ROOT/meta/tags.md" <<'EOF'
# Tag Taxonomy

## Conventions
- Status: `status/IN-PROGRESS`, `status/EDITING`, `status/PUBLISHED`
- Temporal: `@today`, `@tomorrow`, `@this-week`, `@next-week`
- Theme: `theme/mindfulness`, `theme/stoicism`, `theme/CBT`
- TK: `TK/` (to come - needs work)

## Active Tags
- `#action-required` - Needs immediate attention
- `#revisit-later` - Scheduled review
- `#spiritual-growth` - Faith-related
- `#family-priority` - Impacts relationships
- `#distill` - Needs summarization
- `#synthesize` - Needs integration
- `#apply` - Ready for action
EOF
