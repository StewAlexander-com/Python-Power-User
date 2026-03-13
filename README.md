# Python Power User

A comprehensive Python language reference & interactive TUI learning tool — all in a single file.

**47 sections** across 15 parts, from Foundations to Competitive Edge. Read it in VS Code, or run it in your terminal for a full curses-based interactive experience.

Built with the help of [Perplexity Computer](https://www.perplexity.ai/).

---

## TUI

![Main Menu](screenshots/tui-main-menu.png)

![Syntax-Highlighted Viewer](screenshots/tui-viewer.png)

---

## Quick Start

```bash
# Interactive TUI
python python_poweruser.py

# List all sections
python python_poweruser.py -l

# Run a specific section
python python_poweruser.py -s decorators

# Search
python python_poweruser.py -f lambda

# Self-test quiz
python python_poweruser.py -t

# Run all demos
python python_poweruser.py -r
```

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

## Features

- **Monokai-themed curses TUI** — two-pane navigation, syntax highlighting, search, vim keys
- **Fault-tolerant CLI** — argparse with fuzzy matching, graceful fallbacks, never crashes
- **20-question self-test** — predict the output, learn from hints
- **VS Code optimized** — `# %%` cell markers, fold-friendly structure, Better Comments support
- **Zero dependencies** — stdlib only (`windows-curses` auto-installed on Windows if needed)

## VS Code Setup

1. Install the **Python** extension (`ms-python.python`)
2. Install **Better Comments** — colors the `#*` `#!` `#?` `#TODO` markers
3. Install **Indent Rainbow** — makes nesting visually obvious

## Requirements

- Python 3.10+ (uses `match/case` syntax)
- A terminal with at least 80×22 for the TUI (adapts to larger)

## License

MIT
