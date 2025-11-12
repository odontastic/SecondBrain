# Copilot Instructions for SecondBrain (LifeOS)

This file gives concise, project-specific guidance to an AI coding/content agent (Copilot-like) working in this repository.

Principles (what to keep in mind)
- This repo is a personal "Second Brain" / Life OS: content-first, markdown-driven, and optimized for an AI collaborator (Cursor/Claude style agents).
- Preserve the author's voice: most notes are intended to read in first-person. Many agent workflows explicitly ask the assistant to write notes in first-person.
- Be conservative with destructive edits: content is the primary artifact. When moving or deleting files, confirm intent and create backups or note the change in a commit message.
- Ask clarifying questions when intent is ambiguous (e.g., where should this note go, which project should be updated). The `.cursor/rules/life-operating-system.mdc` file emphasizes clarifying questions and human-aligned coaching.

Primary workflows (how the agent should operate)
- Initialization (Cursor-style agents): run the repository README's initialization prompt: `start initializing Second Brain`. This triggers agent behaviors and expected storage locations.
- Capture flows: save raw thoughts to `Notes/Fleeting/` and use the provided fleeting note template from `README.md`. Example: `Notes/Fleeting/2025-11-11_my_thought.md`.
- Project updates: update `01-Projects/Active/<project>.md` when the user reports progress. Use the project's frontmatter template (title/date/type/status/tags) shown in `README.md`.
- Journals: store daily entries in `Journal/Daily/YYYY-MM-DD.md`. Use the daily prefix `[Daily]` in user messages as indicated in `README.md`.
- Screenshot OCR: follow the documented command in `README.md` — screenshots are saved to `Resources/Screenshots/` and raw OCR text goes into a fleeting note. Example command: `Commands/screenshot.sh /path/to/screenshot.png --title "Meeting notes"`.

Conventions and examples (concrete patterns found in this repo)
- File structure: the top-level folders are `01-Projects/`, `02-Areas/`, `03-Resources/`, `04-Archives/`, `05-Documentation/`, plus working folders like `Inbox/`, `Journal/`, `Notes/`, `People/`, and `Tags/`.
- Filenames: prefer descriptive kebab_case or snake_case. Include dates when appropriate, e.g., `2023-10-15_project_milestone.md`.
- Frontmatter / templates: for projects use the frontmatter example in `README.md`. For fleeting notes use the provided template header `# [Topic] - Initial Thoughts` and include metadata fields (Created/Tags/Status).
- Voice: when a user asks the agent to "capture" a thought or create a note, write the content in first-person voice that sounds like the repository owner.

Integration points and tools
- Cursor: agent interactions will often be initiated from Cursor and rely on the `start initializing Second Brain` prompt. Expect to use Cursor APIs/behaviors when available.
- Commands: `Commands/` may include helper shells (e.g., screenshot processing). Prefer using these scripts over inventing new file operations.
- Git: use descriptive commits and, for moves/renames, leave a small migration note in the commit message. Avoid force-pushing without user confirmation.

What agents should NOT do without explicit instruction
- Do not rewrite large swathes of notes to change voice or content meaning.
- Do not merge or archive large folders without asking (e.g., `04-Archives/` operations must be explicit).
- Do not publish or expose personal contact details found under `People/` without the owner's instruction.

Quick examples to include in edits (copyable)
- Create a fleeting note from a message: save to `Notes/Fleeting/{timestamp}_{short-title}.md` with the fleeting note template from `README.md`.
- Update a project progress line: open `01-Projects/Active/{project}.md`, append a new bullet under "Current Status" with date and short summary.
- Process screenshot: run `Commands/screenshot.sh /tmp/shot.png --title "Receipt"` then create `Notes/Fleeting/{timestamp}_receipt.md` with OCR text and a link to `Resources/Screenshots/{file}`.

Files to consult when unsure
- `README.md` (root) — canonical templates, workflow triggers, prefixes
- `.cursor/rules/life-operating-system.mdc` — behavior and high-level assistant principles
- `Commands/` — scripts for screenshot/OCR and other file operations (if present)
- `01-Projects/`, `Journal/`, `Notes/`, `03-Resources/`, `People/` — canonical locations for content

Small operational contract (inputs/outputs)
- Input: short user message with an explicit prefix (e.g., `[Daily]`, `[Thought]`, `[Project: X]`) or an uploaded screenshot.
- Output: a new or updated markdown file in the correct folder, a short confirmation message listing the changed file(s), and a brief summary of what was added.

Edge cases and guardrails
- If multiple candidate locations match (e.g., similar project names), ask a single clarifying question rather than guessing.
- If writing to `People/` or `Contacts/`, ensure contact data is stored in the private preferred format and do not export it elsewhere.
- For ambiguous dates/times, default to ISO date in filename and frontmatter: `YYYY-MM-DD`.

If you think more instructions or examples are needed, tell me which part felt unclear and I'll iterate. Thank you.