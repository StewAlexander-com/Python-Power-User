# Python Power User

A complete Python language reference and interactive learning tool in a single file. No installs, no dependencies, no setup. Just run it.

**47 sections** across 15 parts — from your first variable to the patterns that separate senior devs from everyone else. Read it in VS Code or run it in your terminal for the full experience.

Built with the help of [Perplexity Computer](https://www.perplexity.ai/).

---

## The TUI

Not a wall of text. A real terminal interface with two-pane navigation, syntax highlighting, and vim keys.

![Main Menu](screenshots/tui-main-menu.png)

Browse any section's source with Monokai-themed syntax highlighting, line numbers, and scroll.

![Syntax-Highlighted Viewer](screenshots/tui-viewer.png)

---

## Quick Start

```bash
python python_poweruser.py
```

That's it. Arrow keys or j/k to navigate, Enter to open, / to search, q to quit.

```bash
python python_poweruser.py -s decorators   # Jump straight to a section
python python_poweruser.py -f lambda        # Search across all 47 sections
python python_poweruser.py -l               # See everything at a glance
python python_poweruser.py -r               # Run all demos back to back
python python_poweruser.py -t               # Take the interactive quiz
```

Typo? It'll suggest what you meant. Wrong flag? It'll tell you why and how to fix it. Piped to `head`? No crash. No curses? Falls back gracefully. It handles the weird stuff so you don't have to.

---

## The Quiz

Not a checkbox test. You read the expression, type what you think Python will do, and hit Enter.

```
  [6/20] What does this evaluate to?
         bool([0])

    > False
    Not quite — the answer is True
    This one trips up a lot of people! The list contains something,
             so it's truthy — even though that something is 0.
             Python checks 'is the container empty?', not 'are the
             contents truthy?'.  [0] has one element → True.
```

Get it right and you'll learn something extra you didn't know. Get it wrong and the explanation actually teaches you why — no shame, no "WRONG", just "here's what's happening under the hood."

At the end, it tells you exactly which sections to revisit and gives you the command to get there:

```
  Sections worth revisiting:
    → 04 Booleans & None  (python python_poweruser.py -s booleans)
    → 07 Dictionaries  (python python_poweruser.py -s dicts)
```

---

## What's Inside

| Part | Topic | Sections |
|------|-------|----------|
| 1 | Foundations | Variables & Types, Numbers, Strings, Booleans |
| 2 | Data Structures | Lists, Tuples, Dicts, Sets, Advanced Structures |
| 3 | Control Flow | Conditionals, Loops, Comprehensions |
| 4 | Functions | Basics, Scope & Closures, Lambda, Decorators, Functools |
| 5 | OOP | Classes, Inheritance, Dunders, Properties, ABCs |
| 6 | Error Handling | Exceptions, Context Managers, Custom Exceptions |
| 7 | Iterators & Generators | Iterators, Generators, itertools |
| 8 | File I/O | File Ops, JSON & CSV, Pathlib |
| 9 | Text Mastery | Regex, String Formatting, Datetime |
| 10 | Stdlib Tools | Collections, OS & Subprocess, Typing |
| 11 | The Edge | Idioms, Performance, Gotchas |
| 12 | Reference Tables | Operator Precedence, Built-ins, Exception Hierarchy |
| 13 | Env & Tooling | Virtual Environments, Debugging & Profiling |
| 14 | Recipes | One-Liner Recipes |
| A | Appendix | Cheat Sheet |

Every section has Einstein/Feynman-style explanations that make hard concepts click fast. Comments are written to teach, not to document.

---

## VS Code Setup

Three extensions, one-time install:

1. **Python** (`ms-python.python`) — enables Run Cell, IntelliSense, and the `# %%` cell markers
2. **Better Comments** — colors the `#*` `#!` `#?` `#TODO` markers used throughout
3. **Indent Rainbow** — makes nesting depth visually obvious

Then: `Ctrl+K Ctrl+0` to fold everything, unfold the section you're studying. Each `# %%` marker is a runnable cell.

---

## Requirements

- Python 3.10+ (uses `match/case`)
- A terminal with at least 80×22 for the TUI
- No external dependencies — stdlib only
- `windows-curses` auto-installs on Windows if needed

## License

MIT
