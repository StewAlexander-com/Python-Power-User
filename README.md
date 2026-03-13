# Python Power User

A comprehensive Python language reference & interactive TUI learning tool in a single file.

- **47 sections** across 15 parts — from Foundations to Competitive Edge
- **Monokai-themed curses TUI** with two-pane navigation, syntax highlighting, and search
- **Fault-tolerant CLI** with argparse, fuzzy matching, and graceful fallbacks
- **20-question self-test** quiz
- **VS Code optimized** with `# %%` cell markers, Better Comments support, and fold-friendly structure

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

## VS Code Setup

1. Install the **Python** extension (`ms-python.python`)
2. Install **Better Comments** — colors the `#*` `#!` `#?` `#TODO` markers
3. Install **Indent Rainbow** — makes nesting visually obvious

## Requirements

- Python 3.10+ (uses `match/case` syntax)
- No external dependencies — stdlib only
- `windows-curses` auto-installed on Windows if needed
