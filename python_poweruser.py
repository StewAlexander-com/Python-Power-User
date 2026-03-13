#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ─────────────────────────────────────────────────────────────────────────────
# PYTHON POWER USER — A Complete Language Reference in One File
# ─────────────────────────────────────────────────────────────────────────────
#
#   "If you can't explain it simply, you don't understand it well enough."
#                                                        — Albert Einstein
#
#   "The first principle is that you must not fool yourself—and you are
#    the easiest person to fool."
#                                                       — Richard Feynman
#
# ─────────────────────────────────────────────────────────────────────────────
#
#  HOW TO USE THIS FILE
#  ────────────────────
#  This is a REFERENCE, not a textbook. It's designed to be:
#    • Skimmed fast when you need a refresher
#    • Read section-by-section when learning a topic
#    • Searched with Ctrl+F when you need a specific pattern
#    • Run as a script to see everything in action
#
#  VS CODE SETUP (do these once, thank me forever):
#    1. Install "Python" extension (ms-python.python) — enables Run Cell,
#       IntelliSense, linting, and the # %% cell markers used throughout
#    2. Install "Better Comments" extension — colors the #* #! #? #TODO markers
#    3. Install "Indent Rainbow" — makes nesting visually obvious
#    4. Use Ctrl+Shift+P → "Fold All" to collapse everything, then unfold
#       only the section you're studying
#    5. Each # %% marker creates a runnable cell — click "Run Cell" above it
#    6. Ctrl+K Ctrl+0 folds all, Ctrl+K Ctrl+J unfolds all
#
#  FROM THE TERMINAL:
#    python python_poweruser.py              → Run all demos
#    python python_poweruser.py <section>    → Run one section (e.g. "strings")
#    python python_poweruser.py list         → Show all section names
#    python python_poweruser.py test         → Self-test quiz
#
# ─────────────────────────────────────────────────────────────────────────────
#
#  TABLE OF CONTENTS
#  ─────────────────
#
#  PART 1 — FOUNDATIONS
#    01  Variables & Types         The atoms of Python
#    02  Numbers & Math            Integers, floats, and gotchas
#    03  Strings                   Text manipulation mastery
#    04  Booleans & None           Truth, falsity, and nothingness
#
#  PART 2 — DATA STRUCTURES
#    05  Lists                     Ordered, mutable sequences
#    06  Tuples                    Immutable sequences
#    07  Dictionaries              Key-value lookup tables
#    08  Sets                      Unique collections & set math
#    09  Advanced Structures       namedtuple, dataclass, defaultdict, Counter
#
#  PART 3 — CONTROL FLOW
#    10  Conditionals              if/elif/else, ternary, match/case
#    11  Loops                     for, while, enumerate, zip
#    12  Comprehensions            List, dict, set, generator expressions
#
#  PART 4 — FUNCTIONS
#    13  Function Basics           def, args, kwargs, returns
#    14  Scope & Closures          LEGB rule, nonlocal, closures
#    15  Lambda & Functional       lambda, map, filter, reduce
#    16  Decorators                Wrapping functions for superpowers
#    17  Functools                 lru_cache, partial, wraps
#
#  PART 5 — OBJECT-ORIENTED PROGRAMMING
#    18  Classes                   Blueprints for objects
#    19  Inheritance               Code reuse through hierarchy
#    20  Dunder Methods            __init__, __repr__, __add__, etc.
#    21  Properties & Slots        Controlled attributes, memory savings
#    22  ABCs & Protocols          Interfaces and duck typing
#
#  PART 6 — ERROR HANDLING
#    23  Exceptions                try/except/else/finally
#    24  Context Managers          with statement, custom managers
#    25  Custom Exceptions         Building your own error types
#
#  PART 7 — ITERATORS & GENERATORS
#    26  Iterators                 The protocol behind for loops
#    27  Generators                yield, lazy evaluation, pipelines
#    28  itertools                 The Swiss army knife
#
#  PART 8 — FILE I/O & DATA
#    29  File Operations           read, write, append, pathlib
#    30  JSON & CSV                Data serialization
#    31  Pathlib                   Modern file path handling
#
#  PART 9 — TEXT MASTERY
#    32  Regex                     Pattern matching
#    33  String Formatting         f-strings, alignment, number formats
#    34  Datetime                  Dates, times, timezones
#
#  PART 10 — STANDARD LIBRARY POWER TOOLS
#    35  Collections               deque, OrderedDict, ChainMap
#    36  OS & Subprocess           System interaction
#    37  Typing & Type Hints       Static type annotations
#
#  PART 11 — PYTHONIC PATTERNS (THE EDGE)
#    38  Idioms                    The patterns that separate pros from amateurs
#    39  Performance               When and how to optimize
#    40  Gotchas                   The traps everyone falls into
#
#  PART 12 — REFERENCE TABLES (Ctrl+F heaven)
#    41  Operator Precedence       What binds tighter than what
#    42  Built-in Functions        The 70+ functions you get for free
#    43  Exception Hierarchy       The family tree of errors
#
#  PART 13 — ENVIRONMENT & TOOLING
#    44  Virtual Environments      Isolation, pip, requirements.txt
#    45  Debugging & Profiling     pdb, breakpoint(), cProfile, timeit
#
#  PART 14 — REAL-WORLD RECIPES
#    46  One-Liner Recipes         Copy-paste solutions for daily work
#
#  APPENDIX
#    47  Cheat Sheet               Everything at a glance

#
# ─────────────────────────────────────────────────────────────────────────────

import sys
import os
import re
import inspect
import textwrap
import locale
import argparse

# ── Locale: ensure Unicode box-drawing chars render correctly everywhere ──
try:
    locale.setlocale(locale.LC_ALL, "")
except locale.Error:
    pass  # Hardened environments may block setlocale — that's fine

# ═══════════════════════════════════════════════════════════════════════════════
#  HELPER: Pretty section headers for terminal output
# ═══════════════════════════════════════════════════════════════════════════════

def _header(num, title):
    """Print a clean section header."""
    print(f"\n{'─' * 70}")
    print(f"  {num:02d} │ {title}")
    print(f"{'─' * 70}")


# ═══════════════════════════════════════════════════════════════════════════════
#  TUI — Interactive Terminal User Interface (curses-based)
# ═══════════════════════════════════════════════════════════════════════════════
#
#  This section implements a BTOP-quality interactive TUI using Python's
#  built-in curses library. It provides:
#    • Two-pane main menu (Parts on left, Sections on right)
#    • Source code viewer with syntax highlighting
#    • Keyboard navigation (arrow keys, vim keys, search)
#    • Graceful fallback when curses is unavailable
#
#  All TUI code is self-contained and does not modify any demo functions.
# ═══════════════════════════════════════════════════════════════════════════════

_TUI_VERSION = "3.0"

# Section metadata: maps each section to its part, number, and display title.
# This is built from the table of contents and used by both TUI and CLI.
SECTION_META = [
    # (key, number, title, part_index, part_name)
    ("variables",      1,  "Variables & Types",       0,  "Foundations"),
    ("numbers",        2,  "Numbers & Math",          0,  "Foundations"),
    ("strings",        3,  "Strings",                 0,  "Foundations"),
    ("booleans",       4,  "Booleans & None",         0,  "Foundations"),
    ("lists",          5,  "Lists",                   1,  "Data Structures"),
    ("tuples",         6,  "Tuples",                  1,  "Data Structures"),
    ("dicts",          7,  "Dictionaries",            1,  "Data Structures"),
    ("sets",           8,  "Sets",                    1,  "Data Structures"),
    ("structures",     9,  "Advanced Structures",     1,  "Data Structures"),
    ("conditionals",   10, "Conditionals",            2,  "Control Flow"),
    ("loops",          11, "Loops",                   2,  "Control Flow"),
    ("comprehensions", 12, "Comprehensions",          2,  "Control Flow"),
    ("functions",      13, "Function Basics",         3,  "Functions"),
    ("scope",          14, "Scope & Closures",        3,  "Functions"),
    ("lambda",         15, "Lambda & Functional",     3,  "Functions"),
    ("decorators",     16, "Decorators",              3,  "Functions"),
    ("functools",      17, "Functools",               3,  "Functions"),
    ("classes",        18, "Classes",                 4,  "OOP"),
    ("inheritance",    19, "Inheritance",             4,  "OOP"),
    ("dunders",        20, "Dunder Methods",          4,  "OOP"),
    ("properties",     21, "Properties & Slots",      4,  "OOP"),
    ("abcs",           22, "ABCs & Protocols",        4,  "OOP"),
    ("exceptions",     23, "Exceptions",              5,  "Error Handling"),
    ("context",        24, "Context Managers",         5,  "Error Handling"),
    ("custom_errors",  25, "Custom Exceptions",       5,  "Error Handling"),
    ("iterators",      26, "Iterators",               6,  "Iterators & Gen."),
    ("generators",     27, "Generators",              6,  "Iterators & Gen."),
    ("itertools",      28, "itertools",               6,  "Iterators & Gen."),
    ("files",          29, "File Operations",         7,  "File I/O"),
    ("json_csv",       30, "JSON & CSV",              7,  "File I/O"),
    ("pathlib",        31, "Pathlib",                 7,  "File I/O"),
    ("regex",          32, "Regex",                   8,  "Text Mastery"),
    ("formatting",     33, "String Formatting",       8,  "Text Mastery"),
    ("datetime",       34, "Datetime",                8,  "Text Mastery"),
    ("collections",    35, "Collections",             9,  "Stdlib Tools"),
    ("os",             36, "OS & Subprocess",         9,  "Stdlib Tools"),
    ("typing",         37, "Typing & Type Hints",     9,  "Stdlib Tools"),
    ("idioms",         38, "Idioms",                  10, "The Edge"),
    ("performance",    39, "Performance",             10, "The Edge"),
    ("gotchas",        40, "Gotchas",                 10, "The Edge"),
    ("precedence",     41, "Operator Precedence",     11, "Reference Tables"),
    ("builtins",       42, "Built-in Functions",      11, "Reference Tables"),
    ("exceptions_ref", 43, "Exception Hierarchy",     11, "Reference Tables"),
    ("venv",           44, "Virtual Environments",    12, "Env & Tooling"),
    ("debugging",      45, "Debugging & Profiling",   12, "Env & Tooling"),
    ("recipes",        46, "One-Liner Recipes",       13, "Recipes"),
    ("cheatsheet",     47, "Cheat Sheet",             14, "Appendix"),
]

PARTS_LIST = [
    (1,  "Foundations"),
    (2,  "Data Structures"),
    (3,  "Control Flow"),
    (4,  "Functions"),
    (5,  "OOP"),
    (6,  "Error Handling"),
    (7,  "Iterators & Gen."),
    (8,  "File I/O"),
    (9,  "Text Mastery"),
    (10, "Stdlib Tools"),
    (11, "The Edge"),
    (12, "Reference Tables"),
    (13, "Env & Tooling"),
    (14, "Recipes"),
    (15, "Appendix"),
]


def _get_sections_for_part(part_index):
    """Return section metadata entries for a given part index."""
    return [s for s in SECTION_META if s[3] == part_index]


# ─────────────────────────────────────────────────────────────────────────────
#  CLI: Fault-tolerant argparse parser & non-interactive commands
# ─────────────────────────────────────────────────────────────────────────────
#
#  WHY A SUBCLASS?  Stock argparse calls sys.exit(2) on ANY parse error —
#  unknown flags, missing args, mutual exclusion violations.  That hard exit
#  bypasses our __main__ try/except for KeyboardInterrupt and BrokenPipeError,
#  dumps a cryptic error to stderr (invisible when piping stdout), and exits
#  with code 2 instead of 0.  In other words, it's the opposite of fault-
#  tolerant.
#
#  The fix: override error() and exit() so they NEVER call sys.exit().
#  Instead, print a friendly message to stdout and raise _ParseError, which
#  _parse_args_and_run() catches for a graceful return.  We keep everything
#  argparse does well — structured flag definitions, --version, auto-help,
#  mutually exclusive groups — while eliminating its one fatal flaw.
# ─────────────────────────────────────────────────────────────────────────────


class _ParseError(Exception):
    """Raised by FaultTolerantParser instead of calling sys.exit()."""
    pass


class _FaultTolerantParser(argparse.ArgumentParser):
    """ArgumentParser subclass that never calls sys.exit().

    Stock argparse's error handling model:
      bad input → write to stderr → sys.exit(2)  💀

    Our model:
      bad input → friendly message to stdout → raise _ParseError  ✓

    This keeps us inside the Python exception hierarchy where our
    fault-tolerant wrappers (__main__, TUI, etc.) can handle things
    gracefully.
    """

    def error(self, message):
        """Override: print friendly message + suggestions instead of dying."""
        # ── Parse the error to give contextual help ──
        # argparse passes messages like:
        #   "unrecognized arguments: --bogus"
        #   "argument -s/--section: expected one argument"
        #   "argument -l/--list: not allowed with argument -t/--test"
        print(f"\n  Oops: {message}")
        print(f"  Try:  python {self.prog} --help")

        # ── Extra help for common mistakes ──
        if "unrecognized arguments" in message:
            # Extract the bogus flag and fuzzy-match against known flags
            bad = message.split(":", 1)[-1].strip().split()[0]
            known = [a.option_strings[0] for a in self._actions
                     if a.option_strings]
            from difflib import get_close_matches
            close = get_close_matches(bad, known, n=2, cutoff=0.4)
            if close:
                print(f"  Did you mean: {', '.join(close)}?")
        elif "expected one argument" in message:
            print("  (That flag needs a value — e.g. -s strings)")
        elif "not allowed with" in message:
            print("  (Those flags can't be combined — pick one action at a time)")
        print()  # breathing room
        raise _ParseError(message)

    def exit(self, status=0, message=None):
        """Override: --version and --help print then raise instead of exiting."""
        # --version and --help call self.exit(0) after printing.
        # We've already printed; just raise so we return to caller.
        if message:
            print(message, end="")
        raise _ParseError(message or "")


def _build_parser():
    """Build the fault-tolerant argparse parser with all flags and help text.

    Uses RawDescriptionHelpFormatter so the epilog (TUI nav keys,
    examples) renders exactly as written — no line-wrapping.
    """
    epilog = textwrap.dedent(f"""\
    TUI navigation (when running interactively):
      ↑/↓  or  j/k        Navigate sections
      Enter  or  →         Open section
      Esc  or  ←  or  q    Back to menu
      /                    Search
      r                    Run current section's demo
      t                    Self-test quiz
      q                    Quit (from main menu)
      ?                    Show help overlay
      1-9                  Jump to Part 1-9
      Tab                  Toggle parts/sections pane
      PgUp/PgDn            Scroll viewer
      Home/End             Jump to top/bottom

    examples:
      python python_poweruser.py                Launch interactive TUI
      python python_poweruser.py -s regex       Run the regex section
      python python_poweruser.py -f decorator   Find sections about decorators
      python python_poweruser.py -t             Take the self-test quiz
      python python_poweruser.py strings        Run a section by name (shorthand)
    """)

    parser = _FaultTolerantParser(
        prog="python_poweruser.py",
        description=(
            "PYTHON POWER USER — Interactive Python Reference & Learning Tool\n"
            f"v{_TUI_VERSION} | {len(SECTION_META)} sections | "
            f"{len(PARTS_LIST)} parts"
        ),
        epilog=epilog,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    # ── Mutually exclusive primary actions ──
    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        "-l", "--list",
        action="store_true",
        help="list all sections organized by part",
    )
    group.add_argument(
        "-s", "--section",
        metavar="NAME",
        help="run a specific section by key (e.g. -s strings)",
    )
    group.add_argument(
        "-r", "--run",
        action="store_true",
        help="run all demos sequentially (non-interactive)",
    )
    group.add_argument(
        "-t", "--test",
        action="store_true",
        help="run the 20-question self-test quiz",
    )
    group.add_argument(
        "-f", "--find",
        metavar="TERM",
        help="search section names and content for TERM",
    )

    # ── Modifiers ──
    parser.add_argument(
        "--no-tui",
        action="store_true",
        help="skip the interactive TUI, use print-based output",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"Python Power User v{_TUI_VERSION} — "
                f"{len(SECTION_META)} sections, {len(PARTS_LIST)} parts",
    )

    # ── Positional: bare section name for backward compat ──
    parser.add_argument(
        "section_name",
        nargs="?",
        default=None,
        help=argparse.SUPPRESS,  # Hidden — the -s flag is the documented way
    )

    return parser


def _cli_list():
    """Pretty-print all sections organized by part."""
    print(f"\n{'─' * 60}")
    print(f"  PYTHON POWER USER — All {len(SECTION_META)} Sections")
    print(f"{'─' * 60}\n")
    current_part = -1
    for key, num, title, part_idx, part_name in SECTION_META:
        if part_idx != current_part:
            if current_part >= 0:
                print()
            p = part_idx + 1 if part_idx < 14 else "A"
            print(f"  PART {p} — {part_name}")
            current_part = part_idx
        print(f"    {num:02d}  {title:<28s} [{key}]")
    print(f"\n{'─' * 60}")
    print(f"  Use: python python_poweruser.py -s <key>  to run one section")
    print(f"{'─' * 60}\n")


def _cli_find(term):
    """Search section names/content for a keyword."""
    term_lower = term.lower()
    hits = []
    for key, num, title, part_idx, part_name in SECTION_META:
        # Search in key and title
        if term_lower in key.lower() or term_lower in title.lower():
            hits.append((key, num, title, part_name, "name match"))
            continue
        # Search in function source if available
        # NOTE: DEMO_REGISTRY is defined later in the file but is available
        # at call-time because this function is only called from __main__.
        try:
            reg = DEMO_REGISTRY
        except NameError:
            reg = {}
        if key in reg:
            try:
                src = inspect.getsource(reg[key])
                if term_lower in src.lower():
                    hits.append((key, num, title, part_name, "content match"))
            except (OSError, TypeError):
                pass
    if not hits:
        print(f"  No sections found matching '{term}'.")
        return
    print(f"\n  Found {len(hits)} section(s) matching '{term}':\n")
    for key, num, title, part_name, match_type in hits:
        print(f"    {num:02d}  {title:<28s} [{key}]  ({match_type})")
    print(f"\n  Use: python python_poweruser.py -s <key>  to run one\n")


# ─────────────────────────────────────────────────────────────────────────────
#  TUI: Curses-based interactive terminal interface
# ─────────────────────────────────────────────────────────────────────────────

def _can_use_curses():
    """Check if we can use the curses TUI.

    Checks (in order): TTY, TERM, curses import, Windows auto-install.
    Any failure → False → graceful fallback to CLI mode.
    """
    # Gate 1: Not interactive if piped or redirected
    try:
        if not sys.stdout.isatty() or not sys.stdin.isatty():
            return False
    except Exception:
        return False  # isatty() itself can fail in exotic environments

    # Gate 2: Dumb terminals can't do curses
    term = os.environ.get("TERM", "")
    if term in ("dumb", "unknown", ""):
        # Empty TERM is common in CI/Docker — still try, but guard later
        if term in ("dumb",):
            return False

    # Gate 3: Try importing curses
    try:
        import curses  # noqa: F811
        return True
    except ImportError:
        pass

    # Gate 4: Windows — attempt one-shot install of windows-curses
    if sys.platform == "win32":
        try:
            import subprocess
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "--user",
                 "--quiet", "windows-curses"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=30,  # Don't hang on corporate proxies
            )
            import curses  # noqa: F811
            return True
        except Exception:
            return False

    return False


def _syntax_highlight_tokens(line):
    """Parse a line of Python into (text, color_name) tokens for curses rendering.

    Returns a list of (text, style) tuples where style is one of:
    'keyword', 'string', 'comment', 'number', 'decorator', 'builtin',
    'funcname', 'normal'.
    """
    tokens = []
    if not line:
        return [("", "normal")]

    KEYWORDS = {
        'def', 'class', 'if', 'elif', 'else', 'for', 'while', 'return',
        'import', 'from', 'try', 'except', 'with', 'as', 'yield', 'lambda',
        'True', 'False', 'None', 'and', 'or', 'not', 'in', 'is', 'raise',
        'pass', 'break', 'continue', 'match', 'case', 'global', 'nonlocal',
        'del', 'assert', 'finally', 'async', 'await',
    }
    BUILTINS = {
        'print', 'len', 'range', 'type', 'isinstance', 'enumerate', 'zip',
        'map', 'filter', 'sorted', 'reversed', 'list', 'dict', 'set',
        'tuple', 'str', 'int', 'float', 'bool', 'sum', 'min', 'max',
        'abs', 'round', 'open', 'hasattr', 'getattr', 'setattr', 'super',
        'property', 'staticmethod', 'classmethod', 'any', 'all', 'iter',
        'next', 'repr', 'hash', 'id', 'input', 'vars', 'dir', 'help',
        'callable', 'issubclass', 'object', 'format',
    }

    # Pattern for tokenizing Python source lines
    # Order matters — earlier patterns take priority
    token_pattern = re.compile(
        r'(?P<comment>#.*$)'                         # Comments
        r'|(?P<tripdq>"""[\s\S]*?""")'               # Triple double-quoted
        r'|(?P<tripsq>\'\'\'[\s\S]*?\'\'\')'         # Triple single-quoted
        r"|(?P<fstring>f['\"](?:[^'\"\\]|\\.)*['\"])" # f-strings
        r"|(?P<string>['\"](?:[^'\"\\]|\\.)*['\"])"   # Regular strings
        r'|(?P<decorator>@\w+(?:\.\w+)*)'             # Decorators
        r'|(?P<number>\b\d+\.?\d*(?:e[+-]?\d+)?\b)'  # Numbers
        r'|(?P<word>\b\w+\b)'                         # Words (keywords, builtins, etc.)
        r'|(?P<other>\S+)'                            # Anything else
        r'|(?P<space>\s+)'                            # Whitespace
    )

    prev_word = ""
    for m in token_pattern.finditer(line):
        text = m.group()
        if m.group("comment"):
            # Better Comments markers: #* #! #? get bright yellow
            tokens.append((text, "comment"))
        elif m.group("tripdq") or m.group("tripsq"):
            tokens.append((text, "string"))
        elif m.group("fstring"):
            tokens.append((text, "string"))
        elif m.group("string"):
            tokens.append((text, "string"))
        elif m.group("decorator"):
            tokens.append((text, "decorator"))
        elif m.group("number"):
            tokens.append((text, "number"))
        elif m.group("word"):
            if text in KEYWORDS:
                tokens.append((text, "keyword"))
                prev_word = text
            elif text in BUILTINS:
                tokens.append((text, "builtin"))
                prev_word = text
            elif prev_word in ("def", "class"):
                tokens.append((text, "funcname"))
                prev_word = text
            else:
                tokens.append((text, "normal"))
                prev_word = text
        elif m.group("space"):
            tokens.append((text, "normal"))
        else:
            tokens.append((text, "normal"))

    return tokens if tokens else [("", "normal")]




class PowerUserTUI:
    """Minimal, elegant interactive TUI for Python Power User.

    Design philosophy: less is more.  Clean dividers instead of nested boxes,
    Monokai-inspired color palette, generous whitespace, ASCII-safe layout.
    """

    # -- Color pair IDs (Monokai-inspired, restrained palette) --
    C_NORMAL     = 0   # Default terminal fg/bg
    C_TITLE      = 1   # Title bar (reverse video)
    C_ACCENT     = 2   # Headings, active labels (Monokai green)
    C_COMMENT    = 4   # Comments (subdued gray)
    C_KEYWORD    = 5   # Keywords (Monokai pink/red)
    C_STRING     = 6   # Strings (Monokai yellow)
    C_NUMBER     = 7   # Numbers (Monokai purple)
    C_SELECTED   = 8   # Selection highlight (reverse video)
    C_STATUS     = 9   # Status bar (reverse video, same as title)
    C_DECORATOR  = 10  # Decorators (Monokai green)
    C_BUILTIN    = 11  # Built-in functions (Monokai cyan/blue)
    C_FUNCNAME   = 12  # Function names after def/class (bold green)
    C_DIM        = 13  # Gutters, borders, muted text

    def __init__(self, stdscr, registry):
        import curses
        self.curses = curses
        self.stdscr = stdscr
        self.registry = registry

        # State
        self.screen = "menu"    # 'menu', 'viewer', 'search', 'help'
        self.pane = "parts"     # 'parts' or 'sections'
        self.part_idx = 0
        self.sec_idx = 0
        self.scroll_offset = 0
        self.search_query = ""
        self.search_results = []
        self.search_sel = 0
        self.viewer_lines = []

        # Terminal dimensions
        self.h, self.w = stdscr.getmaxyx()

        self._init_colors()
        self.stdscr.timeout(100)
        try:
            curses.curs_set(0)
        except Exception:
            pass

    def _init_colors(self):
        """Initialize Monokai-inspired color pairs.

        Monokai classic (restrained):
          pink/red  = keywords           green  = funcs/decorators
          yellow    = strings            purple = numbers
          cyan      = builtins           gray   = comments/dim

        We use only what helps comprehension; everything else stays default.
        """
        curses = self.curses
        try:
            curses.start_color()
            curses.use_default_colors()
        except Exception:
            return

        def _pair(pid, fg, bg=-1):
            try:
                curses.init_pair(pid, fg, bg)
            except Exception:
                pass

        # -- Monokai palette mapped to 8-color curses --
        #  Monokai pink   -> RED        (keywords: def, if, return ...)
        #  Monokai yellow -> YELLOW     (strings)
        #  Monokai green  -> GREEN      (function names, decorators)
        #  Monokai purple -> MAGENTA    (numbers)
        #  Monokai blue   -> CYAN       (builtins: print, len, range ...)
        #  Monokai gray   -> WHITE+DIM  (comments, gutters, borders)
        _pair(self.C_TITLE,     curses.COLOR_BLACK,   curses.COLOR_WHITE)
        _pair(self.C_ACCENT,    curses.COLOR_GREEN,   -1)
        _pair(self.C_COMMENT,   curses.COLOR_WHITE,   -1)  # rendered with A_DIM
        _pair(self.C_KEYWORD,   curses.COLOR_RED,     -1)
        _pair(self.C_STRING,    curses.COLOR_YELLOW,  -1)
        _pair(self.C_NUMBER,    curses.COLOR_MAGENTA, -1)
        _pair(self.C_SELECTED,  curses.COLOR_BLACK,   curses.COLOR_GREEN)
        _pair(self.C_STATUS,    curses.COLOR_BLACK,   curses.COLOR_WHITE)
        _pair(self.C_DECORATOR, curses.COLOR_GREEN,   -1)
        _pair(self.C_BUILTIN,   curses.COLOR_CYAN,    -1)
        _pair(self.C_FUNCNAME,  curses.COLOR_GREEN,   -1)
        _pair(self.C_DIM,       curses.COLOR_WHITE,   -1)  # rendered with A_DIM

    def _attr(self, color_id, bold=False, dim=False):
        """Get curses attribute for a color pair."""
        a = self.curses.color_pair(color_id)
        if bold:
            a |= self.curses.A_BOLD
        if dim:
            a |= self.curses.A_DIM
        return a

    def _dim(self):
        """Shorthand for dim gray text (borders, gutters, muted info)."""
        return self._attr(self.C_DIM, dim=True)

    def _style_attr(self, style_name):
        """Map syntax highlight style names to curses attributes."""
        mapping = {
            "keyword":   (self.C_KEYWORD,   True,  False),
            "string":    (self.C_STRING,    False, False),
            "comment":   (self.C_COMMENT,   False, True),
            "number":    (self.C_NUMBER,    False, False),
            "decorator": (self.C_DECORATOR, True,  False),
            "builtin":   (self.C_BUILTIN,   False, False),
            "funcname":  (self.C_FUNCNAME,  True,  False),
            "normal":    (self.C_NORMAL,    False, False),
        }
        cid, bold, dim = mapping.get(style_name, (self.C_NORMAL, False, False))
        return self._attr(cid, bold=bold, dim=dim)

    # -- Drawing primitives --

    def _safe_addstr(self, y, x, text, attr=None):
        """Write text to screen, clipping to terminal boundaries.

        Fault-tolerant: handles Unicode encoding errors, multi-byte
        clipping, out-of-bounds writes, and the classic bottom-right
        corner curses.error.  Never raises.
        """
        if y < 0 or y >= self.h or x >= self.w:
            return
        max_len = self.w - x
        if max_len <= 0:
            return
        text = text[:max_len]
        try:
            if attr is not None:
                self.stdscr.addstr(y, x, text, attr)
            else:
                self.stdscr.addstr(y, x, text)
        except self.curses.error:
            pass
        except UnicodeEncodeError:
            safe = text.encode("ascii", errors="replace").decode("ascii")
            try:
                if attr is not None:
                    self.stdscr.addstr(y, x, safe[:max_len], attr)
                else:
                    self.stdscr.addstr(y, x, safe[:max_len])
            except self.curses.error:
                pass
        except Exception:
            pass

    def _hline(self, y, x1=0, x2=None, char="-"):
        """Draw a horizontal line using plain ASCII dashes."""
        if x2 is None:
            x2 = self.w
        length = min(x2, self.w) - x1
        if length > 0:
            self._safe_addstr(y, x1, char * length, self._dim())

    def _fill_line(self, y, attr, x_start=0, x_end=None):
        """Fill a screen line with spaces using given attribute."""
        if x_end is None:
            x_end = self.w
        self._safe_addstr(y, x_start, " " * (x_end - x_start), attr)

    # -- Title bar and status bar --

    def _draw_title_bar(self):
        """Draw a clean, minimal title bar."""
        attr = self._attr(self.C_TITLE)
        self._fill_line(0, attr)
        self._safe_addstr(0, 1, " PYTHON POWER USER", self._attr(self.C_TITLE, bold=True))
        ver = f"v{_TUI_VERSION} "
        if self.w > 40:
            self._safe_addstr(0, self.w - len(ver), ver, attr)

    def _draw_status_bar(self, text=""):
        """Draw the bottom status bar."""
        y = self.h - 1
        attr = self._attr(self.C_STATUS)
        self._fill_line(y, attr)
        if not text:
            if self.screen == "menu":
                text = " j/k:Nav  Enter:Open  /:Search  t:Test  ?:Help  q:Quit"
            elif self.screen == "viewer":
                text = " j/k:Scroll  PgUp/PgDn  r:Run  Esc:Back"
            elif self.screen == "search":
                text = " Type to search  Enter:Go  Esc:Cancel"
        self._safe_addstr(y, 0, text[:self.w], attr)

    # -- Main Menu Screen --

    def _draw_menu(self):
        """Draw the main menu."""
        self.stdscr.erase()
        self._draw_title_bar()

        content_y = 2   # row after title bar + 1 blank line
        content_h = self.h - 3  # room for title bar, gap, status bar
        narrow = self.w < 72

        if narrow:
            self._draw_menu_narrow(content_y, content_h)
        else:
            self._draw_menu_wide(content_y, content_h)

        self._draw_status_bar()
        self.stdscr.noutrefresh()
        self.curses.doupdate()

    def _draw_menu_wide(self, start_y, avail_h):
        """Two-column layout: parts | sections.  Divided by a single pipe.

        Every row in both columns is padded to a fixed width so the
        divider pipe draws a perfectly straight vertical line.
        """
        # Column widths
        parts_w = min(max(self.w // 3, 24), 32)
        divider_x = parts_w + 1
        sec_x = divider_x + 2
        sec_col_w = self.w - sec_x - 1

        # Column headers  (padded to fill their column)
        self._safe_addstr(start_y, 1,
                         ("  PARTS").ljust(parts_w),
                         self._attr(self.C_ACCENT, bold=True))
        self._safe_addstr(start_y, sec_x,
                         ("  SECTIONS").ljust(sec_col_w),
                         self._attr(self.C_ACCENT, bold=True))

        # Thin divider between columns -- full height, simple pipe
        for row in range(start_y, start_y + avail_h):
            self._safe_addstr(row, divider_x, "|", self._dim())

        # Parts list -- every row padded to parts_w so the pipe stays straight
        list_y = start_y + 1
        max_visible = avail_h - 1
        active = self.pane == "parts"
        for i, (pnum, pname) in enumerate(PARTS_LIST):
            if i >= max_visible:
                break
            y = list_y + i
            label_num = f"{pnum:>2d}" if pnum <= 14 else " A"
            raw = f"{label_num}  {pname}"
            raw = raw[:parts_w - 4]  # room for " > " prefix

            if i == self.part_idx and active:
                row_text = f" > {raw}".ljust(parts_w)
                self._safe_addstr(y, 1, row_text,
                                 self._attr(self.C_SELECTED, bold=True))
            elif i == self.part_idx:
                row_text = f"   {raw}".ljust(parts_w)
                self._safe_addstr(y, 1, row_text,
                                 self._attr(self.C_ACCENT))
            else:
                row_text = f"   {raw}".ljust(parts_w)
                self._safe_addstr(y, 1, row_text,
                                 self._attr(self.C_NORMAL))

        # Blank-fill any remaining rows below the parts list
        for y in range(list_y + len(PARTS_LIST), start_y + avail_h):
            if y >= self.h - 1:
                break
            self._safe_addstr(y, 1, " " * parts_w, self._attr(self.C_NORMAL))

        # Sections list -- every row padded to sec_col_w
        sections = _get_sections_for_part(self.part_idx)
        list_y = start_y + 1
        max_visible = avail_h - 1
        active = self.pane == "sections"
        for i, (key, num, title, _, _) in enumerate(sections):
            if i >= max_visible:
                break
            y = list_y + i
            raw = f"{num:02d}  {title}"
            raw = raw[:sec_col_w - 4]  # room for " > " prefix

            if i == self.sec_idx and active:
                row_text = f" > {raw}".ljust(sec_col_w)
                self._safe_addstr(y, sec_x, row_text,
                                 self._attr(self.C_SELECTED, bold=True))
            elif i == self.sec_idx:
                row_text = f"   {raw}".ljust(sec_col_w)
                self._safe_addstr(y, sec_x, row_text,
                                 self._attr(self.C_ACCENT))
            else:
                row_text = f"   {raw}".ljust(sec_col_w)
                self._safe_addstr(y, sec_x, row_text,
                                 self._attr(self.C_NORMAL))

    def _draw_menu_narrow(self, start_y, avail_h):
        """Single-column layout for narrow terminals."""
        list_y = start_y
        max_visible = avail_h
        inner_w = self.w - 2

        if self.pane == "parts":
            self._safe_addstr(list_y, 2, "PARTS",
                             self._attr(self.C_ACCENT, bold=True))
            self._safe_addstr(list_y, 8, "  (Tab -> sections)", self._dim())
            list_y += 1
            for i, (pnum, pname) in enumerate(PARTS_LIST):
                if i >= max_visible - 1:
                    break
                y = list_y + i
                label_num = f"{pnum:>2d}" if pnum <= 14 else " A"
                label = f"{label_num}  {pname}"
                if i == self.part_idx:
                    attr = self._attr(self.C_SELECTED, bold=True)
                    self._safe_addstr(y, 1, " " * inner_w, attr)
                    self._safe_addstr(y, 1, f" > {label}", attr)
                else:
                    self._safe_addstr(y, 1, f"   {label}",
                                     self._attr(self.C_NORMAL))
        else:
            pname = PARTS_LIST[self.part_idx][1] if self.part_idx < len(PARTS_LIST) else "?"
            self._safe_addstr(list_y, 2, pname,
                             self._attr(self.C_ACCENT, bold=True))
            self._safe_addstr(list_y, 2 + len(pname), "  (Tab -> parts)",
                             self._dim())
            list_y += 1
            sections = _get_sections_for_part(self.part_idx)
            for i, (key, num, title, _, _) in enumerate(sections):
                if i >= max_visible - 1:
                    break
                y = list_y + i
                label = f"{num:02d}  {title}"
                label = label[:inner_w - 4]
                if i == self.sec_idx:
                    attr = self._attr(self.C_SELECTED, bold=True)
                    self._safe_addstr(y, 1, " " * inner_w, attr)
                    self._safe_addstr(y, 1, f" > {label}", attr)
                else:
                    self._safe_addstr(y, 1, f"   {label}",
                                     self._attr(self.C_NORMAL))

    # -- Section Viewer Screen --

    def _prepare_viewer(self, sec_key):
        """Prepare the viewer lines for a section.

        Fault-tolerant: if source can't be read (frozen exe, .pyc-only,
        inspect failure), shows a helpful fallback instead of crashing.
        Regex tokenizer failures on individual lines are caught per-line.
        """
        self.viewer_lines = []
        self.scroll_offset = 0

        if sec_key not in self.registry:
            self.viewer_lines = [[("Section not found", "normal")]]
            return

        func = self.registry[sec_key]

        def _safe_tokenize(line):
            try:
                return _syntax_highlight_tokens(line)
            except Exception:
                return [(line, "normal")]

        # Docstring first (teaching content)
        try:
            doc = func.__doc__
        except Exception:
            doc = None
        if doc:
            for line in doc.split("\n"):
                self.viewer_lines.append(_safe_tokenize(line))
            self.viewer_lines.append(_safe_tokenize(""))
            self.viewer_lines.append(
                _safe_tokenize("# " + "-" * 60)
            )
            self.viewer_lines.append(_safe_tokenize(""))

        # Source code
        try:
            src = inspect.getsource(func)
            src = textwrap.dedent(src)
            for line in src.split("\n"):
                self.viewer_lines.append(_safe_tokenize(line))
        except (OSError, TypeError):
            self.viewer_lines.append(
                [("(Source not available -- running from .pyc or frozen)", "comment")]
            )
        except Exception:
            self.viewer_lines.append(
                [("(Could not read source code)", "comment")]
            )

    def _draw_viewer(self):
        """Draw the section source viewer with syntax highlighting."""
        self.stdscr.erase()
        self._draw_title_bar()

        # Section info
        sections = _get_sections_for_part(self.part_idx)
        if self.sec_idx < len(sections):
            sec_key, sec_num, sec_title, _, _ = sections[self.sec_idx]
        else:
            sec_key, sec_num, sec_title = "?", 0, "?"

        # Section title
        self._safe_addstr(1, 2, f"{sec_num:02d}  {sec_title}",
                         self._attr(self.C_ACCENT, bold=True))
        self._hline(2)

        # Code area
        code_y = 3
        code_h = self.h - 5
        total_lines = len(self.viewer_lines)

        # Clamp scroll
        max_scroll = max(0, total_lines - code_h)
        self.scroll_offset = max(0, min(self.scroll_offset, max_scroll))

        # Render visible lines
        gutter_w = 8  # " 1234 | " = 8 chars, all single-width ASCII
        for i in range(code_h):
            line_idx = self.scroll_offset + i
            y = code_y + i
            if line_idx >= total_lines:
                break
            # Line number gutter (ASCII only: digits + space + pipe)
            gutter = f" {line_idx + 1:>4d} | "
            self._safe_addstr(y, 0, gutter, self._dim())
            # Syntax-highlighted tokens
            x = gutter_w
            for text, style in self.viewer_lines[line_idx]:
                self._safe_addstr(y, x, text, self._style_attr(style))
                x += len(text)

        # Scroll indicator
        sep_y = self.h - 2
        self._hline(sep_y)
        if total_lines > code_h:
            pct = int(100 * self.scroll_offset / max(1, max_scroll))
            info = f" {self.scroll_offset + 1}/{total_lines} ({pct}%)"
        else:
            info = f" {total_lines} lines"
        self._safe_addstr(sep_y, 1, info, self._dim())

        self._draw_status_bar()
        self.stdscr.noutrefresh()
        self.curses.doupdate()

    # -- Search Screen --

    def _draw_search(self):
        """Draw search input and results."""
        self.stdscr.erase()
        self._draw_title_bar()

        # Search prompt
        self._safe_addstr(2, 2, "/", self._attr(self.C_ACCENT, bold=True))
        self._safe_addstr(2, 3, self.search_query, self._attr(self.C_NORMAL))
        cursor_x = 3 + len(self.search_query)
        self._safe_addstr(2, cursor_x, "_", self._attr(self.C_ACCENT))
        self._hline(3)

        # Filter sections
        self.search_results = []
        q = self.search_query.lower()
        if q:
            for key, num, title, pidx, pname in SECTION_META:
                if q in key.lower() or q in title.lower() or q in pname.lower():
                    self.search_results.append((key, num, title, pidx, pname))
        else:
            self.search_results = list(SECTION_META)

        if self.search_results:
            self.search_sel = max(0, min(self.search_sel, len(self.search_results) - 1))

        # Draw results
        max_visible = self.h - 6
        for i, (key, num, title, pidx, pname) in enumerate(self.search_results):
            if i >= max_visible:
                break
            y = 4 + i
            label = f"{num:02d}  {title}"
            label = label[:self.w - 6]
            if i == self.search_sel:
                attr = self._attr(self.C_SELECTED, bold=True)
                self._safe_addstr(y, 1, " " * (self.w - 2), attr)
                self._safe_addstr(y, 1, f" > {label}", attr)
            else:
                self._safe_addstr(y, 1, f"   {label}",
                                 self._attr(self.C_NORMAL))

        # Match count
        self._safe_addstr(self.h - 2, 2,
                         f"{len(self.search_results)} matches", self._dim())

        self._draw_status_bar()
        self.stdscr.noutrefresh()
        self.curses.doupdate()

    # -- Help Overlay --

    def _draw_help(self):
        """Draw a centered, minimal help overlay."""
        lines = [
            "",
            "  KEYS",
            "  " + "-" * 32,
            "",
            "  j/k  Up/Down      Navigate",
            "  Enter  or  >      Open section",
            "  Esc  or  <        Back",
            "  Tab               Switch pane",
            "",
            "  /                 Search",
            "  r                 Run demo",
            "  t                 Self-test",
            "  q                 Quit",
            "",
            "  PgUp/PgDn         Scroll",
            "  Home/End          Top/bottom",
            "  1-9               Jump to part",
            "",
            "  Press any key to close",
            "",
        ]
        box_w = 38
        box_h = len(lines) + 2
        sy = max(0, (self.h - box_h) // 2)
        sx = max(0, (self.w - box_w) // 2)

        # Fill background
        for i in range(box_h):
            self._fill_line(sy + i, self._attr(self.C_NORMAL), sx, sx + box_w)

        # Simple ASCII border
        top    = "+" + "-" * (box_w - 2) + "+"
        bottom = "+" + "-" * (box_w - 2) + "+"
        self._safe_addstr(sy, sx, top, self._dim())
        self._safe_addstr(sy + box_h - 1, sx, bottom, self._dim())
        for i in range(1, box_h - 1):
            self._safe_addstr(sy + i, sx, "|", self._dim())
            self._safe_addstr(sy + i, sx + box_w - 1, "|", self._dim())

        for i, line in enumerate(lines):
            self._safe_addstr(sy + 1 + i, sx + 1,
                             line[:box_w - 2], self._attr(self.C_NORMAL))

        self.stdscr.noutrefresh()
        self.curses.doupdate()


    # ── Curses suspend / restore ──

    def _suspend_curses(self):
        """Cleanly exit curses mode for raw terminal output."""
        try:
            self.curses.endwin()
        except Exception:
            pass

    def _restore_curses(self):
        """Restore curses after raw terminal output.

        Fault-tolerant: if any step fails, keep going —
        a partially restored TUI is better than a dead one.
        """
        curses = self.curses
        try:
            self.stdscr = curses.initscr()
        except Exception:
            return  # Can't recover — event loop will handle it
        try:
            curses.noecho()
        except Exception:
            pass
        try:
            curses.cbreak()
        except Exception:
            pass
        try:
            self.stdscr.keypad(True)
        except Exception:
            pass
        try:
            curses.start_color()
            curses.use_default_colors()
        except Exception:
            pass
        try:
            curses.curs_set(0)
        except Exception:
            pass
        try:
            self.stdscr.timeout(100)
            self.h, self.w = self.stdscr.getmaxyx()
        except Exception:
            pass

    # ── Run a demo ──

    def _run_demo(self, sec_key):
        """Exit curses, run a demo function, return to TUI."""
        if sec_key not in self.registry:
            return
        self._suspend_curses()
        print()
        try:
            self.registry[sec_key]()
        except KeyboardInterrupt:
            print("\n  [Interrupted]")
        except Exception as e:
            print(f"\n  [ERROR]: {e}")
        print(f"\n{'─' * 50}")
        print("  Press Enter to return to TUI...")
        try:
            input()
        except (EOFError, KeyboardInterrupt):
            pass
        self._restore_curses()

    # ── Event loop ──

    def run(self):
        """Main event loop.

        Fault-tolerant: any drawing/input exception is caught and
        the loop continues. Only explicit quit (q) or KeyboardInterrupt
        exits. The terminal is always left in a good state.
        """
        # Reduce escape key delay (default 1000ms → 50ms)
        try:
            self.curses.set_escdelay(50)
        except (AttributeError, self.curses.error):
            pass  # Not available on all builds

        while True:
            try:
                self.h, self.w = self.stdscr.getmaxyx()

                # Minimum terminal size check
                if self.h < 10 or self.w < 40:
                    self.stdscr.erase()
                    msg = "Terminal too small"
                    hint = f"Need 40x10, got {self.w}x{self.h}"
                    self._safe_addstr(self.h // 2, max(0, (self.w - len(msg)) // 2),
                                     msg, self._attr(self.C_KEYWORD, bold=True))
                    self._safe_addstr(self.h // 2 + 1, max(0, (self.w - len(hint)) // 2),
                                     hint, self._attr(self.C_DIM))
                    self.stdscr.noutrefresh()
                    self.curses.doupdate()
                    key = self.stdscr.getch()
                    if key == ord('q'):
                        return
                    continue

                # Draw current screen
                if self.screen == "menu":
                    self._draw_menu()
                elif self.screen == "viewer":
                    self._draw_viewer()
                elif self.screen == "search":
                    self._draw_search()

                # Get input
                key = self.stdscr.getch()
                if key == -1 or key == self.curses.ERR:
                    continue  # Timeout, no input
                if key == self.curses.KEY_RESIZE:
                    self.h, self.w = self.stdscr.getmaxyx()
                    continue

                # Handle help overlay (any screen)
                if key == ord('?') and self.screen != "search":
                    self._draw_help()
                    self.stdscr.getch()  # Wait for any key
                    continue

                # Route to screen-specific handler
                if self.screen == "menu":
                    if self._handle_menu_key(key):
                        return  # Quit
                elif self.screen == "viewer":
                    self._handle_viewer_key(key)
                elif self.screen == "search":
                    self._handle_search_key(key)

            except KeyboardInterrupt:
                return  # Clean exit on Ctrl+C
            except Exception:
                # Drawing glitch, resize race, curses hiccup — soldier on
                try:
                    self.stdscr.clear()
                except Exception:
                    pass
                continue

    def _handle_menu_key(self, key):
        """Handle key press on main menu. Returns True to quit."""
        curses = self.curses
        sections = _get_sections_for_part(self.part_idx)

        # Quit
        if key == ord('q') or key == ord('Q'):
            return True

        # Tab — switch pane
        if key == ord('\t'):
            if self.pane == "parts":
                self.pane = "sections"
            else:
                self.pane = "parts"
            return False

        # Search
        if key == ord('/'):
            self.screen = "search"
            self.search_query = ""
            self.search_sel = 0
            return False

        # Self-test
        if key == ord('t') or key == ord('T'):
            self._suspend_curses()
            print()
            try:
                run_self_tests()
            except KeyboardInterrupt:
                print("\n  [Interrupted]")
            except Exception as e:
                print(f"\n  [ERROR]: {e}")
            print(f"\n{'─' * 50}")
            print("  Press Enter to return to TUI...")
            try:
                input()
            except (EOFError, KeyboardInterrupt):
                pass
            self._restore_curses()
            return False

        # Number keys 1-9: jump to part
        if ord('1') <= key <= ord('9'):
            part_num = key - ord('0')
            idx = part_num - 1
            if 0 <= idx < len(PARTS_LIST):
                self.part_idx = idx
                self.sec_idx = 0
                self.pane = "sections"
            return False

        # Navigation
        if self.pane == "parts":
            if key in (curses.KEY_UP, ord('k')):
                self.part_idx = max(0, self.part_idx - 1)
                self.sec_idx = 0
            elif key in (curses.KEY_DOWN, ord('j')):
                self.part_idx = min(len(PARTS_LIST) - 1, self.part_idx + 1)
                self.sec_idx = 0
            elif key in (curses.KEY_ENTER, 10, 13, curses.KEY_RIGHT, ord('l')):
                self.pane = "sections"
                self.sec_idx = 0
        else:  # sections pane
            if key in (curses.KEY_UP, ord('k')):
                self.sec_idx = max(0, self.sec_idx - 1)
            elif key in (curses.KEY_DOWN, ord('j')):
                self.sec_idx = min(len(sections) - 1, self.sec_idx + 1)
            elif key in (curses.KEY_LEFT, ord('h')):
                self.pane = "parts"
            elif key in (curses.KEY_ENTER, 10, 13, curses.KEY_RIGHT, ord('l')):
                if sections and self.sec_idx < len(sections):
                    sec_key = sections[self.sec_idx][0]
                    self._prepare_viewer(sec_key)
                    self.screen = "viewer"
            elif key == 27:  # Escape
                self.pane = "parts"
            elif key == ord('r'):
                if sections and self.sec_idx < len(sections):
                    sec_key = sections[self.sec_idx][0]
                    self._run_demo(sec_key)

        return False

    def _handle_viewer_key(self, key):
        """Handle key press in section viewer."""
        curses = self.curses
        code_h = self.h - 5
        total = len(self.viewer_lines)

        # Back to menu
        if key in (27, ord('q'), curses.KEY_LEFT, ord('h')):
            self.screen = "menu"
            return

        # Scroll up
        if key in (curses.KEY_UP, ord('k')):
            self.scroll_offset = max(0, self.scroll_offset - 1)
        # Scroll down
        elif key in (curses.KEY_DOWN, ord('j')):
            self.scroll_offset = min(max(0, total - code_h), self.scroll_offset + 1)
        # Page up
        elif key in (curses.KEY_PPAGE,):
            self.scroll_offset = max(0, self.scroll_offset - code_h)
        # Page down
        elif key in (curses.KEY_NPAGE,):
            self.scroll_offset = min(max(0, total - code_h), self.scroll_offset + code_h)
        # Home
        elif key in (curses.KEY_HOME,):
            self.scroll_offset = 0
        # End
        elif key in (curses.KEY_END,):
            self.scroll_offset = max(0, total - code_h)
        # Run demo
        elif key == ord('r'):
            sections = _get_sections_for_part(self.part_idx)
            if self.sec_idx < len(sections):
                sec_key = sections[self.sec_idx][0]
                self._run_demo(sec_key)

    def _handle_search_key(self, key):
        """Handle key press in search overlay."""
        curses = self.curses

        # Cancel
        if key == 27:
            self.screen = "menu"
            return

        # Select
        if key in (curses.KEY_ENTER, 10, 13):
            if self.search_results and self.search_sel < len(self.search_results):
                res = self.search_results[self.search_sel]
                sec_key, _, _, pidx, _ = res
                # Navigate to this section
                self.part_idx = pidx
                self.sec_idx = 0
                sections = _get_sections_for_part(pidx)
                for i, (k, *_) in enumerate(sections):
                    if k == sec_key:
                        self.sec_idx = i
                        break
                self._prepare_viewer(sec_key)
                self.screen = "viewer"
            return

        # Navigate results
        if key in (curses.KEY_UP,):
            self.search_sel = max(0, self.search_sel - 1)
            return
        if key in (curses.KEY_DOWN,):
            if self.search_results:
                self.search_sel = min(len(self.search_results) - 1, self.search_sel + 1)
            return

        # Backspace
        if key in (curses.KEY_BACKSPACE, 127, 8):
            self.search_query = self.search_query[:-1]
            self.search_sel = 0
            return

        # Regular character input
        if 32 <= key <= 126:
            self.search_query += chr(key)
            self.search_sel = 0


def _launch_tui(registry):
    """Launch the interactive TUI. Falls back gracefully on failure.

    Fallback chain:
      1. Full curses TUI (best experience)
      2. Clean error message + section list (usable without TUI)
      3. Help text (absolute minimum)
    """
    if not _can_use_curses():
        print()
        print("  PYTHON POWER USER — Interactive mode unavailable")
        print("  (No terminal detected, curses missing, or output is piped)")
        print()
        print("  To use this file:")
        print("    python python_poweruser.py --help       Show all options")
        print("    python python_poweruser.py --list       Browse all 47 sections")
        print("    python python_poweruser.py -s <name>    Run a specific section")
        print("    python python_poweruser.py --run        Run everything")
        print()
        return

    import curses

    def _main(stdscr):
        tui = PowerUserTUI(stdscr, registry)
        tui.run()

    try:
        curses.wrapper(_main)
    except KeyboardInterrupt:
        pass  # Clean Ctrl+C exit, wrapper handles terminal restore
    except Exception as e:
        # Graceful fallback — always leave terminal in good state
        try:
            curses.endwin()
        except Exception:
            pass
        print(f"\n  [INFO] TUI encountered an issue ({type(e).__name__}: {e}).")
        print("  Your terminal has been restored.\n")
        print("  Try: python python_poweruser.py --help\n")


def _parse_args_and_run():
    """Parse CLI arguments via argparse and dispatch.

    Fault-tolerant: _FaultTolerantParser never calls sys.exit().
    Parse errors raise _ParseError with a friendly message already
    printed; we catch it here and return gracefully.

    Handles:
      • All flags (-h, -l, -s, -r, -t, -f, --no-tui, --version)
      • Bare section names for backward compat (e.g. 'strings')
      • Legacy 'list' / 'test' bare commands
      • Mutually exclusive actions (argparse enforces this)
      • Fuzzy matching for typos (difflib + substring fallback)
      • Friendly error messages on stdout (not stderr)
    """
    parser = _build_parser()

    # ── Pre-parse: intercept legacy bare commands that argparse
    #    would choke on (e.g. 'list', 'test', bare section names) ──
    if len(sys.argv) == 2:
        bare = sys.argv[1]
        bare_lower = bare.lower()
        # Legacy 'list' command
        if bare_lower == "list":
            _cli_list()
            return
        # Legacy 'test' command
        if bare_lower == "test":
            run_self_tests()
            return

    # ── Parse with argparse (fault-tolerant: never sys.exit) ──
    try:
        args = parser.parse_args()
    except _ParseError:
        # _FaultTolerantParser already printed a friendly message;
        # just return gracefully — no traceback, no hard exit.
        return

    # Dispatch in priority order
    if args.list:
        _cli_list()
    elif args.section:
        _run_section_or_suggest(args.section)
    elif args.run or args.no_tui:
        run_all()
    elif args.test:
        run_self_tests()
    elif args.find:
        _cli_find(args.find)
    elif args.section_name:
        _run_section_or_suggest(args.section_name)
    else:
        # No flags, no args → launch interactive TUI
        _launch_tui(DEMO_REGISTRY)


def _run_section_or_suggest(name):
    """Run a section by name, or suggest close matches on typo.

    Uses difflib.get_close_matches for Levenshtein-style fuzzy matching
    plus simple substring containment as a fallback.
    """
    from difflib import get_close_matches
    sec_name = name.lower()

    if sec_name in DEMO_REGISTRY:
        DEMO_REGISTRY[sec_name]()
        return

    # Fuzzy match: Levenshtein distance first, then substring fallback
    keys = list(DEMO_REGISTRY.keys())
    close = get_close_matches(sec_name, keys, n=3, cutoff=0.5)
    if not close:
        # Substring fallback: 'deco' → 'decorators'
        close = [k for k in keys if sec_name in k or k in sec_name]

    print(f"  Unknown section: '{sec_name}'")
    if close:
        print(f"  Did you mean: {', '.join(close)}?")
    print("  Use --list to see available sections.")


# ═════════════════════════════════════════════════════════════════════════════
# ██████╗  █████╗ ██████╗ ████████╗     ██╗
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ███║
# ██████╔╝███████║██████╔╝   ██║       ╚██║
# ██╔═══╝ ██╔══██║██╔══██╗   ██║        ██║
# ██║     ██║  ██║██║  ██║   ██║        ██║
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝        ╚═╝
#  FOUNDATIONS — The atoms everything else is built from
# ═════════════════════════════════════════════════════════════════════════════


# %% 01 — Variables & Types
def demo_variables():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  01 — VARIABLES & TYPES                                            │
    │                                                                     │
    │  Feynman says: "A variable is a name tag, not a box."              │
    │  Python variables don't HOLD data — they POINT to objects in       │
    │  memory. Two names can point to the same object. This is why       │
    │  assignment works differently than you might expect from C/Java.   │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(1, "VARIABLES & TYPES")

    #* Python figures out the type for you — no int x = 5; nonsense
    name = "Stewart"           # str
    age = 49                   # int
    height = 5.11              # float
    is_learning = True         # bool
    nothing = None             # NoneType

    #* type() tells you what something IS
    print(f"name    → {type(name).__name__:>10}  │  '{name}'")
    print(f"age     → {type(age).__name__:>10}  │  {age}")
    print(f"height  → {type(height).__name__:>10}  │  {height}")
    print(f"is_learning → {type(is_learning).__name__:>6}  │  {is_learning}")
    print(f"nothing → {type(nothing).__name__:>10}  │  {nothing}")

    #* isinstance() is the pro way to check types (handles inheritance)
    print(f"\nisinstance(age, int)          → {isinstance(age, int)}")
    print(f"isinstance(age, (int, float)) → {isinstance(age, (int, float))}")

    #* Everything in Python is an object — even functions and classes
    print(f"\ntype(print)  → {type(print)}")
    print(f"type(int)    → {type(int)}")

    #* POWER USER: id() shows the memory address — proves names are pointers
    a = [1, 2, 3]
    b = a              # b now points to the SAME list object
    b.append(4)        # modifying b also modifies a — same object!
    print(f"\na = {a}")
    print(f"b = {b}")
    print(f"id(a) == id(b) → {id(a) == id(b)}  (same object in memory)")

    #* To get an actual copy:
    c = a.copy()       # shallow copy — new list, same inner objects
    c.append(5)
    print(f"c = {c}, a = {a}  (different objects now)")


# %% 02 — Numbers & Math
def demo_numbers():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  02 — NUMBERS & MATH                                               │
    │                                                                     │
    │  Einstein says: "As far as the laws of mathematics refer to        │
    │  reality, they are not certain; as far as they are certain, they   │
    │  do not refer to reality."                                         │
    │                                                                     │
    │  Python's integers have unlimited precision. Floats don't. Know    │
    │  where the dragons live.                                           │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(2, "NUMBERS & MATH")

    #* Basic arithmetic — nothing surprising here
    print(f"2 + 3   = {2 + 3}")
    print(f"2 ** 10 = {2 ** 10}")       # exponentiation
    print(f"17 / 5  = {17 / 5}")        # true division → always float
    print(f"17 // 5 = {17 // 5}")       # floor division → int
    print(f"17 % 5  = {17 % 5}")        # modulo (remainder)

    #* GOTCHA: Division ALWAYS returns float in Python 3
    print(f"\n10 / 2  = {10 / 2}  ← float, not int!")
    print(f"10 // 2 = {10 // 2}  ← use // if you want int")

    #* Python integers have UNLIMITED precision (no overflow!)
    big = 2 ** 1000
    print(f"\n2^1000 has {len(str(big))} digits — no overflow, ever")

    #! DANGER ZONE: Floating point is approximate
    print(f"\n0.1 + 0.2 == 0.3 → {0.1 + 0.2 == 0.3}  ← False!")
    print(f"0.1 + 0.2       → {0.1 + 0.2}")

    #* FIX: Use math.isclose() for float comparison
    import math
    print(f"math.isclose(0.1 + 0.2, 0.3) → {math.isclose(0.1 + 0.2, 0.3)}")

    #* FIX: Use Decimal for exact decimal math (money, etc.)
    from decimal import Decimal
    print(f"Decimal('0.1') + Decimal('0.2') = {Decimal('0.1') + Decimal('0.2')}")

    #* Useful number tricks
    print(f"\nabs(-42)        = {abs(-42)}")
    print(f"round(3.14159, 2) = {round(3.14159, 2)}")
    print(f"divmod(17, 5)   = {divmod(17, 5)}  ← (quotient, remainder)")
    print(f"max(3, 7, 1)    = {max(3, 7, 1)}")
    print(f"min(3, 7, 1)    = {min(3, 7, 1)}")

    #* POWER USER: Underscores as thousands separators (readability)
    million = 1_000_000
    print(f"\n1_000_000 = {million}")

    #* POWER USER: Numeric base conversions
    print(f"bin(255) = {bin(255)}")      # binary
    print(f"oct(255) = {oct(255)}")      # octal
    print(f"hex(255) = {hex(255)}")      # hexadecimal
    print(f"int('ff', 16) = {int('ff', 16)}")  # hex string → int


# %% 03 — Strings
def demo_strings():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  03 — STRINGS                                                      │
    │                                                                     │
    │  Feynman says: Strings are immutable sequences of Unicode chars.   │
    │  "Immutable" = once created, never changed. Every operation that   │
    │  looks like it modifies a string actually creates a brand new one. │
    │  This is WHY they can be dict keys and set members — they're       │
    │  reliable, unchanging labels.                                      │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(3, "STRINGS")

    text = "Hello, Python"

    #* ── SLICING: [start:stop:step] ──
    #  Think of indices as pointing BETWEEN characters:
    #   H | e | l | l | o | , |   | P | y | t | h  | o  | n
    #   0   1   2   3   4   5   6   7   8   9   10   11   12
    #  -13 -12 -11 -10  -9  -8  -7  -6  -5  -4  -3   -2   -1

    print(f"text[0:5]   → '{text[0:5]}'")       # Hello
    print(f"text[7:]    → '{text[7:]}'")         # Python
    print(f"text[-6:]   → '{text[-6:]}'")        # Python
    print(f"text[::-1]  → '{text[::-1]}'")       # Reverse
    print(f"text[::2]   → '{text[::2]}'")        # Every other char

    #* ── ESSENTIAL METHODS ──
    print(f"\n.upper()    → '{text.upper()}'")
    print(f".lower()    → '{text.lower()}'")
    print(f".title()    → '{text.title()}'")
    print(f".strip()    → '{'  spaces  '.strip()}'")
    print(f".replace()  → '{text.replace('Python', 'World')}'")
    print(f".split(',') → {text.split(',')}")
    print(f".find('Py') → {text.find('Py')}")    # returns index, -1 if not found
    print(f".count('l') → {text.count('l')}")

    #* ── CHECKING METHODS (return bool) ──
    print(f"\n'abc'.isalpha()  → {'abc'.isalpha()}")
    print(f"'123'.isdigit()  → {'123'.isdigit()}")
    print(f"'abc'.isalnum()  → {'abc'.isalnum()}")
    print(f"'ABC'.isupper()  → {'ABC'.isupper()}")
    print(f"'hello'.startswith('hel') → {'hello'.startswith('hel')}")
    print(f"'hello'.endswith('llo')   → {'hello'.endswith('llo')}")

    #* ── f-STRINGS (Python 3.6+): The only formatting you need ──
    name, age = "Stewart", 49
    pi = 3.14159
    print(f"\n{name} is {age}")                   # basic
    print(f"{pi:.2f}")                             # 2 decimal places
    print(f"{1000000:,}")                          # comma separator
    print(f"{42:08d}")                             # zero-padded
    print(f"{'left':<15}|")                        # left align
    print(f"{'center':^15}|")                      # center align
    print(f"{'right':>15}|")                       # right align

    #* POWER USER: f-string expressions (Python 3.8+ with = for debug)
    x = 42
    print(f"\n{x = }")                             # prints "x = 42"
    print(f"{len('hello') = }")                    # prints "len('hello') = 5"

    #* ── JOIN: The inverse of split ──
    words = ["Python", "is", "awesome"]
    print(f"\n' '.join(words) → '{' '.join(words)}'")
    print(f"', '.join(words) → '{', '.join(words)}'")

    #* ── MULTILINE STRINGS ──
    sql = """
        SELECT name, age
        FROM users
        WHERE age > 30
    """.strip()
    print(f"\nMultiline:\n{sql}")


# %% 04 — Booleans & None
def demo_booleans():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  04 — BOOLEANS & NONE                                              │
    │                                                                     │
    │  Einstein says: "Everything should be as simple as possible,       │
    │  but not simpler." Know what Python considers True and False —     │
    │  this is foundational to writing clean conditionals.               │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(4, "BOOLEANS & NONE")

    #* ── FALSY VALUES: These are ALL False in a boolean context ──
    #  Know these cold. Everything else is True.
    falsy_values = [False, 0, 0.0, "", [], {}, set(), None, 0j]
    print("Falsy values (all evaluate to False):")
    for val in falsy_values:
        print(f"  bool({str(val):>10}) → {bool(val)}")

    #* ── TRUTHY: Non-empty, non-zero = True ──
    print(f"\nbool([0])    → {bool([0])}   ← non-empty list, even if contents are 0")
    print(f"bool(' ')    → {bool(' ')}   ← space is not empty")
    print(f"bool(-1)     → {bool(-1)}   ← negative numbers are truthy")

    #* ── PYTHONIC EMPTY CHECKS ──
    items = []
    if not items:                           # DON'T: if len(items) == 0
        print("\nPythonic: 'if not items' checks emptiness")

    name = ""
    if not name:                            # DON'T: if name == ""
        print("Pythonic: 'if not name' checks empty string")

    #* ── NONE: Python's "nothing" — it's a singleton object ──
    x = None
    print(f"\nx is None → {x is None}")     # ALWAYS use 'is', never ==
    print(f"x == None → {x == None}")       # Works but WRONG — use 'is'

    #? Why 'is' not '=='? Because '==' can be overridden by classes.
    #  'is' checks identity (same object), '==' checks equality (same value).
    #  None is a singleton — there's exactly ONE None object in all of Python.

    #* ── SHORT-CIRCUIT EVALUATION ──
    #  'and' returns first falsy or last value
    #  'or' returns first truthy or last value
    print(f"\n'' or 'default'     → {'default'}")           # common default pattern
    print(f"'hello' or 'default' → {'hello' or 'default'}")
    print(f"0 or 42              → {0 or 42}")
    print(f"'hello' and 'world'  → {'hello' and 'world'}")  # both truthy → last
    print(f"'' and 'world'       → {'' and 'world'!r}")     # first falsy → ''

    #* POWER USER: None as default argument guard
    def greet(name=None):
        name = name or "World"     # if name is falsy, use "World"
        return f"Hello, {name}"
    print(f"\ngreet()         → {greet()}")
    print(f"greet('Stewart') → {greet('Stewart')}")


# ═════════════════════════════════════════════════════════════════════════════
# ██████╗  █████╗ ██████╗ ████████╗    ██████╗
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ╚════██╗
# ██████╔╝███████║██████╔╝   ██║        █████╔╝
# ██╔═══╝ ██╔══██║██╔══██╗   ██║       ██╔═══╝
# ██║     ██║  ██║██║  ██║   ██║       ███████╗
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚══════╝
#  DATA STRUCTURES — Your toolbox for organizing information
# ═════════════════════════════════════════════════════════════════════════════


# %% 05 — Lists
def demo_lists():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  05 — LISTS                                                        │
    │                                                                     │
    │  Feynman says: A list is like a train — ordered cars you can add,  │
    │  remove, or rearrange. It's the workhorse of Python. When in       │
    │  doubt, start with a list.                                         │
    │                                                                     │
    │  COMPLEXITY CHEAT SHEET:                                           │
    │    append()       O(1)    │  insert(i, x)  O(n)                   │
    │    pop()          O(1)    │  pop(i)        O(n)                   │
    │    x in list      O(n)    │  list[i]       O(1)                   │
    │    sort()         O(n log n)                                       │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(5, "LISTS")

    #* ── CREATING ──
    empty = []
    nums = [1, 2, 3, 4, 5]
    mixed = [1, "two", 3.0, True, None]    # can mix types (but usually don't)

    #* ── ADDING ──
    nums.append(6)              # add to end — O(1), fast
    nums.insert(0, 0)           #! add at position — O(n), slow (shifts everything)
    nums.extend([7, 8])         # add multiple — same as += [7, 8]

    #* ── REMOVING ──
    nums.remove(0)              # remove first occurrence by VALUE
    popped = nums.pop()         # remove & return last — O(1)
    popped_at = nums.pop(2)     # remove & return at index — O(n)
    print(f"After mutations: {nums}")

    #* ── SLICING (same as strings) ──
    print(f"\nnums[1:4]  → {nums[1:4]}")     # elements 1, 2, 3
    print(f"nums[::2]  → {nums[::2]}")       # every other element
    print(f"nums[::-1] → {nums[::-1]}")      # reversed copy

    #* ── USEFUL METHODS ──
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"\nsorted()   → {sorted(numbers)}")           # returns NEW list
    print(f"reversed() → {list(reversed(numbers))}")     # returns iterator → list
    print(f"index(5)   → {numbers.index(5)}")            # first index of value
    print(f"count(1)   → {numbers.count(1)}")            # how many times

    #* ── COPYING (know the difference!) ──
    original = [[1, 2], [3, 4]]
    shallow = original.copy()          # new list, but inner lists are SHARED
    import copy
    deep = copy.deepcopy(original)     # everything is independent

    shallow[0].append(99)
    print(f"\noriginal after shallow copy mutation: {original}")   # [1,2,99] — oops!
    print(f"deep copy is safe: {deep}")                            # [1,2] — untouched

    #* POWER USER: List as a stack (LIFO)
    stack = []
    stack.append("first")
    stack.append("second")
    stack.append("third")
    print(f"\nStack pop: {stack.pop()}")     # "third" — last in, first out


# %% 06 — Tuples
def demo_tuples():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  06 — TUPLES                                                       │
    │                                                                     │
    │  Einstein says: A tuple is a list that made a promise never to     │
    │  change. Because it can't change, Python trusts it more — you     │
    │  can use tuples as dictionary keys and set members.               │
    │                                                                     │
    │  TL;DR: Use tuples for fixed collections. Use lists for dynamic.  │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(6, "TUPLES")

    #* ── CREATING ──
    point = (3, 4)
    single = (42,)               #! The comma makes it a tuple, not the parens!
    not_a_tuple = (42)           # this is just int 42 in parentheses
    from_list = tuple([1, 2, 3])

    print(f"point       = {point}")
    print(f"single      = {single}  (type: {type(single).__name__})")
    print(f"not_a_tuple = {not_a_tuple}  (type: {type(not_a_tuple).__name__})")

    #* ── UNPACKING: The killer feature of tuples ──
    x, y = point                          # destructure into variables
    print(f"\nUnpacked: x={x}, y={y}")

    #* Swap variables — no temp variable needed!
    a, b = 1, 2
    a, b = b, a
    print(f"After swap: a={a}, b={b}")

    #* Extended unpacking with *
    first, *middle, last = [1, 2, 3, 4, 5]
    print(f"first={first}, middle={middle}, last={last}")

    #* ── WHY TUPLES MATTER ──
    #  1. Can be dict keys (lists can't)
    location_data = {(40.7128, -74.0060): "New York"}
    print(f"\nTuple as dict key: {location_data}")

    #  2. Functions returning multiple values actually return tuples
    def get_stats(numbers):
        return min(numbers), max(numbers), sum(numbers) / len(numbers)

    lo, hi, avg = get_stats([10, 20, 30, 40, 50])
    print(f"Stats: min={lo}, max={hi}, avg={avg}")

    #  3. Named tuples give you the best of both worlds (see Section 09)


# %% 07 — Dictionaries
def demo_dicts():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  07 — DICTIONARIES                                                 │
    │                                                                     │
    │  Feynman says: A dict is a lookup table. You give it a key, it    │
    │  gives you a value — in O(1) time. It uses hash tables under the  │
    │  hood. Every key gets hashed to a memory address, so Python can   │
    │  jump directly to the value without scanning.                     │
    │                                                                     │
    │  This is probably the most important data structure in Python.     │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(7, "DICTIONARIES")

    #* ── CREATING ──
    person = {"name": "Stewart", "age": 49, "city": "Whitsett"}
    from_pairs = dict([("a", 1), ("b", 2)])       # from list of tuples
    from_kwargs = dict(x=10, y=20)                  # keyword style

    #* ── ACCESSING ──
    print(f"person['name']        → {person['name']}")
    print(f"person.get('email')   → {person.get('email')}")          # None
    print(f"person.get('email', 'N/A') → {person.get('email', 'N/A')}")  # default

    #! person['email'] would raise KeyError — always use .get() for maybe-missing keys

    #* ── MODIFYING ──
    person["email"] = "stewart@example.com"       # add/update
    person.update({"age": 50, "state": "NC"})     # merge in
    removed = person.pop("email")                  # remove & return
    print(f"\nAfter mutations: {person}")

    #* ── ITERATING ──
    print("\nKeys & values:")
    for key, value in person.items():              #* .items() is the pro move
        print(f"  {key:>8} → {value}")

    #* ── DICT COMPREHENSION ──
    squares = {n: n**2 for n in range(6)}
    print(f"\nSquares: {squares}")

    #* ── MERGING (Python 3.9+) ──
    defaults = {"theme": "dark", "lang": "en"}
    overrides = {"lang": "zh", "debug": True}
    merged = defaults | overrides               # overrides wins on conflicts
    print(f"Merged: {merged}")

    #* ── POWER USER PATTERNS ──

    # Counting pattern
    words = "the cat sat on the mat the cat".split()
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1       # get with default 0
    print(f"\nWord counts: {counts}")

    # Grouping pattern
    names = ["Alice", "Bob", "Anna", "Bill", "Charlie", "Carl"]
    by_letter = {}
    for name in names:
        by_letter.setdefault(name[0], []).append(name)
    print(f"Grouped: {by_letter}")

    #* setdefault() → if key missing, set it to default AND return it
    #  This avoids the if-key-not-in-dict-then-create dance


# %% 08 — Sets
def demo_sets():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  08 — SETS                                                         │
    │                                                                     │
    │  Einstein says: Sets are collections with one rule — no repeats.  │
    │  Think Venn diagrams from math class. Membership testing is O(1)  │
    │  vs O(n) for lists. When you need to ask "is X in here?" fast,   │
    │  use a set.                                                        │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(8, "SETS")

    #* ── CREATING ──
    fruits = {"apple", "banana", "cherry"}
    from_list = set([1, 2, 2, 3, 3, 3])         # instant dedup
    empty_set = set()                             #! NOT {} — that's an empty dict!
    print(f"Deduped: {from_list}")

    #* ── SET MATH (Venn diagrams) ──
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}

    print(f"\na | b  (union)        → {a | b}")        # everything
    print(f"a & b  (intersection) → {a & b}")          # overlap
    print(f"a - b  (difference)   → {a - b}")          # in a, not in b
    print(f"a ^ b  (symmetric)    → {a ^ b}")          # in one, not both

    #* ── MEMBERSHIP TESTING (the main reason to use sets) ──
    big_list = list(range(100_000))
    big_set = set(big_list)

    #  "Is 99999 in here?"
    #  list: scans up to 100,000 items → O(n)
    #  set:  one hash lookup           → O(1)
    print(f"\n99999 in big_set → {99999 in big_set}")   # instant

    #* ── PRACTICAL: Finding differences between collections ──
    required = {"python", "sql", "git", "docker"}
    have = {"python", "git", "linux"}
    need = required - have
    print(f"\nSkills to learn: {need}")

    #* ── FROZEN SETS: immutable sets (can be dict keys) ──
    frozen = frozenset([1, 2, 3])
    # frozen.add(4)   #! AttributeError — can't modify


# %% 09 — Advanced Structures
def demo_advanced_structures():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  09 — ADVANCED STRUCTURES                                          │
    │                                                                     │
    │  Feynman says: Don't build what the standard library already has.  │
    │  These four tools eliminate 90% of boilerplate data code.          │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(9, "ADVANCED STRUCTURES")

    #* ── NAMEDTUPLE: Tuple with names (lightweight, immutable) ──
    from collections import namedtuple

    Point = namedtuple("Point", ["x", "y"])
    p = Point(3, 4)
    print(f"NamedTuple: p.x={p.x}, p.y={p.y}")
    print(f"  Still a tuple: p[0]={p[0]}")
    # p.x = 5   #! Can't modify — it's still immutable

    #* ── DATACLASS (Python 3.7+): The modern way to make data holders ──
    from dataclasses import dataclass, field

    @dataclass
    class Employee:
        name: str
        title: str
        salary: float
        skills: list = field(default_factory=list)   #* mutable defaults need field()

        @property
        def annual(self):
            return self.salary * 12

    emp = Employee("Stewart", "Supply Chain Analyst", 8000)
    emp.skills.append("Python")
    print(f"\nDataclass: {emp}")
    print(f"  Annual: ${emp.annual:,.0f}")

    #? Why dataclass over regular class? It auto-generates __init__, __repr__,
    #  __eq__, and more. Less boilerplate, same power.

    #* ── DEFAULTDICT: Dict that creates missing keys automatically ──
    from collections import defaultdict

    # Counting (no more "if key not in dict" checks)
    word_freq = defaultdict(int)              # missing keys start at 0
    for word in "the cat sat on the mat".split():
        word_freq[word] += 1
    print(f"\ndefaultdict(int): {dict(word_freq)}")

    # Grouping (no more setdefault dance)
    grouped = defaultdict(list)               # missing keys start as []
    for name in ["Alice", "Bob", "Anna", "Bill"]:
        grouped[name[0]].append(name)
    print(f"defaultdict(list): {dict(grouped)}")

    #* ── COUNTER: Purpose-built frequency counter ──
    from collections import Counter

    inventory = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    counts = Counter(inventory)
    print(f"\nCounter: {counts}")
    print(f"  Most common 2: {counts.most_common(2)}")
    print(f"  Total items:   {counts.total()}")

    # Counter arithmetic
    sales = Counter(apple=5, banana=3)
    restock = Counter(apple=10, banana=10, cherry=5)
    after = sales + restock
    print(f"  After restock:  {after}")


# ═════════════════════════════════════════════════════════════════════════════
# ██████╗  █████╗ ██████╗ ████████╗    ██████╗
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ╚════██╗
# ██████╔╝███████║██████╔╝   ██║        █████╔╝
# ██╔═══╝ ██╔══██║██╔══██╗   ██║        ╚═══██╗
# ██║     ██║  ██║██║  ██║   ██║       ██████╔╝
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚═════╝
#  CONTROL FLOW — Directing the program's path
# ═════════════════════════════════════════════════════════════════════════════


# %% 10 — Conditionals
def demo_conditionals():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  10 — CONDITIONALS                                                 │
    │                                                                     │
    │  Einstein says: "The only real valuable thing is intuition."       │
    │  Python's conditionals are designed to read like English — use     │
    │  that. If your conditional needs a comment to explain it,         │
    │  rewrite the conditional.                                          │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(10, "CONDITIONALS")

    value = 42

    #* ── BASIC if/elif/else ──
    if value > 100:
        tier = "high"
    elif value > 10:
        tier = "medium"
    else:
        tier = "low"
    print(f"value={value} → tier={tier}")

    #* ── TERNARY: One-liner for simple cases ──
    status = "adult" if value >= 18 else "minor"
    print(f"Ternary: {status}")

    #* ── CHAINED COMPARISONS: Python's secret weapon ──
    # Other languages: value > 0 && value < 100
    # Python: reads like math
    if 0 < value < 100:
        print("Chained: 0 < value < 100")

    #* ── IDENTITY vs EQUALITY ──
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a
    print(f"\na == b → {a == b}")    # True  — same VALUE
    print(f"a is b → {a is b}")      # False — different OBJECTS
    print(f"a is c → {a is c}")      # True  — same OBJECT

    #? When to use 'is': ONLY for None, True, False
    #  Always: if x is None     Never: if x == None

    #* ── in OPERATOR: Membership testing ──
    fruits = ["apple", "banana", "cherry"]
    if "banana" in fruits:
        print("\n'in' works for lists, strings, dicts, sets...")

    if "py" in "python":
        print("'in' works for substring check too")

    #* ── MATCH/CASE (Python 3.10+): Structural pattern matching ──
    def handle_command(command):
        match command.split():
            case ["quit"]:
                return "Exiting"
            case ["go", direction]:
                return f"Going {direction}"
            case ["pick", "up", item]:
                return f"Picked up {item}"
            case _:                              # _ is the wildcard/default
                return f"Unknown: {command}"

    print(f"\nmatch 'go north'    → {handle_command('go north')}")
    print(f"match 'pick up key' → {handle_command('pick up key')}")
    print(f"match 'dance'       → {handle_command('dance')}")


# %% 11 — Loops
def demo_loops():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  11 — LOOPS                                                        │
    │                                                                     │
    │  Feynman says: "In Python, you iterate over things, not indices." │
    │  If you're writing range(len(x)), you're doing it wrong. Python   │
    │  gives you enumerate, zip, and direct iteration — use them.       │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(11, "LOOPS")

    #* ── FOR: Iterate directly over objects ──
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:                    # DON'T: for i in range(len(fruits))
        print(f"  {fruit}")

    #* ── ENUMERATE: When you need the index too ──
    for i, fruit in enumerate(fruits):
        print(f"  [{i}] {fruit}")

    for i, fruit in enumerate(fruits, start=1):    # start counting at 1
        print(f"  {i}. {fruit}")

    #* ── ZIP: Parallel iteration ──
    names = ["Alice", "Bob", "Charlie"]
    scores = [95, 87, 92]
    for name, score in zip(names, scores):
        print(f"  {name}: {score}")

    #* ZIP stops at the shortest — use zip_longest for padding
    from itertools import zip_longest
    short = [1, 2]
    long = [10, 20, 30]
    print(f"\nzip_longest: {list(zip_longest(short, long, fillvalue=0))}")

    #* ── WHILE: When you don't know how many iterations ──
    count = 0
    while count < 3:
        print(f"  count = {count}")
        count += 1

    #* ── BREAK, CONTINUE, ELSE ──
    for n in range(2, 20):
        for i in range(2, n):
            if n % i == 0:
                break                       # not prime, stop checking
        else:
            #* 'else' on a for loop runs when loop DIDN'T break
            #  This is rare but perfect for search patterns
            print(f"  {n} is prime", end="  ")
    print()

    #* ── LOOP IDIOMS ──

    # Build a dict from two lists
    keys = ["name", "age", "city"]
    vals = ["Stewart", 49, "Whitsett"]
    d = dict(zip(keys, vals))
    print(f"\ndict(zip(...)): {d}")

    # Iterate with index AND value from a dict
    for key, val in d.items():
        print(f"  {key}: {val}")


# %% 12 — Comprehensions
def demo_comprehensions():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  12 — COMPREHENSIONS                                               │
    │                                                                     │
    │  Einstein says: Comprehensions are Python's answer to the          │
    │  question "how do I transform data in one readable line?"          │
    │                                                                     │
    │  PATTERN: [expression FOR item IN iterable IF condition]           │
    │  That's it. Same pattern works for lists, dicts, sets, generators. │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(12, "COMPREHENSIONS")

    numbers = range(20)

    #* ── LIST COMPREHENSION ──
    squares = [n**2 for n in range(10)]
    evens = [n for n in numbers if n % 2 == 0]
    print(f"Squares: {squares}")
    print(f"Evens:   {evens}")

    #* ── WITH CONDITIONAL EXPRESSION ──
    labels = ["even" if n % 2 == 0 else "odd" for n in range(6)]
    print(f"Labels:  {labels}")

    #* ── NESTED COMPREHENSION (read left-to-right like nested loops) ──
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flat = [x for row in matrix for x in row]       # flatten
    print(f"Flat:    {flat}")

    #  Same as:
    #  flat = []
    #  for row in matrix:        ← outer loop comes first
    #      for x in row:         ← inner loop comes second
    #          flat.append(x)

    #* ── DICT COMPREHENSION ──
    word_lens = {w: len(w) for w in ["Python", "is", "great"]}
    inverted = {v: k for k, v in {"a": 1, "b": 2}.items()}    # swap keys/values
    print(f"Word lens: {word_lens}")
    print(f"Inverted:  {inverted}")

    #* ── SET COMPREHENSION ──
    unique_lengths = {len(w) for w in ["hi", "hello", "hey", "howdy"]}
    print(f"Unique lengths: {unique_lengths}")

    #* ── GENERATOR EXPRESSION (lazy — doesn't build the whole list) ──
    total = sum(n**2 for n in range(1000))          # () not [] — no list created
    print(f"Sum of squares 0-999: {total}")

    #? When to use generator vs list comprehension?
    #  Generator: when you only need to iterate ONCE (sum, any, all, for loop)
    #  List: when you need to index, slice, or iterate multiple times

    #* ── POWER USER: any() and all() with generators ──
    data = [2, 4, 6, 8, 10]
    print(f"\nall even?   {all(n % 2 == 0 for n in data)}")
    print(f"any > 5?    {any(n > 5 for n in data)}")

    # Find first match (or None)
    first_big = next((n for n in data if n > 7), None)
    print(f"First > 7:  {first_big}")


# ═════════════════════════════════════════════════════════════════════════════
# ██████╗  █████╗ ██████╗ ████████╗    ██╗  ██╗
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ██║  ██║
# ██████╔╝███████║██████╔╝   ██║       ███████║
# ██╔═══╝ ██╔══██║██╔══██╗   ██║       ╚════██║
# ██║     ██║  ██║██║  ██║   ██║            ██║
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝            ╚═╝
#  FUNCTIONS — Reusable building blocks
# ═════════════════════════════════════════════════════════════════════════════


# %% 13 — Function Basics
def demo_functions():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  13 — FUNCTION BASICS                                              │
    │                                                                     │
    │  Feynman says: "A function is a machine. Stuff goes in, stuff     │
    │  comes out. The beauty is you don't need to know HOW it works     │
    │  to USE it — that's abstraction."                                 │
    │                                                                     │
    │  ARGUMENT ORDER: positional → *args → keyword → **kwargs          │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(13, "FUNCTION BASICS")

    #* ── BASIC FUNCTION ──
    def add(a, b):
        """Add two numbers. ← This is a docstring. Always write one."""
        return a + b

    print(f"add(3, 4)  → {add(3, 4)}")
    print(f"add(b=4, a=3) → {add(b=4, a=3)}")    # keyword args, any order

    #* ── DEFAULT VALUES ──
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"

    print(f"\ngreet('Stewart')           → {greet('Stewart')}")
    print(f"greet('Stewart', 'Hey')    → {greet('Stewart', 'Hey')}")

    #! DANGER: Mutable default arguments are shared across calls!
    def bad_append(item, items=[]):     # BUG: this [] is created ONCE
        items.append(item)
        return items

    bad_append(1)
    print(f"\nbad_append(2) → {bad_append(2)}")    # [1, 2] — not [2]!

    def good_append(item, items=None):  #* FIX: use None as default
        if items is None:
            items = []
        items.append(item)
        return items

    #* ── *args AND **kwargs ──
    def flexible(required, *args, **kwargs):
        """
        required: must provide
        *args:    captures extra positional args as a TUPLE
        **kwargs: captures extra keyword args as a DICT
        """
        print(f"  required: {required}")
        print(f"  args:     {args}")
        print(f"  kwargs:   {kwargs}")

    print("\nflexible(1, 2, 3, x=10, y=20):")
    flexible(1, 2, 3, x=10, y=20)

    #* ── KEYWORD-ONLY ARGUMENTS (after *) ──
    def search(query, *, case_sensitive=False, limit=10):
        """* forces case_sensitive and limit to be keyword-only."""
        return f"Searching '{query}' (case={case_sensitive}, limit={limit})"

    print(f"\n{search('python', case_sensitive=True)}")
    # search('python', True)  #! TypeError — must use keyword

    #* ── MULTIPLE RETURN VALUES (really a tuple) ──
    def analyze(numbers):
        return min(numbers), max(numbers), sum(numbers) / len(numbers)

    lo, hi, avg = analyze([10, 20, 30, 40])
    print(f"\nmin={lo}, max={hi}, avg={avg}")

    #* ── FUNCTIONS ARE OBJECTS (first-class) ──
    operations = {"add": add, "greet": greet}
    print(f"\nFunctions in a dict: {operations['add'](10, 20)}")


# %% 14 — Scope & Closures
def demo_scope():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  14 — SCOPE & CLOSURES                                             │
    │                                                                     │
    │  Einstein says: "God does not play dice with the universe."        │
    │  Neither does Python with variable scope. It follows the LEGB     │
    │  rule — Local, Enclosing, Global, Built-in — in that exact order. │
    │                                                                     │
    │  A closure is a function that remembers variables from its         │
    │  enclosing scope even after that scope has finished executing.     │
    │  Think of it as a function with a backpack of captured variables.  │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(14, "SCOPE & CLOSURES")

    #* ── LEGB RULE ──
    global_var = "I'm global"               # G — module level

    def outer():
        enclosing_var = "I'm enclosing"     # E — enclosing function

        def inner():
            local_var = "I'm local"         # L — local to inner
            # Python searches: L → E → G → B (built-ins like len, print)
            print(f"  local:     {local_var}")
            print(f"  enclosing: {enclosing_var}")
            print(f"  global:    {global_var}")
            print(f"  built-in:  {len}")      # B — built-in functions

        inner()

    outer()

    #* ── CLOSURE: Function factory ──
    def make_multiplier(factor):
        """Returns a function that multiplies by 'factor'."""
        def multiply(x):
            return x * factor               # 'factor' is captured from enclosing
        return multiply                      # return the function, not its result

    double = make_multiplier(2)
    triple = make_multiplier(3)
    print(f"\ndouble(5) → {double(5)}")      # 10
    print(f"triple(5) → {triple(5)}")        # 15

    #? Why is this useful? Decorators, callback factories, configuration.
    #  You create specialized functions at runtime without classes.

    #* ── CLOSURE: Counter (encapsulated state) ──
    def make_counter(start=0):
        count = [start]                      # list because we need mutability
        def increment():
            count[0] += 1
            return count[0]
        return increment

    counter = make_counter()
    print(f"\ncounter() → {counter()}")       # 1
    print(f"counter() → {counter()}")         # 2
    print(f"counter() → {counter()}")         # 3

    #* ── NONLOCAL: Modify enclosing variable directly ──
    def make_counter_v2(start=0):
        count = start
        def increment():
            nonlocal count                   # lets us modify enclosing 'count'
            count += 1
            return count
        return increment

    c = make_counter_v2(10)
    print(f"\nnonlocal counter: {c()}, {c()}, {c()}")    # 11, 12, 13


# %% 15 — Lambda & Functional
def demo_lambda():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  15 — LAMBDA & FUNCTIONAL PROGRAMMING                              │
    │                                                                     │
    │  Feynman says: A lambda is a nameless function — a one-line       │
    │  throwaway. Use it when a full 'def' would be overkill. But if    │
    │  you need two lines, give it a name.                               │
    │                                                                     │
    │  Functional programming = treating functions as data. You pass     │
    │  them around, return them, combine them like Lego bricks.         │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(15, "LAMBDA & FUNCTIONAL")

    #* ── LAMBDA: anonymous single-expression function ──
    square = lambda x: x ** 2                   # same as def square(x): return x**2
    add = lambda a, b: a + b
    print(f"square(5) → {square(5)}")
    print(f"add(3, 4) → {add(3, 4)}")

    #* ── SORTING: The #1 use case for lambda ──
    people = [("Bob", 30), ("Alice", 25), ("Charlie", 35)]
    by_age = sorted(people, key=lambda p: p[1])
    by_name = sorted(people, key=lambda p: p[0])
    print(f"\nBy age:  {by_age}")
    print(f"By name: {by_name}")

    # Sorting dicts — extremely common
    items = [{"name": "Laptop", "price": 999},
             {"name": "Mouse", "price": 25},
             {"name": "Keyboard", "price": 75}]
    by_price = sorted(items, key=lambda x: x["price"])
    print(f"By price: {[i['name'] for i in by_price]}")

    #* ── MAP: Apply function to every element ──
    nums = [1, 2, 3, 4, 5]
    doubled = list(map(lambda x: x * 2, nums))
    print(f"\nmap (doubled): {doubled}")
    #? Pythonic alternative: [x * 2 for x in nums]

    #* ── FILTER: Keep elements where function returns True ──
    evens = list(filter(lambda x: x % 2 == 0, nums))
    print(f"filter (evens): {evens}")
    #? Pythonic alternative: [x for x in nums if x % 2 == 0]

    #* ── REDUCE: Accumulate into single value ──
    from functools import reduce
    total = reduce(lambda acc, x: acc + x, nums, 0)
    product = reduce(lambda acc, x: acc * x, nums, 1)
    print(f"reduce (sum):     {total}")
    print(f"reduce (product): {product}")
    #? Pythonic alternative: sum(nums), math.prod(nums)

    #* ── WHEN TO USE WHAT ──
    #  List comprehension > map/filter for most cases (more readable)
    #  Lambda + sorted() is THE standard pattern — learn it cold
    #  reduce() is rarely needed — sum(), max(), min() cover most cases


# %% 16 — Decorators
def demo_decorators():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  16 — DECORATORS                                                   │
    │                                                                     │
    │  Einstein says: "Imagination is more important than knowledge."    │
    │  Decorators are Python's most imaginative feature. They let you    │
    │  wrap functions with new behavior — logging, timing, caching,     │
    │  authentication — WITHOUT modifying the original code.            │
    │                                                                     │
    │  @decorator is just syntactic sugar for: func = decorator(func)   │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(16, "DECORATORS")

    import time
    from functools import wraps

    #* ── BASIC DECORATOR ──
    def timer(func):
        @wraps(func)                        #* preserves original function metadata
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            print(f"  ⏱  {func.__name__} took {elapsed:.4f}s")
            return result
        return wrapper

    @timer
    def slow_add(a, b):
        """Add two numbers, slowly."""
        time.sleep(0.05)
        return a + b

    result = slow_add(3, 4)
    print(f"  Result: {result}")
    print(f"  Docstring preserved: {slow_add.__doc__}")

    #* ── DECORATOR WITH ARGUMENTS ──
    def retry(max_attempts=3):
        """Retry a function up to N times on failure."""
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                for attempt in range(1, max_attempts + 1):
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        print(f"  Attempt {attempt}/{max_attempts} failed: {e}")
                        if attempt == max_attempts:
                            raise
            return wrapper
        return decorator

    call_count = 0

    @retry(max_attempts=3)
    def flaky_function():
        nonlocal call_count
        call_count += 1
        if call_count < 3:
            raise ConnectionError("Network timeout")
        return "Success!"

    print(f"\n{flaky_function()}")

    #* ── DECORATOR: Logging ──
    def log_calls(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            args_str = ", ".join(map(repr, args))
            kwargs_str = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
            all_args = ", ".join(filter(None, [args_str, kwargs_str]))
            print(f"  → {func.__name__}({all_args})")
            result = func(*args, **kwargs)
            print(f"  ← {func.__name__} returned {result!r}")
            return result
        return wrapper

    @log_calls
    def calculate(x, y, operation="add"):
        ops = {"add": x + y, "mul": x * y}
        return ops.get(operation, 0)

    print(f"\n")
    calculate(3, 4, operation="mul")

    #* ── STACKING DECORATORS (applied bottom-up) ──
    @timer
    @log_calls
    def process(data):
        return sorted(data)

    print(f"\n")
    process([3, 1, 4, 1, 5])


# %% 17 — Functools
def demo_functools():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  17 — FUNCTOOLS                                                    │
    │                                                                     │
    │  Feynman says: "The standard library is your secret weapon. Most  │
    │  patterns you're about to code already exist in functools."       │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(17, "FUNCTOOLS")

    from functools import lru_cache, partial, wraps, reduce

    #* ── LRU_CACHE: Instant memoization ──
    #  Caches results of expensive function calls.
    #  Same input → return cached result instead of recalculating.

    @lru_cache(maxsize=128)
    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    #  Without cache: O(2^n) — impossibly slow for n=100
    #  With cache: O(n) — instant
    print(f"fibonacci(50)  → {fibonacci(50)}")
    print(f"Cache info: {fibonacci.cache_info()}")

    #* ── PARTIAL: Pre-fill some arguments ──
    def power(base, exponent):
        return base ** exponent

    square = partial(power, exponent=2)           # pre-fill exponent=2
    cube = partial(power, exponent=3)
    print(f"\nsquare(5)  → {square(5)}")
    print(f"cube(5)    → {cube(5)}")

    #? Use case: creating specialized versions of general functions
    import json
    pretty_json = partial(json.dumps, indent=2, sort_keys=True)
    print(f"\n{pretty_json({'b': 2, 'a': 1})}")

    #* ── REDUCE: Accumulate a sequence into a single value ──
    from operator import mul
    factorial_10 = reduce(mul, range(1, 11))
    print(f"\n10! = {factorial_10}")


# ═════════════════════════════════════════════════════════════════════════════
# ██████╗  █████╗ ██████╗ ████████╗    ███████╗
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ██╔════╝
# ██████╔╝███████║██████╔╝   ██║       ███████╗
# ██╔═══╝ ██╔══██║██╔══██╗   ██║       ╚════██║
# ██║     ██║  ██║██║  ██║   ██║       ███████║
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚══════╝
#  OOP — Object-Oriented Programming
# ═════════════════════════════════════════════════════════════════════════════


# %% 18 — Classes
def demo_classes():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  18 — CLASSES                                                      │
    │                                                                     │
    │  Einstein says: "A class is a blueprint. An object is a building  │
    │  made from that blueprint. You can make many buildings from one   │
    │  blueprint, each with its own address and paint color."           │
    │                                                                     │
    │  TL;DR: Use classes when your data needs BEHAVIOR (methods).      │
    │  Use dicts/dataclasses when it's just data storage.               │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(18, "CLASSES")

    class BankAccount:
        #* CLASS VARIABLE — shared by ALL instances
        bank_name = "Python National Bank"

        def __init__(self, owner, balance=0):
            #* INSTANCE VARIABLES — unique per object
            self.owner = owner
            self.balance = balance
            self._transactions = []         # _ prefix = "private by convention"

        def deposit(self, amount):
            if amount <= 0:
                raise ValueError("Deposit must be positive")
            self.balance += amount
            self._transactions.append(f"+{amount}")
            return self

        def withdraw(self, amount):
            if amount > self.balance:
                raise ValueError("Insufficient funds")
            self.balance -= amount
            self._transactions.append(f"-{amount}")
            return self                     #* returning self enables chaining

        @classmethod
        def from_csv(cls, csv_string):
            """Alternative constructor — creates from CSV data."""
            owner, balance = csv_string.split(",")
            return cls(owner.strip(), float(balance))

        @staticmethod
        def is_valid_amount(amount):
            """Utility — doesn't need instance or class data."""
            return isinstance(amount, (int, float)) and amount > 0

        def __str__(self):
            """What users see: print(account)"""
            return f"{self.owner}'s account: ${self.balance:,.2f}"

        def __repr__(self):
            """What developers see: in debugger/REPL"""
            return f"BankAccount('{self.owner}', {self.balance})"

    #* ── USAGE ──
    acct = BankAccount("Stewart", 1000)
    acct.deposit(500).withdraw(200)          # method chaining!
    print(acct)
    print(f"repr: {acct!r}")

    #* Alternative constructor
    acct2 = BankAccount.from_csv("Alice, 5000")
    print(f"From CSV: {acct2}")

    #* Static method
    print(f"Valid amount? {BankAccount.is_valid_amount(100)}")

    #* Class variable is shared
    print(f"Bank: {acct.bank_name}")
    print(f"Bank: {acct2.bank_name}")


# %% 19 — Inheritance
def demo_inheritance():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  19 — INHERITANCE                                                  │
    │                                                                     │
    │  Feynman says: Inheritance lets you build specialized things from │
    │  general things. A Dog IS an Animal. A Car IS a Vehicle. The      │
    │  child inherits everything from the parent, then adds or          │
    │  overrides what's different.                                       │
    │                                                                     │
    │  Rule of thumb: "is-a" → inheritance. "has-a" → composition.     │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(19, "INHERITANCE")

    class Shape:
        def __init__(self, color="black"):
            self.color = color

        def area(self):
            raise NotImplementedError("Subclasses must implement area()")

        def describe(self):
            return f"{self.color} {type(self).__name__}: area={self.area():.2f}"

    class Circle(Shape):
        def __init__(self, radius, color="black"):
            super().__init__(color)          #* call parent's __init__
            self.radius = radius

        def area(self):
            import math
            return math.pi * self.radius ** 2

    class Rectangle(Shape):
        def __init__(self, width, height, color="black"):
            super().__init__(color)
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

    class Square(Rectangle):                 # Square IS a Rectangle
        def __init__(self, side, color="black"):
            super().__init__(side, side, color)

    #* ── POLYMORPHISM: Same interface, different behavior ──
    shapes = [
        Circle(5, "red"),
        Rectangle(4, 6, "blue"),
        Square(3, "green"),
    ]
    for shape in shapes:
        print(f"  {shape.describe()}")

    #* ── isinstance and issubclass ──
    s = Square(5)
    print(f"\nisinstance(s, Square)    → {isinstance(s, Square)}")
    print(f"isinstance(s, Rectangle) → {isinstance(s, Rectangle)}")  # True!
    print(f"isinstance(s, Shape)     → {isinstance(s, Shape)}")      # True!
    print(f"issubclass(Square, Rectangle) → {issubclass(Square, Rectangle)}")

    #* ── METHOD RESOLUTION ORDER (MRO) ──
    print(f"\nSquare MRO: {[c.__name__ for c in Square.__mro__]}")


# %% 20 — Dunder Methods
def demo_dunders():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  20 — DUNDER METHODS (Magic Methods)                               │
    │                                                                     │
    │  Einstein says: Dunder methods (double underscore: __xxx__)        │
    │  let your objects behave like built-in types. Want your object to  │
    │  work with +? Implement __add__. Want len()? Implement __len__.   │
    │  It's Python's operator overloading system.                        │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(20, "DUNDER METHODS")

    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        # String representations
        def __repr__(self):                  # for developers/debugging
            return f"Vector({self.x}, {self.y})"

        def __str__(self):                   # for users/print
            return f"({self.x}, {self.y})"

        # Arithmetic operators
        def __add__(self, other):            # v1 + v2
            return Vector(self.x + other.x, self.y + other.y)

        def __sub__(self, other):            # v1 - v2
            return Vector(self.x - other.x, self.y - other.y)

        def __mul__(self, scalar):           # v * 3
            return Vector(self.x * scalar, self.y * scalar)

        def __abs__(self):                   # abs(v) → magnitude
            return (self.x**2 + self.y**2) ** 0.5

        # Comparison
        def __eq__(self, other):             # v1 == v2
            return self.x == other.x and self.y == other.y

        def __lt__(self, other):             # v1 < v2 (by magnitude)
            return abs(self) < abs(other)

        # Container protocol
        def __len__(self):                   # len(v) → dimensions
            return 2

        def __getitem__(self, index):        # v[0], v[1]
            return (self.x, self.y)[index]

        def __iter__(self):                  # for x in v, unpacking
            yield self.x
            yield self.y

        # Boolean
        def __bool__(self):                  # bool(v), if v:
            return abs(self) > 0

    #* ── DEMO ──
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)

    print(f"v1        = {v1}")
    print(f"v1 + v2   = {v1 + v2}")
    print(f"v1 - v2   = {v1 - v2}")
    print(f"v1 * 3    = {v1 * 3}")
    print(f"|v1|      = {abs(v1)}")
    print(f"v1 == v2  = {v1 == v2}")
    print(f"len(v1)   = {len(v1)}")
    print(f"v1[0]     = {v1[0]}")

    # Unpacking works because of __iter__
    x, y = v1
    print(f"Unpacked: x={x}, y={y}")

    #* ── MOST USEFUL DUNDERS CHEAT SHEET ──
    #   __init__     constructor
    #   __repr__     developer-friendly string
    #   __str__      user-friendly string
    #   __eq__       ==
    #   __lt__       <  (enables sorted() with your objects!)
    #   __hash__     makes object usable as dict key / set member
    #   __len__      len()
    #   __getitem__  indexing with []
    #   __iter__     for loops, unpacking
    #   __contains__ 'in' operator
    #   __call__     object() — make instance callable like a function
    #   __enter__/__exit__  context manager (with statement)


# %% 21 — Properties & Slots
def demo_properties():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  21 — PROPERTIES & SLOTS                                           │
    │                                                                     │
    │  Feynman says: Properties let you put a gatekeeper on attribute   │
    │  access. Instead of obj.x blindly reading/writing, you run code.  │
    │  Slots tell Python exactly which attributes to expect, saving     │
    │  memory and catching typos.                                        │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(21, "PROPERTIES & SLOTS")

    #* ── PROPERTY: Controlled attribute access ──
    class Temperature:
        def __init__(self, celsius):
            self.celsius = celsius           # triggers the setter

        @property
        def celsius(self):                   # getter
            return self._celsius

        @celsius.setter
        def celsius(self, value):            # setter with validation
            if value < -273.15:
                raise ValueError("Temperature below absolute zero")
            self._celsius = value

        @property
        def fahrenheit(self):                # computed/derived property
            return self._celsius * 9/5 + 32

        @fahrenheit.setter
        def fahrenheit(self, value):
            self.celsius = (value - 32) * 5/9

    temp = Temperature(100)
    print(f"celsius:    {temp.celsius}°C")
    print(f"fahrenheit: {temp.fahrenheit}°F")

    temp.fahrenheit = 32
    print(f"Set 32°F → {temp.celsius}°C")

    #? Why not just use methods like get_temp()/set_temp()?
    #  Properties let you START with simple attributes, then ADD
    #  validation/computation LATER without changing the interface.
    #  Callers still use obj.celsius — they never know a function runs.

    #* ── __SLOTS__: Memory optimization ──
    class PointWithSlots:
        __slots__ = ('x', 'y')              # only these attributes allowed
        def __init__(self, x, y):
            self.x = x
            self.y = y

    class PointWithoutSlots:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    p = PointWithSlots(1, 2)
    print(f"\nSlots point: ({p.x}, {p.y})")
    # p.z = 3   #! AttributeError — slots prevents arbitrary attributes
    # This catches typos and saves ~40% memory per instance

    import sys
    p1 = PointWithSlots(1, 2)
    p2 = PointWithoutSlots(1, 2)
    print(f"With slots:    {sys.getsizeof(p1)} bytes")
    print(f"Without slots: {sys.getsizeof(p2)} + {sys.getsizeof(p2.__dict__)} dict bytes")


# %% 22 — ABCs & Protocols
def demo_abcs():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  22 — ABCs & PROTOCOLS                                             │
    │                                                                     │
    │  Einstein says: An ABC is a contract — "if you want to be a       │
    │  Shape, you MUST implement area()." A Protocol is duck typing      │
    │  with documentation — "if it has area(), I'll treat it as a       │
    │  Shape, no inheritance required."                                  │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(22, "ABCs & PROTOCOLS")

    #* ── ABSTRACT BASE CLASS: Enforced interface ──
    from abc import ABC, abstractmethod

    class Drawable(ABC):
        @abstractmethod
        def draw(self):
            """Subclasses MUST implement this."""
            pass

        def clear(self):                     # concrete method — inherited as-is
            print("  Cleared canvas")

    # d = Drawable()   #! TypeError — can't instantiate abstract class

    class Circle(Drawable):
        def draw(self):
            print("  Drawing circle ○")

    c = Circle()
    c.draw()
    c.clear()

    #* ── PROTOCOL (Python 3.8+): Structural typing (duck typing) ──
    from typing import Protocol, runtime_checkable

    @runtime_checkable
    class Printable(Protocol):
        def to_string(self) -> str: ...      # just the signature

    class Report:
        def to_string(self) -> str:
            return "Q4 Report"

    class Invoice:
        def to_string(self) -> str:
            return "Invoice #1234"

    # Neither inherits from Printable — but both satisfy its protocol
    def output(item: Printable):
        print(f"  Output: {item.to_string()}")

    output(Report())
    output(Invoice())
    print(f"\nReport is Printable? {isinstance(Report(), Printable)}")

    #? ABC vs Protocol?
    #  ABC:      "You must inherit from me" → explicit, enforced
    #  Protocol: "Just have the methods"    → flexible, duck typing
    #  Prefer Protocol for loose coupling. Use ABC when you need strict contracts.


# ═════════════════════════════════════════════════════════════════════════════
# ██████╗  █████╗ ██████╗ ████████╗     ██████╗
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ██╔════╝
# ██████╔╝███████║██████╔╝   ██║       ███████╗
# ██╔═══╝ ██╔══██║██╔══██╗   ██║       ██╔═══██╗
# ██║     ██║  ██║██║  ██║   ██║       ╚██████╔╝
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝        ╚═════╝
#  ERROR HANDLING — Graceful failure
# ═════════════════════════════════════════════════════════════════════════════


# %% 23 — Exceptions
def demo_exceptions():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  23 — EXCEPTIONS                                                   │
    │                                                                     │
    │  Feynman says: "The exception is the rule." Errors are normal.    │
    │  The question isn't IF things will go wrong, but how gracefully   │
    │  you handle it when they do.                                       │
    │                                                                     │
    │  GOLDEN RULE: Catch specific exceptions. Never bare except:.      │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(23, "EXCEPTIONS")

    #* ── BASIC TRY/EXCEPT ──
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Caught: {e}")
        result = float('inf')

    #* ── MULTIPLE EXCEPTIONS ──
    def safe_convert(value):
        try:
            return int(value)
        except (ValueError, TypeError) as e:
            print(f"  Can't convert {value!r}: {e}")
            return None

    safe_convert("abc")
    safe_convert(None)

    #* ── THE FULL PATTERN: try/except/else/finally ──
    def read_config(path):
        try:
            with open(path) as f:
                data = f.read()
        except FileNotFoundError:
            print("  File not found — using defaults")
            data = "{}"
        except PermissionError:
            print("  No permission — using defaults")
            data = "{}"
        else:
            #* Only runs if NO exception occurred
            print(f"  Config loaded ({len(data)} chars)")
        finally:
            #* ALWAYS runs — cleanup goes here
            print("  Config attempt complete")
        return data

    read_config("/nonexistent/path")

    #* ── RAISING EXCEPTIONS ──
    def validate_email(email):
        if "@" not in email:
            raise ValueError(f"Invalid email: {email}")
        return email

    try:
        validate_email("not-an-email")
    except ValueError as e:
        print(f"\nRaised: {e}")

    #* ── EXCEPTION HIERARCHY (know the important ones) ──
    # BaseException
    #  └── Exception                 ← catch this or below, never BaseException
    #       ├── ValueError           argument has right type, wrong value
    #       ├── TypeError            wrong type entirely
    #       ├── KeyError             dict key not found
    #       ├── IndexError           list index out of range
    #       ├── AttributeError       object has no such attribute
    #       ├── FileNotFoundError    file doesn't exist
    #       ├── IOError              general I/O failure
    #       ├── RuntimeError         generic runtime issue
    #       └── StopIteration        iterator exhausted (internal use)

    #* ── EAFP vs LBYL ──
    data = {"key": "value"}

    # LBYL (Look Before You Leap) — C/Java style
    if "key" in data:
        val = data["key"]

    # EAFP (Easier to Ask Forgiveness) — Pythonic style
    try:
        val = data["key"]
    except KeyError:
        val = None

    #? Python prefers EAFP. It's faster when the key usually exists
    #  (no double lookup), and handles race conditions better.


# %% 24 — Context Managers
def demo_context_managers():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  24 — CONTEXT MANAGERS                                             │
    │                                                                     │
    │  Einstein says: A context manager is a promise — "I will set up,  │
    │  you do your work, and I will ALWAYS clean up, even if things     │
    │  explode." The 'with' statement is how you invoke this promise.   │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(24, "CONTEXT MANAGERS")

    #* ── THE PROBLEM 'with' SOLVES ──
    #  Without 'with':
    #    f = open("file.txt")
    #    data = f.read()       ← if this crashes, f.close() never runs!
    #    f.close()
    #
    #  With 'with':
    #    with open("file.txt") as f:
    #        data = f.read()   ← f.close() runs GUARANTEED

    #* ── CLASS-BASED CONTEXT MANAGER ──
    class Timer:
        """Times a block of code."""
        def __enter__(self):
            import time
            self.start = time.perf_counter()
            return self                      # what 'as' binds to

        def __exit__(self, exc_type, exc_val, exc_tb):
            import time
            elapsed = time.perf_counter() - self.start
            print(f"  Block took {elapsed:.4f}s")
            return False                     # False = don't suppress exceptions

    with Timer():
        total = sum(range(1_000_000))
    print(f"  Total: {total:,}")

    #* ── CONTEXTLIB: The easy way ──
    from contextlib import contextmanager

    @contextmanager
    def working_directory(path):
        """Temporarily change directory, always restore."""
        import os
        original = os.getcwd()
        try:
            os.chdir(path)
            print(f"  Changed to: {os.getcwd()}")
            yield                            # ← your 'with' block runs here
        finally:
            os.chdir(original)
            print(f"  Restored to: {os.getcwd()}")

    with working_directory("/tmp"):
        pass  # do work in /tmp

    #* ── MULTIPLE CONTEXT MANAGERS ──
    #  with open("in.txt") as src, open("out.txt", "w") as dst:
    #      dst.write(src.read())

    #* ── SUPPRESS: Ignore specific exceptions ──
    from contextlib import suppress

    with suppress(FileNotFoundError):
        with open("/nonexistent/file") as f:
            data = f.read()
    # No crash — FileNotFoundError is silently caught
    print("\n  suppress() swallowed the FileNotFoundError")


# %% 25 — Custom Exceptions
def demo_custom_exceptions():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  25 — CUSTOM EXCEPTIONS                                            │
    │                                                                     │
    │  Feynman says: Custom exceptions tell the CALLER exactly what      │
    │  went wrong. "InsufficientFunds" is infinitely more useful than   │
    │  "ValueError: something bad happened."                             │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(25, "CUSTOM EXCEPTIONS")

    #* ── BASIC CUSTOM EXCEPTION ──
    class AppError(Exception):
        """Base exception for our application."""
        pass

    class ValidationError(AppError):
        """Data validation failed."""
        def __init__(self, field, message):
            self.field = field
            self.message = message
            super().__init__(f"{field}: {message}")

    class NotFoundError(AppError):
        """Resource not found."""
        def __init__(self, resource, id):
            self.resource = resource
            self.id = id
            super().__init__(f"{resource} #{id} not found")

    #* ── USAGE: Catch by hierarchy ──
    try:
        raise ValidationError("email", "must contain @")
    except ValidationError as e:
        print(f"Validation: {e.field} — {e.message}")
    except AppError as e:
        print(f"App error: {e}")             # catches any AppError subclass

    try:
        raise NotFoundError("User", 42)
    except NotFoundError as e:
        print(f"Not found: {e.resource} #{e.id}")

    #? Pattern: Create a base exception for your app/module.
    #  All custom exceptions inherit from it. Callers can catch
    #  the base to handle ALL your errors, or specific ones.


# ═════════════════════════════════════════════════════════════════════════════
# ██████╗  █████╗ ██████╗ ████████╗    ███████╗
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ╚════██║
# ██████╔╝███████║██████╔╝   ██║          ██╔╝
# ██╔═══╝ ██╔══██║██╔══██╗   ██║         ██╔╝
# ██║     ██║  ██║██║  ██║   ██║         ██║
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝         ╚═╝
#  ITERATORS & GENERATORS — Lazy evaluation
# ═════════════════════════════════════════════════════════════════════════════


# %% 26 — Iterators
def demo_iterators():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  26 — ITERATORS                                                    │
    │                                                                     │
    │  Einstein says: "The iterator protocol is the engine behind every │
    │  for loop in Python. When you write 'for x in thing', Python      │
    │  calls iter(thing) to get an iterator, then next() repeatedly     │
    │  until StopIteration. That's the whole trick."                    │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(26, "ITERATORS")

    #* ── HOW FOR LOOPS ACTUALLY WORK ──
    nums = [10, 20, 30]
    iterator = iter(nums)                    # get the iterator
    print(f"next() → {next(iterator)}")      # 10
    print(f"next() → {next(iterator)}")      # 20
    print(f"next() → {next(iterator)}")      # 30
    # next(iterator) would raise StopIteration

    #* ── CUSTOM ITERATOR ──
    class Countdown:
        def __init__(self, start):
            self.current = start

        def __iter__(self):
            return self                      # iterator returns itself

        def __next__(self):
            if self.current <= 0:
                raise StopIteration
            val = self.current
            self.current -= 1
            return val

    print(f"\nCountdown: {list(Countdown(5))}")

    #* ── KEY INSIGHT: Iterators are single-use ──
    it = iter([1, 2, 3])
    print(f"\nFirst pass:  {list(it)}")       # [1, 2, 3]
    print(f"Second pass: {list(it)}")         # [] — exhausted!

    #? Lists are ITERABLE (can create iterators), but not iterators themselves.
    #  You can iterate over a list multiple times because each for loop
    #  calls iter() to get a FRESH iterator.


# %% 27 — Generators
def demo_generators():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  27 — GENERATORS                                                   │
    │                                                                     │
    │  Feynman says: "A generator is a lazy iterator. It doesn't        │
    │  compute the next value until you ask for it. A list of 1 billion │
    │  items eats all your RAM. A generator uses almost none — it       │
    │  produces one value at a time, on demand."                        │
    │                                                                     │
    │  Any function with 'yield' becomes a generator function.          │
    │  Calling it returns a generator OBJECT (it doesn't run yet).      │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(27, "GENERATORS")

    #* ── BASIC GENERATOR ──
    def countdown(n):
        print("  (Generator started)")
        while n > 0:
            yield n                          # pause here, return value
            n -= 1
        print("  (Generator exhausted)")

    gen = countdown(3)                       # nothing printed yet!
    print(f"Type: {type(gen)}")
    print(f"next: {next(gen)}")              # NOW it runs to first yield → 3
    print(f"next: {next(gen)}")              # resumes, yields 2
    print(f"next: {next(gen)}")              # resumes, yields 1

    #* ── FIBONACCI (infinite generator) ──
    def fibonacci():
        a, b = 0, 1
        while True:                          # infinite! But only produces on demand
            yield a
            a, b = b, a + b

    from itertools import islice
    first_10 = list(islice(fibonacci(), 10))
    print(f"\nFirst 10 fib: {first_10}")

    #* ── GENERATOR EXPRESSION (one-liner) ──
    squares_gen = (x**2 for x in range(10))  # () not [] — lazy!
    print(f"Sum of squares: {sum(squares_gen)}")

    #* ── GENERATOR PIPELINE: Chain generators like Unix pipes ──
    def read_lines(text):
        for line in text.strip().split('\n'):
            yield line.strip()

    def filter_nonempty(lines):
        for line in lines:
            if line:
                yield line

    def to_upper(lines):
        for line in lines:
            yield line.upper()

    text = """
        hello world
        
        python is great
        
        generators rock
    """

    #  Pipeline: read → filter → transform
    pipeline = to_upper(filter_nonempty(read_lines(text)))
    print(f"\nPipeline output: {list(pipeline)}")

    #? Why pipelines? Each generator holds ONE item in memory at a time.
    #  Process a 10GB file with 10KB of RAM.

    #* ── YIELD FROM: Delegate to another generator ──
    def chain(*iterables):
        for it in iterables:
            yield from it                    # same as: for item in it: yield item

    result = list(chain([1, 2], [3, 4], [5, 6]))
    print(f"\nyield from: {result}")


# %% 28 — itertools
def demo_itertools():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  28 — ITERTOOLS                                                    │
    │                                                                     │
    │  Feynman says: "itertools is the Swiss army knife you didn't know │
    │  you had. Before writing a custom loop, check if itertools has    │
    │  a function that does it already."                                │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(28, "ITERTOOLS")

    import itertools as it

    #* ── COUNTING & REPEATING ──
    # count(10)        → 10, 11, 12, ... (infinite)
    # cycle([1,2,3])   → 1, 2, 3, 1, 2, 3, ... (infinite)
    # repeat("x", 3)   → "x", "x", "x"

    #* ── CHAIN: Concatenate iterables ──
    combined = list(it.chain([1, 2], [3, 4], [5, 6]))
    print(f"chain:       {combined}")

    #* ── ISLICE: Slice any iterator ──
    from itertools import islice
    first_5_evens = list(islice(it.count(0, 2), 5))
    print(f"islice:      {first_5_evens}")

    #* ── GROUPBY: Group consecutive elements ──
    data = [("A", 1), ("A", 2), ("B", 3), ("B", 4), ("A", 5)]
    # MUST be sorted by key first!
    data_sorted = sorted(data, key=lambda x: x[0])
    for key, group in it.groupby(data_sorted, key=lambda x: x[0]):
        print(f"  {key}: {list(group)}")

    #* ── PRODUCT: Cartesian product (nested loops in one line) ──
    colors = ["red", "blue"]
    sizes = ["S", "M", "L"]
    combos = list(it.product(colors, sizes))
    print(f"\nproduct:     {combos}")
    # Same as: [(c,s) for c in colors for s in sizes]

    #* ── COMBINATIONS & PERMUTATIONS ──
    items = ["A", "B", "C"]
    print(f"combinations(2): {list(it.combinations(items, 2))}")
    print(f"permutations(2): {list(it.permutations(items, 2))}")

    #* ── ACCUMULATE: Running totals ──
    nums = [1, 2, 3, 4, 5]
    running_sum = list(it.accumulate(nums))
    print(f"\naccumulate:  {running_sum}")

    #* ── STARMAP: map() for functions with multiple args ──
    pairs = [(2, 5), (3, 2), (10, 3)]
    results = list(it.starmap(pow, pairs))
    print(f"starmap(pow): {results}")       # [32, 9, 1000]

    #* ── PAIRWISE (Python 3.10+): Sliding window of 2 ──
    try:
        data = [1, 2, 3, 4, 5]
        pairs = list(it.pairwise(data))
        print(f"pairwise:    {pairs}")
    except AttributeError:
        print("pairwise:    (requires Python 3.10+)")

    #* ── BATCHED (Python 3.12+): Chunk into groups ──
    try:
        data = range(10)
        batches = list(it.batched(data, 3))
        print(f"batched(3):  {batches}")
    except AttributeError:
        print("batched:     (requires Python 3.12+)")


# ═════════════════════════════════════════════════════════════════════════════
# ██████╗  █████╗ ██████╗ ████████╗     █████╗
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ██╔══██╗
# ██████╔╝███████║██████╔╝   ██║       ╚█████╔╝
# ██╔═══╝ ██╔══██║██╔══██╗   ██║       ██╔══██╗
# ██║     ██║  ██║██║  ██║   ██║       ╚█████╔╝
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝        ╚════╝
#  FILE I/O & DATA — Reading and writing the world
# ═════════════════════════════════════════════════════════════════════════════


# %% 29 — File Operations
def demo_files():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  29 — FILE OPERATIONS                                              │
    │                                                                     │
    │  Einstein says: "ALWAYS use 'with' for files. It's not optional.  │
    │  If your code crashes between open() and close(), the file stays  │
    │  open and bad things happen. 'with' makes this impossible."       │
    │                                                                     │
    │  MODES: 'r' read │ 'w' write │ 'a' append │ 'x' create-only     │
    │         Add 'b' for binary: 'rb', 'wb'                            │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(29, "FILE OPERATIONS")

    import tempfile, os

    # Use a temp file so we don't litter the filesystem
    tmpfile = os.path.join(tempfile.gettempdir(), "python_demo.txt")

    #* ── WRITING ──
    with open(tmpfile, 'w') as f:
        f.write("Line 1: Hello, Python!\n")
        f.write("Line 2: Files are easy.\n")
        f.writelines(["Line 3: writelines\n", "Line 4: takes a list\n"])

    #* ── READING: Three ways ──
    # 1. Read entire file as string
    with open(tmpfile, 'r') as f:
        content = f.read()
    print(f"read():\n{content}")

    # 2. Read all lines as a list
    with open(tmpfile, 'r') as f:
        lines = f.readlines()
    print(f"readlines(): {lines}")

    # 3. Iterate line by line (memory efficient for big files)
    with open(tmpfile, 'r') as f:
        for line in f:                       #* best for large files
            print(f"  → {line.strip()}")

    #* ── APPENDING ──
    with open(tmpfile, 'a') as f:
        f.write("Line 5: Appended!\n")

    #* ── READING + WRITING ──
    with open(tmpfile, 'r+') as f:           # r+ = read and write
        content = f.read()
        f.write("Line 6: r+ mode\n")

    # Cleanup
    os.remove(tmpfile)
    print("\n  Temp file cleaned up")


# %% 30 — JSON & CSV
def demo_json_csv():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  30 — JSON & CSV                                                   │
    │                                                                     │
    │  Feynman says: JSON is how programs talk to each other. CSV is    │
    │  how spreadsheets talk to programs. Know both cold.               │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(30, "JSON & CSV")

    import json, csv, io

    #* ── JSON: Python dict ↔ JSON string ──
    data = {
        "name": "Stewart",
        "skills": ["Python", "Supply Chain", "Cybersecurity"],
        "active": True,
        "score": 9.5
    }

    # Serialize: Python → JSON string
    json_str = json.dumps(data, indent=2)
    print(f"json.dumps():\n{json_str}")

    # Deserialize: JSON string → Python
    parsed = json.loads(json_str)
    print(f"\njson.loads() type: {type(parsed).__name__}")
    print(f"Skills: {parsed['skills']}")

    #* ── JSON to/from files ──
    # json.dump(data, open("file.json", "w"), indent=2)  # write
    # data = json.load(open("file.json"))                 # read

    #* ── JSON TYPE MAPPING ──
    # JSON     →  Python
    # object   →  dict
    # array    →  list
    # string   →  str
    # number   →  int/float
    # true     →  True
    # false    →  False
    # null     →  None

    #* ── CSV: Reading and writing ──
    # Writing to a string (use a file path in real code)
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Stewart", 49, "Whitsett"])
    writer.writerow(["Alice", 30, "NYC"])
    csv_text = output.getvalue()
    print(f"\nCSV output:\n{csv_text}")

    # Reading from a string
    reader = csv.reader(io.StringIO(csv_text))
    header = next(reader)                    # first row is header
    for row in reader:
        print(f"  {dict(zip(header, row))}")

    #* ── DICTREADER/DICTWRITER: The pro way ──
    reader = csv.DictReader(io.StringIO(csv_text))
    for row in reader:
        print(f"  DictReader: {row['Name']} from {row['City']}")


# %% 31 — Pathlib
def demo_pathlib():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  31 — PATHLIB                                                      │
    │                                                                     │
    │  Einstein says: "Stop using os.path.join(). pathlib is cleaner,   │
    │  more readable, and works everywhere. It's Python's modern way    │
    │  to handle filesystem paths."                                     │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(31, "PATHLIB")

    from pathlib import Path

    #* ── CREATING PATHS (/ operator!) ──
    home = Path.home()
    project = home / "projects" / "myapp"    # readable path joining!
    config = project / "config.json"

    print(f"Home:    {home}")
    print(f"Project: {project}")
    print(f"Config:  {config}")

    #* ── PATH PROPERTIES ──
    p = Path("/home/stewart/projects/app/main.py")
    print(f"\n.name:    {p.name}")           # main.py
    print(f".stem:    {p.stem}")             # main
    print(f".suffix:  {p.suffix}")           # .py
    print(f".parent:  {p.parent}")           # /home/stewart/projects/app
    print(f".parts:   {p.parts}")            # ('/', 'home', 'stewart', ...)

    #* ── CURRENT DIRECTORY ──
    cwd = Path.cwd()
    print(f"\nCWD: {cwd}")

    #* ── GLOBBING (find files by pattern) ──
    py_files = list(Path(".").glob("*.py"))
    print(f"Python files here: {py_files[:5]}")

    # Recursive glob
    # all_py = list(Path(".").rglob("*.py"))

    #* ── FILE OPERATIONS (no more open() for simple tasks) ──
    import tempfile
    tmp = Path(tempfile.gettempdir()) / "pathlib_demo.txt"

    tmp.write_text("Hello from pathlib!")     # write entire file
    content = tmp.read_text()                 # read entire file
    print(f"\nread_text(): {content}")

    print(f".exists():  {tmp.exists()}")
    print(f".is_file(): {tmp.is_file()}")
    print(f".stat():    {tmp.stat().st_size} bytes")

    tmp.unlink()                              # delete file

    #* ── WHY PATHLIB > os.path ──
    #  os.path way:  os.path.join(os.path.expanduser("~"), "file.txt")
    #  pathlib way:  Path.home() / "file.txt"
    #  Which would you rather read?


# ═════════════════════════════════════════════════════════════════════════════
# ██████╗  █████╗ ██████╗ ████████╗     █████╗
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ██╔══██╗
# ██████╔╝███████║██████╔╝   ██║       ╚██████║
# ██╔═══╝ ██╔══██║██╔══██╗   ██║        ╚═══██║
# ██║     ██║  ██║██║  ██║   ██║       █████╔╝
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚════╝
#  TEXT MASTERY — Regex, formatting, dates
# ═════════════════════════════════════════════════════════════════════════════


# %% 32 — Regex
def demo_regex():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  32 — REGULAR EXPRESSIONS                                          │
    │                                                                     │
    │  Feynman says: "Regex is a tiny language for pattern matching.    │
    │  It's cryptic at first, but once it clicks, you'll use it        │
    │  everywhere. Start simple. Test at regex101.com. Build up."       │
    │                                                                     │
    │  TIP: Always use r"raw strings" for regex patterns.              │
    │  This prevents Python from interpreting \\ as escape sequences.    │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(32, "REGEX")

    import re

    #* ── CHEAT SHEET ──
    #  .        any character (except newline)
    #  \d       digit [0-9]
    #  \w       word char [a-zA-Z0-9_]
    #  \s       whitespace [ \t\n\r]
    #  \D \W \S negation of above
    #  ^        start of string
    #  $        end of string
    #  *        0 or more
    #  +        1 or more
    #  ?        0 or 1
    #  {n,m}    n to m occurrences
    #  []       character class: [aeiou], [0-9], [^abc] (negated)
    #  ()       capturing group
    #  |        OR
    #  (?:...)  non-capturing group

    text = "Contact stewart@example.com or call 336-555-1234"

    #* ── SEARCH: Find first match ──
    email = re.search(r'[\w.-]+@[\w.-]+\.\w+', text)
    if email:
        print(f"Email found: {email.group()}")

    #* ── FINDALL: Find all matches ──
    phones = re.findall(r'\d{3}-\d{3}-\d{4}', text)
    print(f"Phones: {phones}")

    #* ── SUB: Search and replace ──
    censored = re.sub(r'\d', 'X', text)
    print(f"Censored: {censored}")

    #* ── GROUPS: Capture parts of the match ──
    pattern = r'(\w+)@(\w+)\.(\w+)'
    match = re.search(pattern, text)
    if match:
        print(f"\nFull match:  {match.group(0)}")
        print(f"Username:    {match.group(1)}")
        print(f"Domain:      {match.group(2)}")
        print(f"TLD:         {match.group(3)}")
        print(f"All groups:  {match.groups()}")

    #* ── NAMED GROUPS ──
    pattern = r'(?P<user>\w+)@(?P<domain>\w+)\.(?P<tld>\w+)'
    match = re.search(pattern, text)
    if match:
        print(f"\nNamed: {match.group('user')}@{match.group('domain')}")
        print(f"groupdict(): {match.groupdict()}")

    #* ── COMPILE: Pre-compile for repeated use ──
    email_re = re.compile(r'[\w.-]+@[\w.-]+\.\w+')
    results = email_re.findall(text)
    print(f"\nCompiled findall: {results}")

    #* ── SPLIT with regex ──
    parts = re.split(r'[,;|]', "apple,banana;cherry|date")
    print(f"Split: {parts}")

    #* ── COMMON PATTERNS (bookmark these) ──
    patterns = {
        "email":    r'[\w.-]+@[\w.-]+\.\w+',
        "phone":    r'\d{3}[-.]?\d{3}[-.]?\d{4}',
        "url":      r'https?://[\w.-]+(?:/[\w.-]*)*',
        "ip":       r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b',
        "date":     r'\d{4}-\d{2}-\d{2}',
        "hex_color": r'#[0-9a-fA-F]{6}',
    }
    print(f"\nPattern library: {list(patterns.keys())}")


# %% 33 — String Formatting
def demo_formatting():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  33 — STRING FORMATTING DEEP DIVE                                  │
    │                                                                     │
    │  Einstein says: "Make things as simple as possible, but not       │
    │  simpler." f-strings do 95% of what you need. But know the        │
    │  format spec mini-language for the other 5%.                      │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(33, "STRING FORMATTING")

    #* ── f-STRING FORMAT SPEC: {value:spec} ──
    #  The spec is:  [[fill]align][sign][#][0][width][grouping][.precision][type]

    n = 42
    pi = 3.14159265
    big = 1234567.89

    #* ── WIDTH & ALIGNMENT ──
    print("Width & Alignment:")
    print(f"  {'left':<20}|")                # left-align in 20 chars
    print(f"  {'center':^20}|")              # center in 20 chars
    print(f"  {'right':>20}|")               # right-align in 20 chars
    print(f"  {'padded':*^20}|")             # fill with *

    #* ── NUMBERS ──
    print(f"\nNumbers:")
    print(f"  Integer:     {n:10d}")         # right-aligned int
    print(f"  Zero-padded: {n:010d}")        # leading zeros
    print(f"  Plus sign:   {n:+d}")          # always show sign
    print(f"  Binary:      {n:b}")           # binary
    print(f"  Hex:         {n:x}")           # hexadecimal
    print(f"  Octal:       {n:o}")           # octal

    #* ── FLOATS ──
    print(f"\nFloats:")
    print(f"  Default:     {pi}")
    print(f"  2 decimals:  {pi:.2f}")
    print(f"  Scientific:  {pi:.2e}")
    print(f"  Percentage:  {0.856:.1%}")     # 85.6%
    print(f"  Comma sep:   {big:,.2f}")      # 1,234,567.89

    #* ── DATES (format directly in f-strings!) ──
    from datetime import datetime
    now = datetime.now()
    print(f"\nDates:")
    print(f"  ISO:   {now:%Y-%m-%d}")
    print(f"  Human: {now:%B %d, %Y}")
    print(f"  Time:  {now:%I:%M %p}")

    #* ── TABLE FORMATTING ──
    data = [("Python", 3.12, "2024"), ("Java", 21, "2023"), ("Rust", 1.75, "2024")]
    print(f"\n  {'Language':<12} {'Version':>8} {'Year':>6}")
    print(f"  {'─'*12} {'─'*8} {'─'*6}")
    for lang, ver, year in data:
        print(f"  {lang:<12} {ver:>8.2f} {year:>6}")


# %% 34 — Datetime
def demo_datetime():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  34 — DATETIME                                                     │
    │                                                                     │
    │  Feynman says: "Time is simple until you add timezones. Then      │
    │  it's the hardest problem in computer science. Always store       │
    │  UTC, convert to local only for display."                         │
    │                                                                     │
    │  MNEMONICS:                                                        │
    │    strftime = "string FORMAT time"  → datetime to string          │
    │    strptime = "string PARSE time"   → string to datetime          │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(34, "DATETIME")

    from datetime import datetime, date, time, timedelta, timezone

    #* ── CREATING ──
    now = datetime.now()
    today = date.today()
    specific = datetime(2026, 3, 13, 9, 30, 0)
    print(f"now:      {now}")
    print(f"today:    {today}")
    print(f"specific: {specific}")

    #* ── FORMATTING (datetime → string) ──
    # strftime = "string FORMAT time"
    print(f"\nFormatting:")
    print(f"  ISO:      {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Human:    {now.strftime('%B %d, %Y at %I:%M %p')}")
    print(f"  Compact:  {now.strftime('%m/%d/%y')}")

    #  %Y  4-digit year    %m  month 01-12    %d  day 01-31
    #  %H  hour 00-23      %M  minute 00-59   %S  second 00-59
    #  %I  hour 01-12      %p  AM/PM          %B  full month name
    #  %A  full day name   %a  abbreviated     %b  abbreviated month

    #* ── PARSING (string → datetime) ──
    # strptime = "string PARSE time"
    parsed = datetime.strptime("2026-03-13", "%Y-%m-%d")
    print(f"\nParsed: {parsed}")

    #* ── TIME ARITHMETIC ──
    tomorrow = now + timedelta(days=1)
    next_week = now + timedelta(weeks=1)
    in_2_hours = now + timedelta(hours=2)
    print(f"\nTomorrow:   {tomorrow.date()}")
    print(f"Next week:  {next_week.date()}")
    print(f"+2 hours:   {in_2_hours.strftime('%I:%M %p')}")

    # Difference between dates
    new_years = datetime(2027, 1, 1)
    delta = new_years - now
    print(f"\nDays until 2027: {delta.days}")
    print(f"Total seconds:   {delta.total_seconds():,.0f}")

    #* ── TIMEZONE-AWARE DATETIMES ──
    utc_now = datetime.now(timezone.utc)
    eastern = timezone(timedelta(hours=-5))
    eastern_now = utc_now.astimezone(eastern)
    print(f"\nUTC:     {utc_now.strftime('%H:%M %Z')}")
    print(f"Eastern: {eastern_now.strftime('%H:%M %Z')}")

    #? For production timezone handling, use the 'zoneinfo' module (Python 3.9+)
    #  or the third-party 'pytz' library.

    #* ── USEFUL PATTERNS ──
    # Age calculation
    birth = date(1977, 1, 1)
    age = (today - birth).days // 365
    print(f"\nAge from 1977: ~{age} years")

    # ISO format (universal exchange format)
    print(f"ISO: {now.isoformat()}")


# ═════════════════════════════════════════════════════════════════════════════
# ██████╗  █████╗ ██████╗ ████████╗    ██╗ ██████╗
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ██║██╔═══██╗
# ██████╔╝███████║██████╔╝   ██║       ██║██║   ██║
# ██╔═══╝ ██╔══██║██╔══██╗   ██║       ██║██║   ██║
# ██║     ██║  ██║██║  ██║   ██║       ██║╚██████╔╝
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚═╝ ╚═════╝
#  STANDARD LIBRARY POWER TOOLS
# ═════════════════════════════════════════════════════════════════════════════


# %% 35 — Collections
def demo_collections():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  35 — COLLECTIONS MODULE                                           │
    │                                                                     │
    │  Einstein says: The collections module has specialized containers  │
    │  that solve common problems more elegantly than basic dicts/lists. │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(35, "COLLECTIONS")

    from collections import deque, OrderedDict, ChainMap

    #* ── DEQUE: Double-ended queue ──
    #  O(1) append/pop from BOTH ends (list is O(n) for left operations)
    dq = deque([1, 2, 3])
    dq.appendleft(0)                         # O(1) — list.insert(0,x) is O(n)
    dq.append(4)                             # O(1)
    dq.popleft()                             # O(1) — list.pop(0) is O(n)
    print(f"deque: {list(dq)}")

    # Bounded deque — automatically drops oldest
    recent = deque(maxlen=3)
    for i in range(5):
        recent.append(i)
    print(f"Bounded deque: {list(recent)}")  # [2, 3, 4]

    # Rotate
    dq = deque([1, 2, 3, 4, 5])
    dq.rotate(2)                             # rotate right by 2
    print(f"Rotated: {list(dq)}")

    #* ── CHAINMAP: Stack of dicts (config layering) ──
    defaults = {"theme": "light", "lang": "en", "debug": False}
    user_prefs = {"theme": "dark", "lang": "zh"}
    cli_args = {"debug": True}

    config = ChainMap(cli_args, user_prefs, defaults)  # first dict wins
    print(f"\nChainMap:")
    print(f"  theme: {config['theme']}")     # dark (from user_prefs)
    print(f"  lang:  {config['lang']}")      # zh (from user_prefs)
    print(f"  debug: {config['debug']}")     # True (from cli_args)

    #? ChainMap doesn't merge — it searches dicts in order.
    #  Perfect for configuration layering: CLI > user > defaults.


# %% 36 — OS & Subprocess
def demo_os():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  36 — OS & SUBPROCESS                                              │
    │                                                                     │
    │  Feynman says: Python can talk to your operating system. os gives │
    │  you file/directory operations. subprocess runs external commands. │
    │  Prefer pathlib over os.path, and subprocess over os.system.      │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(36, "OS & SUBPROCESS")

    import os
    import subprocess

    #* ── ENVIRONMENT VARIABLES ──
    home = os.environ.get("HOME", "unknown")
    path = os.environ.get("PATH", "")
    print(f"HOME: {home}")
    print(f"PATH dirs: {len(path.split(':'))}")

    #* ── OS MODULE ESSENTIALS ──
    print(f"\nos.getcwd():    {os.getcwd()}")
    print(f"os.cpu_count(): {os.cpu_count()}")
    print(f"os.getpid():    {os.getpid()}")

    #* ── SUBPROCESS: Run external commands ──
    result = subprocess.run(
        ["echo", "Hello from subprocess"],
        capture_output=True,
        text=True
    )
    print(f"\nsubprocess output: {result.stdout.strip()}")
    print(f"Return code: {result.returncode}")

    # Get command output as string
    output = subprocess.run(
        ["python3", "--version"],
        capture_output=True,
        text=True
    )
    print(f"Python version: {output.stdout.strip()}")

    #! NEVER use shell=True with user input — security risk (injection)
    #  subprocess.run(f"rm {user_input}", shell=True)  ← DANGEROUS
    #  subprocess.run(["rm", user_input])               ← SAFE


# %% 37 — Typing & Type Hints
def demo_typing():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  37 — TYPING & TYPE HINTS                                          │
    │                                                                     │
    │  Einstein says: Type hints are documentation that tools can        │
    │  verify. Python won't enforce them at runtime, but your IDE will  │
    │  catch bugs before you even run the code.                         │
    │                                                                     │
    │  TL;DR: Add type hints to function signatures. Skip variable      │
    │  annotations unless it helps readability.                          │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(37, "TYPING & TYPE HINTS")

    from typing import Optional, Union

    #* ── BASIC TYPE HINTS ──
    def greet(name: str, times: int = 1) -> str:
        """Type hints on params and return value."""
        return (f"Hello, {name}! " * times).strip()

    print(greet("Stewart", 2))

    #* ── COLLECTION TYPES (Python 3.9+ can use built-in names) ──
    def process(
        items: list[str],                    # list of strings
        config: dict[str, int],              # dict with str keys, int values
        ids: set[int],                       # set of ints
        point: tuple[float, float],          # exactly 2 floats
    ) -> list[str]:
        return [item.upper() for item in items]

    #* ── OPTIONAL: Might be None ──
    def find_user(id: int) -> Optional[str]:   # same as str | None
        users = {1: "Stewart", 2: "Alice"}
        return users.get(id)

    #* ── UNION: Multiple possible types ──
    def double(x: int | float) -> int | float:    # Python 3.10+
        return x * 2

    # Pre-3.10: Union[int, float]

    #* ── CALLABLE: Function types ──
    from typing import Callable

    def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
        return func(a, b)

    result = apply(lambda x, y: x + y, 3, 4)
    print(f"\napply result: {result}")

    #* ── TYPE ALIASES ──
    UserId = int
    UserMap = dict[UserId, str]

    users: UserMap = {1: "Stewart", 2: "Alice"}
    print(f"Users: {users}")

    #* ── POWER USER: TypeVar for generics ──
    from typing import TypeVar
    T = TypeVar("T")

    def first(items: list[T]) -> T:          # returns same type as list contains
        return items[0]

    print(f"\nfirst(['a','b']) → {first(['a','b'])}")
    print(f"first([1,2,3])   → {first([1, 2, 3])}")

    #? Type hints are NEVER enforced at runtime. Use mypy or pyright
    #  to check them: `mypy script.py` or let VS Code's Pylance do it.


# ═════════════════════════════════════════════════════════════════════════════
# ██████╗  █████╗ ██████╗ ████████╗    ██╗  ██╗
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ██║ ██╔╝
# ██████╔╝███████║██████╔╝   ██║       █████╔╝
# ██╔═══╝ ██╔══██║██╔══██╗   ██║       ██╔═██╗
# ██║     ██║  ██║██║  ██║   ██║       ██║  ██╗
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═╝
#  PYTHONIC PATTERNS — The edge
# ═════════════════════════════════════════════════════════════════════════════


# %% 38 — Idioms
def demo_idioms():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  38 — PYTHONIC IDIOMS                                              │
    │                                                                     │
    │  Feynman says: "These are the patterns that separate someone who  │
    │  WRITES Python from someone who THINKS in Python."                │
    │                                                                     │
    │  Every pattern here replaces 3-5 lines of amateur code with 1    │
    │  line of clear, professional Python. This IS the competitive     │
    │  edge.                                                             │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(38, "PYTHONIC IDIOMS")

    print("── Swap variables ──")
    a, b = 1, 2
    a, b = b, a                              # no temp variable
    print(f"  a={a}, b={b}")

    print("\n── Conditional assignment ──")
    x = None
    result = x or "default"                  # if x is falsy, use default
    print(f"  {result}")

    print("\n── Walrus operator := (Python 3.8+) ──")
    # Assign AND use in one expression
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if (n := len(data)) > 5:                 # assign n, then check it
        print(f"  List has {n} items (that's a lot)")

    # In list comprehensions
    results = [y for x in range(10) if (y := x**2) > 20]
    print(f"  Squares > 20: {results}")

    print("\n── Chained comparison ──")
    age = 25
    if 18 <= age < 65:
        print(f"  {age} is working age")

    print("\n── Multiple assignment ──")
    x = y = z = 0                            # all point to same 0
    a, b, c = 1, 2, 3                        # tuple unpacking

    print("\n── Truthiness shortcuts ──")
    items = [1, 2, 3]
    if items:                                # DON'T: if len(items) > 0
        print(f"  Has {len(items)} items")

    name = ""
    greeting = name or "Anonymous"            # DON'T: if name: greeting = name
    print(f"  Greeting: {greeting}")

    print("\n── Dictionary dispatch (replacing if/elif chains) ──")
    def handle_add(a, b): return a + b
    def handle_sub(a, b): return a - b
    def handle_mul(a, b): return a * b

    ops = {"add": handle_add, "sub": handle_sub, "mul": handle_mul}
    result = ops.get("mul", lambda a, b: None)(6, 7)
    print(f"  dispatch('mul', 6, 7) = {result}")

    print("\n── EAFP: Try first, apologize later ──")
    config = {"debug": True}
    # LBYL (Look Before You Leap):
    #   if "debug" in config: debug = config["debug"]
    # EAFP (Easier to Ask Forgiveness):
    try:
        debug = config["debug"]
    except KeyError:
        debug = False
    print(f"  debug = {debug}")

    print("\n── Enumerate is better than range(len()) ──")
    items = ["a", "b", "c"]
    # BAD:  for i in range(len(items)): print(i, items[i])
    # GOOD:
    for i, item in enumerate(items):
        print(f"  [{i}] {item}")

    print("\n── Zip to build dicts ──")
    keys = ["name", "age", "city"]
    values = ["Stewart", 49, "Whitsett"]
    d = dict(zip(keys, values))
    print(f"  {d}")

    print("\n── Underscore for unused variables ──")
    for _ in range(3):                       # _ signals "I don't use this"
        pass

    coords = (10, 20, 30)
    x, _, z = coords                         # ignore y
    print(f"  x={x}, z={z}")


# %% 39 — Performance
def demo_performance():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  39 — PERFORMANCE TIPS                                             │
    │                                                                     │
    │  Einstein says: "Premature optimization is the root of all evil"  │
    │  (actually Knuth). But knowing what's fast and what's slow lets   │
    │  you write naturally efficient code from the start.               │
    │                                                                     │
    │  RULE: Make it work, make it right, THEN make it fast.            │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(39, "PERFORMANCE")

    import time

    def benchmark(label, func, *args):
        start = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - start
        print(f"  {label:<35} {elapsed*1000:.2f}ms")
        return result

    N = 100_000

    #* ── STRING CONCATENATION ──
    print("String building:")
    # SLOW: string concatenation in a loop (creates new string each time)
    benchmark("  += in loop", lambda: ''.join(str(i) for i in range(N)))
    # FAST: join (allocates once)
    benchmark("  ''.join() ", lambda: ''.join(str(i) for i in range(N)))

    #* ── LIST BUILDING ──
    print("\nList building:")
    benchmark("  append loop",
              lambda: (lambda: (l := [], [l.append(i) for i in range(N)], l[0]))()[-1])
    benchmark("  comprehension", lambda: [i for i in range(N)])

    #* ── MEMBERSHIP TESTING ──
    print("\nMembership test (is X in collection?):")
    big_list = list(range(N))
    big_set = set(big_list)
    target = N - 1                           # worst case for list

    benchmark(f"  list (scan {N:,} items)", lambda: target in big_list)
    benchmark(f"  set  (hash lookup)     ", lambda: target in big_set)

    #* ── DICT vs OBJECT ATTRIBUTE ACCESS ──
    print("\nLookup:")
    d = {"key": "value"}
    benchmark("  dict['key']", lambda: [d["key"] for _ in range(N)])

    #* ── KEY TAKEAWAYS ──
    print("""
  PERFORMANCE RULES OF THUMB:
  ├─ Use list comprehensions over loops
  ├─ Use sets for membership testing
  ├─ Use ''.join() for string building
  ├─ Use dict for O(1) lookups
  ├─ Use generators for large datasets
  ├─ Use collections.deque for queue operations
  ├─ Use functools.lru_cache for repeated calculations
  └─ Profile before optimizing: python -m cProfile script.py""")


# %% 40 — Gotchas
def demo_gotchas():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  40 — PYTHON GOTCHAS                                               │
    │                                                                     │
    │  Feynman says: "The first principle is that you must not fool     │
    │  yourself." These are the traps that bite everyone at least once. │
    │  Learn them now, save hours of debugging later.                   │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(40, "GOTCHAS")

    #* ── GOTCHA 1: Mutable default arguments ──
    print("1. Mutable default arguments:")
    def append_to(item, target=[]):          #! BUG: [] is created ONCE
        target.append(item)
        return target

    print(f"   Call 1: {append_to('a')}")    # ['a']
    print(f"   Call 2: {append_to('b')}")    # ['a', 'b'] ← NOT ['b']!

    def append_to_fixed(item, target=None):  #* FIX: use None
        if target is None:
            target = []
        target.append(item)
        return target

    #* ── GOTCHA 2: Late binding closures ──
    print("\n2. Late binding closures:")
    funcs = [lambda: i for i in range(3)]
    print(f"   Expected [0,1,2]: {[f() for f in funcs]}")  # [2,2,2]!

    funcs = [lambda i=i: i for i in range(3)]  #* FIX: capture with default arg
    print(f"   Fixed [0,1,2]:    {[f() for f in funcs]}")

    #* ── GOTCHA 3: Integer identity ──
    print("\n3. Integer caching:")
    a = 256
    b = 256
    print(f"   256 is 256: {a is b}")        # True (Python caches -5 to 256)
    a = 257
    b = 257
    print(f"   257 is 257: {a is b}")        # False (or True in some contexts)
    print("   → Always use == for value comparison, 'is' only for None")

    #* ── GOTCHA 4: Shallow vs deep copy ──
    print("\n4. Shallow copy surprise:")
    original = [[1, 2], [3, 4]]
    shallow = original.copy()
    shallow[0].append(99)
    print(f"   Original after shallow copy edit: {original}")  # [[1,2,99],[3,4]]

    #* ── GOTCHA 5: String immutability ──
    print("\n5. Strings are immutable:")
    s = "hello"
    # s[0] = 'H'                             #! TypeError
    s = 'H' + s[1:]                          # creates a NEW string
    print(f"   'Fixed': {s}")

    #* ── GOTCHA 6: Modifying list while iterating ──
    print("\n6. Modifying while iterating:")
    nums = [1, 2, 3, 4, 5]
    # for n in nums:                         #! Skips items or infinite loop
    #     if n % 2 == 0: nums.remove(n)
    nums = [n for n in nums if n % 2 != 0]   #* FIX: create new list
    print(f"   Odds: {nums}")

    #* ── GOTCHA 7: == vs is ──
    print("\n7. == vs is:")
    a = [1, 2, 3]
    b = [1, 2, 3]
    print(f"   a == b: {a == b}")            # True (same value)
    print(f"   a is b: {a is b}")            # False (different objects)

    #* ── GOTCHA 8: Float precision ──
    print("\n8. Float precision:")
    print(f"   0.1 + 0.2 = {0.1 + 0.2}")    # 0.30000000000000004
    print(f"   0.1 + 0.2 == 0.3: {0.1 + 0.2 == 0.3}")  # False!
    import math
    print(f"   isclose: {math.isclose(0.1 + 0.2, 0.3)}")  # True


# ═════════════════════════════════════════════════════════════════════════════
# ██████╗  █████╗ ██████╗ ████████╗    ██╗██████╗
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ██║╚════██╗
# ██████╔╝███████║██████╔╝   ██║       ██║ █████╔╝
# ██╔═══╝ ██╔══██║██╔══██╗   ██║       ██║██╔═══╝
# ██║     ██║  ██║██║  ██║   ██║       ██║███████╗
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚═╝╚══════╝
#  CHEAT SHEET — Quick reference
# ═════════════════════════════════════════════════════════════════════════════


# %% 41 — Quick Reference
def demo_cheatsheet():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  41 — QUICK REFERENCE CHEAT SHEET                                  │
    │                                                                     │
    │  One-liners and patterns you'll use daily. Print this out.        │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(41, "CHEAT SHEET")

    print("""
  ┌─────────────────────────────────────────────────────────────────────┐
  │  STRINGS                                                            │
  ├─────────────────────────────────────────────────────────────────────┤
  │  s.strip()              remove whitespace from edges                │
  │  s.split(",")           split into list                             │
  │  ",".join(list)         join list into string                       │
  │  s.replace("a", "b")   replace all occurrences                     │
  │  s.startswith("x")     check prefix                                 │
  │  f"{val:.2f}"           format float to 2 decimals                  │
  │  f"{val:,}"             format with comma separator                 │
  │  s[::-1]                reverse a string                            │
  ├─────────────────────────────────────────────────────────────────────┤
  │  LISTS                                                              │
  ├─────────────────────────────────────────────────────────────────────┤
  │  [x for x in items if cond]     comprehension                       │
  │  sorted(items, key=func)        sort by custom key                  │
  │  list(set(items))               deduplicate                         │
  │  items[-1]                      last element                        │
  │  items[::2]                     every other element                 │
  │  items[::-1]                    reversed copy                       │
  │  any(cond for x in items)       any match?                          │
  │  all(cond for x in items)       all match?                          │
  ├─────────────────────────────────────────────────────────────────────┤
  │  DICTS                                                              │
  ├─────────────────────────────────────────────────────────────────────┤
  │  d.get(key, default)            safe access                         │
  │  d.setdefault(key, [])          get or create                       │
  │  d | other                      merge (3.9+)                        │
  │  {k: v for k, v in items}      comprehension                       │
  │  for k, v in d.items()         iterate pairs                        │
  │  dict(zip(keys, values))        build from two lists                │
  ├─────────────────────────────────────────────────────────────────────┤
  │  FILES                                                              │
  ├─────────────────────────────────────────────────────────────────────┤
  │  Path("file").read_text()       read entire file                    │
  │  Path("file").write_text(s)     write entire file                   │
  │  with open(f) as fh:            context-managed file                │
  │  json.dumps(obj, indent=2)      Python → JSON                      │
  │  json.loads(string)             JSON → Python                       │
  ├─────────────────────────────────────────────────────────────────────┤
  │  ONE-LINERS                                                         │
  ├─────────────────────────────────────────────────────────────────────┤
  │  a, b = b, a                    swap                                │
  │  x = val or default             default if falsy                    │
  │  result if cond else other      ternary                             │
  │  [*list1, *list2]               merge lists                         │
  │  {**dict1, **dict2}             merge dicts                         │
  │  first, *rest = items           head/tail split                     │
  │  _ = unused_value               signal unused variable              │
  └─────────────────────────────────────────────────────────────────────┘
    """)




# ═══════════════════════════════════════════════════════════════════════════════
# ██████╗  █████╗ ██████╗ ████████╗    ██╗██████╗
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ██║╚════██╗
# ██████╔╝███████║██████╔╝   ██║       ██║ █████╔╝
# ██╔═══╝ ██╔══██║██╔══██╗   ██║       ██║██╔═══╝
# ██║     ██║  ██║██║  ██║   ██║       ██║███████╗
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚═╝╚══════╝
#  REFERENCE TABLES — Ctrl+F heaven
# ═══════════════════════════════════════════════════════════════════════════════


# %% 41 — Operator Precedence
def demo_operator_precedence():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  41 — OPERATOR PRECEDENCE TABLE                                    │
    │                                                                     │
    │  Feynman says: "When two operators fight over an operand, the one  │
    │  with higher precedence wins. When in doubt, use parentheses —    │
    │  explicit is better than implicit."                                │
    │                                                                     │
    │  TABLE: Top = lowest precedence (loosest), Bottom = highest        │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(41, "OPERATOR PRECEDENCE")

    print("""
  ┌───────────────────────────────────────────────────────────────────────┐
  │  OPERATOR              │ DESCRIPTION              │ ASSOC.  │        │
  ├───────────────────────────────────────────────────────────────────────┤
  │  := (walrus)           │ Assignment expression     │ RIGHT  │ LOWEST │
  │  lambda                │ Lambda expression         │ ─      │        │
  │  if – else             │ Ternary conditional       │ ─      │        │
  │  or                    │ Boolean OR                │ LEFT   │        │
  │  and                   │ Boolean AND               │ LEFT   │        │
  │  not x                 │ Boolean NOT               │ ─      │        │
  │  in, not in, is,       │ Membership, identity,     │ LEFT   │        │
  │    is not, <, <=, >,   │   comparison              │        │        │
  │    >=, !=, ==          │                           │        │        │
  │  |                     │ Bitwise OR / set union    │ LEFT   │        │
  │  ^                     │ Bitwise XOR / set sym.    │ LEFT   │        │
  │  &                     │ Bitwise AND / set inter   │ LEFT   │        │
  │  <<, >>                │ Bit shifts                │ LEFT   │        │
  │  +, -                  │ Add, subtract             │ LEFT   │        │
  │  *, /, //, %, @        │ Mul, div, floor, mod      │ LEFT   │        │
  │  +x, -x, ~x           │ Unary plus, neg, invert   │ ─      │        │
  │  **                    │ Exponentiation            │ RIGHT  │        │
  │  await x               │ Await expression          │ ─      │        │
  │  x[i], x[i:j],        │ Index, slice, call,       │ LEFT   │ HIGHEST│
  │    x(...), x.attr      │   attribute access        │        │        │
  │  (expr), [expr],       │ Tuple, list, dict, set    │ ─      │        │
  │    {k:v}, {expr}       │   displays                │        │        │
  └───────────────────────────────────────────────────────────────────────┘
    """)

    #* ── WHY THIS MATTERS ──
    print("  Precedence gotchas:")
    print(f"    2 ** 3 ** 2   = {2 ** 3 ** 2}")       # 512 (right-assoc: 2^(3^2)=2^9)
    print(f"    (2 ** 3) ** 2 = {(2 ** 3) ** 2}")     # 64
    print(f"    -1 ** 2       = {-1 ** 2}")            #! -1 (** binds tighter than unary -)
    print(f"    (-1) ** 2     = {(-1) ** 2}")          # 1
    print(f"    True or True and False = {True or True and False}")  # True ('and' before 'or')
    print(f"    not 1 in [1,2] = {not 1 in [1, 2]}")   # False ('in' before 'not')

    #* RULE OF THUMB: If you have to think about precedence, add parens.
    #  Readable code > clever code. Always.


# %% 42 — Built-in Functions
def demo_builtins():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  42 — BUILT-IN FUNCTIONS REFERENCE                                 │
    │                                                                     │
    │  Einstein says: "These are Python's batteries — 70+ functions you  │
    │  get without importing anything. The ones marked * are the ones    │
    │  you'll use daily. The rest, you'll reach for when you need them." │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(42, "BUILT-IN FUNCTIONS")

    print("""
  ── DATA INSPECTION ("What is this?") ───────────────────────────────────
  * type(x)           → type of x
  * isinstance(x, T)  → True if x is of type T (handles inheritance)
    id(x)             → memory address (identity)
  * len(x)            → length of container
  * dir(x)            → list all attributes/methods
    vars(x)           → x.__dict__ (instance attributes)
    help(x)           → interactive docs (use in REPL)
    hasattr(x, 'y')   → does x have attribute 'y'?
    getattr(x, 'y')   → get attribute, with optional default
    callable(x)       → can you call x() ?

  ── TYPE CONVERSION ("Make this into that") ─────────────────────────────
  * int(x)            → convert to integer
  * float(x)          → convert to float
  * str(x)            → convert to string
  * bool(x)           → convert to boolean
  * list(x)           → convert iterable to list
  * tuple(x)          → convert iterable to tuple
  * dict(x)           → create dict from pairs
  * set(x)            → convert iterable to set
    frozenset(x)      → immutable set
    bytes(x)          → immutable byte sequence
    bytearray(x)      → mutable byte sequence
    chr(n)            → Unicode char from int (chr(65)→'A')
    ord(c)            → int from Unicode char (ord('A')→65)
    bin(n)            → binary string ('0b1010')
    oct(n)            → octal string ('0o12')
    hex(n)            → hex string ('0xff')
    complex(r, i)     → complex number

  ── MATH & NUMBERS ──────────────────────────────────────────────────────
  * abs(x)            → absolute value
  * max(iterable)     → largest item (key= for custom)
  * min(iterable)     → smallest item (key= for custom)
  * sum(iterable)     → total
  * round(x, n)       → round to n decimal places
    pow(x, y[, mod])  → x**y (with optional modulo)
    divmod(a, b)      → (quotient, remainder)

  ── ITERABLES ("Transform sequences") ───────────────────────────────────
  * sorted(x)         → new sorted list (key=, reverse=)
  * reversed(x)       → reverse iterator
  * enumerate(x)      → (index, value) pairs
  * zip(a, b)         → parallel pairs, stops at shortest
  * map(fn, x)        → apply fn to each element
  * filter(fn, x)     → keep elements where fn returns True
  * range(start,stop,step) → integer sequence
  * any(iterable)     → True if ANY element is truthy
  * all(iterable)     → True if ALL elements are truthy
    next(iterator)    → get next item (or default)
    iter(x)           → get iterator from iterable
    slice(start,stop) → slice object for indexing

  ── I/O & DISPLAY ───────────────────────────────────────────────────────
  * print(x, sep, end, file)  → output to console/file
  * input(prompt)     → read string from user
  * open(path, mode)  → file object
    format(x, spec)   → format x with spec string
    repr(x)           → developer-friendly string
    ascii(x)          → repr but escapes non-ASCII

  ── OOP & CLASSES ───────────────────────────────────────────────────────
  * super()           → parent class proxy
    property(fget)    → managed attribute (prefer @property)
    classmethod(fn)   → method bound to class (prefer decorator)
    staticmethod(fn)  → plain function in class namespace
    issubclass(A, B)  → is A a subclass of B?
    object()          → base object (root of all classes)

  ── ADVANCED / METAPROGRAMMING ──────────────────────────────────────────
    eval(expr)        → evaluate string as expression
    exec(code)        → execute string as code  ━━ DANGER ━━
    compile(src)      → compile to code object
    globals()         → global namespace dict
    locals()          → local namespace dict
    __import__(name)  → import by string name (prefer importlib)
    """)

    #* ── LIVE EXAMPLES of the ones people forget ──
    print("  Live examples:")
    print(f"    chr(65)={chr(65)}  ord('A')={ord('A')}")
    print(f"    divmod(17,5)={divmod(17,5)}")
    print(f"    any([0,0,1])={any([0,0,1])}  all([1,1,0])={all([1,1,0])}")
    print(f"    callable(print)={callable(print)}  callable(42)={callable(42)}")
    print(f"    hash('hello')={hash('hello')}")


# %% 43 — Exception Hierarchy
def demo_exception_tree():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  43 — EXCEPTION HIERARCHY                                          │
    │                                                                     │
    │  Feynman says: "Knowing the family tree of exceptions tells you    │
    │  what to catch. Catching too high = swallowing bugs. Catching      │
    │  too specific = missing related errors."                           │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(43, "EXCEPTION HIERARCHY")

    print("""
  BaseException                          ← NEVER catch this
  ├── SystemExit                          raise SystemExit() or sys.exit()
  ├── KeyboardInterrupt                   Ctrl+C
  ├── GeneratorExit                       generator.close()
  └── Exception                           ← catch THIS or below
       ├── ArithmeticError
       │    ├── ZeroDivisionError           1/0
       │    ├── OverflowError               float too large
       │    └── FloatingPointError          rare float issues
       ├── LookupError
       │    ├── IndexError                  list[999] on short list
       │    └── KeyError                    dict['missing_key']
       ├── OSError (aka IOError)
       │    ├── FileNotFoundError           open('nope.txt')
       │    ├── PermissionError             no access
       │    ├── FileExistsError             file already exists
       │    ├── IsADirectoryError           expected file, got dir
       │    ├── ConnectionError
       │    │    ├── ConnectionRefusedError  server said no
       │    │    ├── ConnectionResetError    connection dropped
       │    │    └── BrokenPipeError         pipe closed
       │    └── TimeoutError                operation timed out
       ├── ValueError                      right type, wrong value
       │    └── UnicodeError
       │         ├── UnicodeDecodeError      bytes → str failed
       │         └── UnicodeEncodeError      str → bytes failed
       ├── TypeError                       wrong type entirely
       ├── AttributeError                  obj has no such attribute
       ├── NameError                       undefined variable
       │    └── UnboundLocalError           local var used before assign
       ├── ImportError
       │    └── ModuleNotFoundError         no such module
       ├── RuntimeError                    generic runtime issue
       │    ├── NotImplementedError         ABC method not overridden
       │    └── RecursionError              max recursion depth hit
       ├── StopIteration                   iterator exhausted
       ├── StopAsyncIteration              async iterator exhausted
       ├── SyntaxError                     invalid Python code
       │    └── IndentationError
       │         └── TabError                mixed tabs/spaces
       ├── MemoryError                     out of RAM
       └── Warning
            ├── DeprecationWarning          feature going away
            ├── FutureWarning               behavior will change
            └── UserWarning                 warnings.warn()

  PRACTICAL GUIDE:
  ────────────────
  Catch THIS              When you want to handle...
  ──────────────────────  ──────────────────────────────────────────
  Exception               ...anything that might go wrong (safe catch-all)
  LookupError             ...any missing key OR index
  OSError                 ...any file/network/system issue
  ValueError              ...bad function arguments
  TypeError               ...wrong argument types
  FileNotFoundError       ...specifically missing files
  KeyError                ...specifically missing dict keys
    """)


# ═══════════════════════════════════════════════════════════════════════════════
# ██████╗  █████╗ ██████╗ ████████╗    ██╗██████╗
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ██║╚════██╗
# ██████╔╝███████║██████╔╝   ██║       ██║ █████╔╝
# ██╔═══╝ ██╔══██║██╔══██╗   ██║       ██║ ╚═══██╗
# ██║     ██║  ██║██║  ██║   ██║       ██║██████╔╝
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚═╝╚═════╝
#  ENVIRONMENT & TOOLING — The stuff around the code
# ═══════════════════════════════════════════════════════════════════════════════


# %% 44 — Virtual Environments
def demo_venv():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  44 — VIRTUAL ENVIRONMENTS, PIP & PROJECT SETUP                    │
    │                                                                     │
    │  Einstein says: "Never install packages globally. Virtual envs     │
    │  give each project its own isolated Python with its own packages.  │
    │  This prevents 'it works on my machine' disasters."               │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(44, "VIRTUAL ENVIRONMENTS")

    print("""
  ── CREATE & ACTIVATE A VIRTUAL ENV ─────────────────────────────────────
  $ python3 -m venv .venv            # create env in .venv folder
  $ source .venv/bin/activate        # activate (Mac/Linux)
  $ .venv\\Scripts\\activate           # activate (Windows)
  $ deactivate                       # leave the virtual env

  ── PIP: PACKAGE MANAGEMENT ─────────────────────────────────────────────
  $ pip install requests             # install a package
  $ pip install requests==2.31.0    # install specific version
  $ pip install -r requirements.txt  # install from file
  $ pip freeze > requirements.txt    # save current packages
  $ pip list                         # see what's installed
  $ pip show requests                # package details
  $ pip uninstall requests           # remove package

  ── PROJECT STRUCTURE (the standard layout) ─────────────────────────────
  my_project/
  ├── .venv/                   ← virtual env (never commit this)
  ├── .gitignore               ← include .venv/ and __pycache__/
  ├── requirements.txt         ← pip freeze output
  ├── README.md
  ├── src/
  │   ├── __init__.py          ← makes src a package
  │   ├── main.py
  │   └── utils.py
  ├── tests/
  │   ├── __init__.py
  │   └── test_main.py
  └── pyproject.toml           ← modern project config (replaces setup.py)

  ── COMMAND-LINE ARGS ───────────────────────────────────────────────────
  $ python script.py arg1 arg2       # sys.argv = ['script.py', 'arg1', 'arg2']
  $ python -m module_name            # run as module (finds __main__.py)
  $ python -c "print('hi')"          # run one-liner
  $ python -i script.py              # run then drop into REPL

  ── USEFUL PYTHON CLI FLAGS ─────────────────────────────────────────────
  -B         don't write .pyc files
  -O         optimize (remove asserts)
  -v         verbose imports
  -W error   turn warnings into errors
  -u         unbuffered stdout/stderr
    """)

    #* ── LIVE: Checking your current environment ──
    import sys, os
    print(f"  Python:    {sys.version.split()[0]}")
    print(f"  Prefix:    {sys.prefix}")
    print(f"  Exec:      {sys.executable}")
    venv = os.environ.get('VIRTUAL_ENV', 'None (not in a venv)')
    print(f"  VENV:      {venv}")
    print(f"  Platform:  {sys.platform}")


# %% 45 — Debugging & Profiling
def demo_debugging():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  45 — DEBUGGING & PROFILING                                        │
    │                                                                     │
    │  "Everyone knows that debugging is twice as hard as writing the    │
    │  code. So if you write code as cleverly as possible, you are by   │
    │  definition not smart enough to debug it."  — Brian Kernighan     │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(45, "DEBUGGING & PROFILING")

    print("""
  ── PRINT DEBUGGING (quick & dirty, but effective) ──────────────────────
  print(f"{x = }")                   # Python 3.8+: prints "x = 42"
  print(f"{type(x) = }")             # prints type alongside value
  print(f"{len(data) = }")           # any expression works

  ── BREAKPOINT() — THE MODERN WAY (Python 3.7+) ────────────────────────
  # Drop this line anywhere in your code:
  breakpoint()                       # drops into pdb debugger

  # pdb commands (memorize these 6):
  n          next line (step over)
  s          step into function
  c          continue to next breakpoint
  p expr     print expression
  l          list source around current line
  q          quit debugger

  # Extra useful:
  pp expr    pretty-print
  w          where (call stack)
  b 42       set breakpoint at line 42
  h          help

  ── ASSERT: Poor man's unit test ────────────────────────────────────────
  assert len(users) > 0, "Users list is empty"    # crashes if False
  assert isinstance(x, int), f"Expected int, got {type(x)}"
  # Removed when running with python -O (optimize mode)

  ── TIMING CODE ─────────────────────────────────────────────────────────
  $ python -m timeit "[x**2 for x in range(100)]" # from terminal

  ── PROFILING ───────────────────────────────────────────────────────────
  $ python -m cProfile script.py               # full profile
  $ python -m cProfile -s cumulative script.py  # sorted by time
    """)

    #* ── LIVE: timeit example ──
    import timeit

    list_comp = timeit.timeit('[x**2 for x in range(100)]', number=10000)
    map_func = timeit.timeit('list(map(lambda x: x**2, range(100)))', number=10000)
    print(f"  timeit results (10k runs):")
    print(f"    List comp:  {list_comp:.4f}s")
    print(f"    map+lambda: {map_func:.4f}s")
    print(f"    Winner: {'list comp' if list_comp < map_func else 'map'}")

    #* ── Logging (better than print for real apps) ──
    print(f"\n  Logging levels: DEBUG(10) INFO(20) WARNING(30) ERROR(40) CRITICAL(50)")
    print("""
  import logging
  logging.basicConfig(level=logging.INFO)
  logger = logging.getLogger(__name__)
  logger.info("Normal operation")     # ← use instead of print()
  logger.error("Something broke")     # ← errors
  logger.debug("Detailed trace")      # ← dev only, hidden at INFO level
    """)


# ═══════════════════════════════════════════════════════════════════════════════
# ██████╗  █████╗ ██████╗ ████████╗    ██╗██╗  ██╗
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ██║██║  ██║
# ██████╔╝███████║██████╔╝   ██║       ██║███████║
# ██╔═══╝ ██╔══██║██╔══██╗   ██║       ██║╚════██║
# ██║     ██║  ██║██║  ██║   ██║       ██║     ██║
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚═╝     ╚═╝
#  REAL-WORLD RECIPES — Copy-paste solutions
# ═══════════════════════════════════════════════════════════════════════════════


# %% 46 — One-Liner Recipes
def demo_recipes():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  46 — ONE-LINER RECIPES                                            │
    │                                                                     │
    │  Einstein says: "These are the solutions you'll copy-paste into    │
    │  real projects. Each one replaces 5-20 lines of verbose code."    │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(46, "ONE-LINER RECIPES")

    #* ── FLATTEN A NESTED LIST ──
    nested = [[1, 2], [3, 4], [5, 6]]
    flat = [x for sub in nested for x in sub]
    print(f"  Flatten: {nested} → {flat}")

    #* ── DEDUPLICATE PRESERVING ORDER ──
    items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    unique = list(dict.fromkeys(items))          # dict preserves insertion order
    print(f"  Dedup:   {items} → {unique}")

    #* ── TRANSPOSE A MATRIX ──
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transposed = list(zip(*matrix))
    print(f"  Transpose: {matrix[0]}... → {list(transposed[0])}...")

    #* ── CHUNK A LIST INTO GROUPS OF N ──
    data = list(range(10))
    n = 3
    chunks = [data[i:i+n] for i in range(0, len(data), n)]
    print(f"  Chunk(3): {data} → {chunks}")

    #* ── INVERT A DICTIONARY ──
    original = {"a": 1, "b": 2, "c": 3}
    inverted = {v: k for k, v in original.items()}
    print(f"  Invert:  {original} → {inverted}")

    #* ── MERGE MULTIPLE DICTS ──
    d1, d2, d3 = {"a": 1}, {"b": 2}, {"c": 3}
    merged = {**d1, **d2, **d3}
    print(f"  Merge:   {merged}")

    #* ── FIND MOST COMMON ELEMENT ──
    from collections import Counter
    words = "the cat sat on the mat the cat".split()
    most_common = Counter(words).most_common(1)[0]
    print(f"  Most common: '{most_common[0]}' ({most_common[1]} times)")

    #* ── REMOVE FALSY VALUES ──
    messy = [0, 1, "", "hello", None, 42, False, [], "world"]
    clean = list(filter(None, messy))
    print(f"  Remove falsy: {clean}")

    #* ── SAFE DICTIONARY ACCESS WITH DEFAULTS ──
    config = {"debug": True}
    verbose = config.get("verbose", False)
    print(f"  Safe get: {verbose}")

    #* ── RUNNING TALLY / CUMULATIVE SUM ──
    from itertools import accumulate
    nums = [1, 2, 3, 4, 5]
    running = list(accumulate(nums))
    print(f"  Running sum: {nums} → {running}")

    #* ── QUICK HTTP REQUEST (stdlib, no pip install) ──
    # from urllib.request import urlopen
    # data = urlopen('https://api.example.com/data').read().decode()
    print(f"  HTTP: urllib.request.urlopen() — no pip needed")

    #* ── READ ENTIRE FILE AS STRING ──
    # content = Path('file.txt').read_text()
    print(f"  Read file: Path('file.txt').read_text()")

    #* ── PRETTY PRINT ANY DATA STRUCTURE ──
    import pprint
    complex_data = {"users": [{"name": "Stewart", "skills": ["Python", "Supply Chain"]}]}
    print(f"\n  pprint:")
    pprint.pprint(complex_data, indent=4, width=60)


# ═══════════════════════════════════════════════════════════════════════════════
#  APPENDIX
# ═══════════════════════════════════════════════════════════════════════════════


# ═══════════════════════════════════════════════════════════════════════════════
#  SELF-TEST QUIZ
# ═══════════════════════════════════════════════════════════════════════════════

# %% Self-Test
def run_self_tests():
    """
    Interactive quiz — type your prediction, get instant feedback.

    Teaches through encouragement: when you miss one, the explanation
    helps you understand WHY, not just WHAT.  Designed so you walk
    away smarter every time, even on a perfect score.
    """

    # ── Quiz questions ──────────────────────────────────────────────────
    # (name, code_shown, answer, section, teach_right, teach_wrong)
    #
    #  code_shown:   the expression displayed to the user
    #  answer:       the actual Python result (evaluated at definition time)
    #  section:      which section covers this topic (for cross-reference)
    #  teach_right:  short congrats + deeper insight (shown on correct answer)
    #  teach_wrong:  encouraging explanation (shown on wrong answer)
    # ───────────────────────────────────────────────────────────────────
    tests = [
        (
            "Slicing",
            '"hello"[1:4]',
            "hello"[1:4],
            "strings",
            "Nailed it. Slicing is [start:stop) — stop is always exclusive."
            "  This half-open interval convention is the same in range(), "
            "and once it clicks you'll never get an off-by-one error again.",
            "Almost! Slicing uses [start:stop) — the stop index is exclusive.\n"
            "         So 'hello'[1:4] grabs indices 1, 2, 3 → 'ell'.\n"
            "         Think of it like a fence: start is the first post,\n"
            "         stop is where you STOP (not where you include)."
        ),
        (
            "Negative index",
            "[10, 20, 30, 40][-2]",
            [10, 20, 30, 40][-2],
            "lists",
            "Exactly. Negative indices count from the end: -1 is last, -2 is second-last.",
            "Close — negative indices count backward from the end.\n"
            "         -1 is the last element (40), -2 is second-to-last (30).\n"
            "         Think of it as len(list) + index: 4 + (-2) = index 2."
        ),
        (
            "Nested length",
            "len([1, [2, 3], 4])",
            len([1, [2, 3], 4]),
            "lists",
            "Right — [2, 3] is ONE element.  len() counts top-level items, not contents.",
            "Good instinct, but [2, 3] counts as a single element.\n"
            "         The outer list has three items: 1, [2,3], and 4.\n"
            "         len() only counts the top level — it doesn't peek inside."
        ),
        (
            "Dict .get()",
            '{"a": 1}.get("b", 0)',
            {"a": 1}.get("b", 0),
            "dicts",
            "Spot on. .get() returns the default when the key is missing — no KeyError."
            "  This is the Pythonic way to handle missing keys without try/except.",
            "Think of .get(key, default) as 'try this key, but if it's\n"
            "         not there, give me this instead.'  'b' isn't in the dict,\n"
            "         so it returns the default: 0.  This is safer than dict['b']\n"
            "         which would raise a KeyError."
        ),
        (
            "Bool of empty",
            "bool([])",
            bool([]),
            "booleans",
            "Yes — empty containers are falsy.  [], {}, set(), '', 0, None → all False.",
            "This is Python's 'truthiness' system: empty containers are falsy.\n"
            "         [], {}, set(), '', 0, and None all evaluate to False.\n"
            "         Anything with content is truthy.  This is why you can write\n"
            "         'if my_list:' instead of 'if len(my_list) > 0:'."
        ),
        (
            "Bool of [0]",
            "bool([0])",
            bool([0]),
            "booleans",
            "Nice catch — the list ISN'T empty, so it's truthy.  The 0 inside doesn't matter.",
            "This one trips up a lot of people! The list contains something,\n"
            "         so it's truthy — even though that something is 0.\n"
            "         Python checks 'is the container empty?', not 'are the\n"
            "         contents truthy?'.  [0] has one element → True."
        ),
        (
            "Division type",
            "type(10 / 2).__name__",
            type(10 / 2).__name__,
            "numbers",
            "Got it — / ALWAYS returns float in Python 3, even for 10/2.  Use // for int.",
            "Careful — in Python 3, / always gives you a float.\n"
            "         Even 10 / 2 = 5.0, not 5.  This changed from Python 2.\n"
            "         If you want integer division, use //: 10 // 2 = 5."
        ),
        (
            "Floor division",
            "17 // 5",
            17 // 5,
            "numbers",
            "Right — // floors toward negative infinity.  17 / 5 = 3.4, floored to 3.",
            "// is floor division — it rounds DOWN to the nearest integer.\n"
            "         17 / 5 = 3.4, and floor(3.4) = 3.\n"
            "         Watch out with negatives: -17 // 5 = -4 (not -3),\n"
            "         because floor() goes toward negative infinity."
        ),
        (
            "Ternary",
            '"yes" if "" else "no"',
            "yes" if "" else "no",
            "conditionals",
            "Exactly — empty string is falsy, so the else branch fires.",
            "Remember Python's truthiness: empty string '' is falsy.\n"
            "         The ternary pattern is: VALUE_IF_TRUE if CONDITION else VALUE_IF_FALSE.\n"
            "         Since '' is falsy, the condition fails → 'no'."
        ),
        (
            "Tuple trap",
            "type((42,)).__name__",
            type((42,)).__name__,
            "tuples",
            "Yes! The COMMA makes the tuple, not the parentheses.  This catches everyone once.",
            "Here's the thing — the comma makes the tuple, not the parentheses.\n"
            "         (42,) has a trailing comma → it's a tuple.\n"
            "         (42) has no comma → it's just grouping, same as plain 42.\n"
            "         Once you see it, you never forget it."
        ),
        (
            "Not a tuple",
            "type((42)).__name__",
            type((42)).__name__,
            "tuples",
            "Exactly — no comma, no tuple.  (42) is just 42 in parentheses.",
            "This is the flip side of the comma rule: without a trailing comma,\n"
            "         parentheses are just grouping.  (42) == 42, which is an int.\n"
            "         To make a single-element tuple: (42,) — note the comma."
        ),
        (
            "Comprehension",
            "[x*2 for x in range(4)]",
            [x*2 for x in range(4)],
            "comprehensions",
            "Clean.  Comprehensions are the Pythonic way to transform sequences.",
            "range(4) produces 0, 1, 2, 3 (four numbers, starting at 0).\n"
            "         Each gets doubled: 0*2=0, 1*2=2, 2*2=4, 3*2=6.\n"
            "         Result: [0, 2, 4, 6].  Remember: range(n) gives you\n"
            "         n numbers starting from 0."
        ),
        (
            "Chained compare",
            "1 < 2 < 3",
            1 < 2 < 3,
            "conditionals",
            "Yes — Python chains comparisons naturally.  It means (1<2) and (2<3).",
            "Python lets you chain comparisons like math notation.\n"
            "         1 < 2 < 3 means (1 < 2) AND (2 < 3) — both True → True.\n"
            "         This works with any comparisons: a <= b < c == d."
        ),
        (
            "String repeat",
            '"ha" * 3',
            "ha" * 3,
            "strings",
            "Right — * repeats strings.  Works on lists too: [0] * 5 = [0, 0, 0, 0, 0].",
            "The * operator repeats sequences.  'ha' * 3 = 'hahaha'.\n"
            "         Works on lists too: [0] * 3 = [0, 0, 0].\n"
            "         But be careful with mutable contents:\n"
            "         [[]] * 3 creates three references to the SAME inner list."
        ),
        (
            "Substring",
            '"py" in "python"',
            "py" in "python",
            "strings",
            "Yes — 'in' checks for substring containment in strings.",
            "The 'in' operator checks for substrings in strings.\n"
            "         'py' appears at the start of 'python' → True.\n"
            "         For lists, 'in' checks for element membership instead."
        ),
        (
            "Dict merge",
            "{1: 'a', 2: 'b'} | {2: 'c'}",
            {1: 'a', 2: 'b'} | {2: 'c'},
            "dicts",
            "Exactly — | merges dicts, right side wins on conflicts.  Python 3.9+ feature.",
            "The | operator merges two dicts (Python 3.9+).\n"
            "         When both have the same key (2), the right side wins.\n"
            "         So key 2 gets 'c' (from the right dict), not 'b'.\n"
            "         Result: {1: 'a', 2: 'c'}."
        ),
        (
            "Walrus",
            "(n := 10) > 5",
            (n := 10) > 5,
            "conditionals",
            "Got it — := assigns AND returns the value in one shot.  10 > 5 = True.",
            "The walrus operator := assigns a value AND returns it.\n"
            "         (n := 10) assigns 10 to n, then the expression becomes 10 > 5.\n"
            "         10 > 5 is True.  This is useful in while-loops and if-conditions\n"
            "         where you need the value AND the test."
        ),
        (
            "Set intersection",
            "{1,2,3} & {2,3,4}",
            {1,2,3} & {2,3,4},
            "sets",
            "Right — & gives you elements in BOTH sets.  Set math is underrated.",
            "& is set intersection — elements that appear in BOTH sets.\n"
            "         {1,2,3} and {2,3,4} share 2 and 3 → {2, 3}.\n"
            "         Other set ops: | (union), - (difference), ^ (symmetric diff)."
        ),
        (
            "Star unpacking",
            "a, *b, c = [1,2,3,4,5]\n         What is (a, b, c)?",
            (1, [2, 3, 4], 5),
            "variables",
            "Yes — *b captures everything in the middle as a list.  Powerful for APIs.",
            "The * in unpacking captures 'the rest' into a list.\n"
            "         a gets the first element: 1\n"
            "         c gets the last element: 5\n"
            "         *b gets everything in between: [2, 3, 4]\n"
            "         Works anywhere: first, *rest = [1,2,3] → rest = [2,3]."
        ),
        (
            "Mutable default",
            "def f(x=[]):\n             x.append(1)\n             return x\n"
            "         f(); f(); f()  — what does the last call return?",
            [1, 1, 1],
            "gotchas",
            "You spotted the trap! Default args are evaluated ONCE — the same list persists.",
            "This is Python's most famous gotcha.  Default arguments are\n"
            "         evaluated ONCE when the function is defined, not on each call.\n"
            "         So every call to f() appends to the SAME list object.\n"
            "         After three calls: [1, 1, 1].\n"
            "         Fix: use 'def f(x=None): x = x or []'."
        ),
    ]

    # ── Normalize an answer for flexible comparison ────────────────────
    def _normalize(text):
        """Strip whitespace, quotes, and normalize Python literals for comparison."""
        t = text.strip()
        # Strip matching outer quotes: 'ell' or "ell" → ell
        if len(t) >= 2 and t[0] == t[-1] and t[0] in ('"', "'"):
            t = t[1:-1]
        return t

    def _check_answer(user_input, expected):
        """Compare user's text answer against the expected Python value.

        Flexible: accepts 'ell', "ell", ell for string answers;
        True/true/TRUE for booleans; {2, 3} or {3, 2} for sets; etc.
        """
        raw = user_input.strip()
        if not raw:
            return False

        norm = _normalize(raw)
        exp_str = repr(expected)
        exp_norm = _normalize(exp_str)

        # Direct match against repr
        if norm == exp_norm:
            return True

        # Try evaluating the user's input as a Python literal
        try:
            user_val = eval(raw, {"__builtins__": {}}, {})
            if user_val == expected:
                return True
        except Exception:
            pass

        # Case-insensitive match for simple types (True/False/None, strings)
        if isinstance(expected, bool):
            return norm.lower() in ("true", "false") and \
                   (norm.lower() == "true") == expected
        if isinstance(expected, str):
            return norm == expected
        if isinstance(expected, (int, float)):
            try:
                return float(norm) == float(expected)
            except (ValueError, TypeError):
                return False

        return False

    # ── Run the quiz ──────────────────────────────────────────────────
    print("\n" + "─" * 70)
    print("  SELF-TEST QUIZ")
    print("─" * 70)
    print("  Type your answer for each expression.  No peeking at the REPL!")
    print("  Press Enter with no answer to skip.  Ctrl+C to quit early.\n")

    passed = 0
    skipped = 0
    wrong = 0
    weak_areas = []  # (section_key, question_name) for missed questions
    total = len(tests)

    for i, (name, code, answer, section, teach_right, teach_wrong) in enumerate(tests, 1):
        print(f"  [{i}/{total}] What does this evaluate to?")
        print(f"         {code}")
        print()

        try:
            user = input("    > ")
        except (EOFError, KeyboardInterrupt):
            print("\n")
            break

        if not user.strip():
            skipped += 1
            print(f"    Skipped.  Answer: {answer!r}")
            print(f"    {teach_wrong.split(chr(10))[0]}")
            print()
            weak_areas.append((section, name))
            continue

        if _check_answer(user, answer):
            passed += 1
            print(f"    Correct! {answer!r}")
            print(f"    {teach_right.split(chr(10))[0]}")
        else:
            wrong += 1
            print(f"    Not quite — the answer is {answer!r}")
            # Print the full encouraging explanation, indented
            for line in teach_wrong.split("\n"):
                print(f"    {line}")
            weak_areas.append((section, name))

        print()

    # ── Results ──────────────────────────────────────────────────────
    answered = passed + wrong
    print("─" * 70)
    print(f"  Score: {passed}/{total}", end="")
    if skipped:
        print(f"  ({skipped} skipped)", end="")
    print("\n")

    if passed == total:
        print("  You know your Python.  Go build something.")
    elif passed >= total * 0.8:
        print("  Strong showing.  A few rough edges to polish, but you're")
        print("  well ahead of the curve.")
    elif passed >= total * 0.5:
        print("  Solid start — you've got the foundations.  The ones you missed")
        print("  are the same ones that trip up experienced devs.  Keep going.")
    elif answered > 0:
        print("  No worries — every expert started exactly where you are.")
        print("  The fact that you're testing yourself puts you ahead of most.")
    else:
        print("  Quiz cut short — come back any time.  No rush.")

    # ── Targeted study suggestions ───────────────────────────────────
    if weak_areas:
        # Group by section, deduplicate
        sections_to_review = []
        seen = set()
        for sec_key, q_name in weak_areas:
            if sec_key not in seen:
                seen.add(sec_key)
                # Look up the section title
                title = sec_key
                for sk, sn, st, _, _ in SECTION_META:
                    if sk == sec_key:
                        title = f"{sn:02d} {st}"
                        break
                sections_to_review.append((sec_key, title))

        print("\n  Sections worth revisiting:")
        for sec_key, title in sections_to_review:
            print(f"    → {title}  (python python_poweruser.py -s {sec_key})")

    print(f"\n{'─' * 70}")
    return passed, total


# ═══════════════════════════════════════════════════════════════════════════════
#  DEMO REGISTRY & MAIN
# ═══════════════════════════════════════════════════════════════════════════════

DEMO_REGISTRY = {
    # Part 1 — Foundations
    "variables":      demo_variables,
    "numbers":        demo_numbers,
    "strings":        demo_strings,
    "booleans":       demo_booleans,
    # Part 2 — Data Structures
    "lists":          demo_lists,
    "tuples":         demo_tuples,
    "dicts":          demo_dicts,
    "sets":           demo_sets,
    "structures":     demo_advanced_structures,
    # Part 3 — Control Flow
    "conditionals":   demo_conditionals,
    "loops":          demo_loops,
    "comprehensions": demo_comprehensions,
    # Part 4 — Functions
    "functions":      demo_functions,
    "scope":          demo_scope,
    "lambda":         demo_lambda,
    "decorators":     demo_decorators,
    "functools":      demo_functools,
    # Part 5 — OOP
    "classes":        demo_classes,
    "inheritance":    demo_inheritance,
    "dunders":        demo_dunders,
    "properties":     demo_properties,
    "abcs":           demo_abcs,
    # Part 6 — Error Handling
    "exceptions":     demo_exceptions,
    "context":        demo_context_managers,
    "custom_errors":  demo_custom_exceptions,
    # Part 7 — Iterators & Generators
    "iterators":      demo_iterators,
    "generators":     demo_generators,
    "itertools":      demo_itertools,
    # Part 8 — File I/O
    "files":          demo_files,
    "json_csv":       demo_json_csv,
    "pathlib":        demo_pathlib,
    # Part 9 — Text Mastery
    "regex":          demo_regex,
    "formatting":     demo_formatting,
    "datetime":       demo_datetime,
    # Part 10 — Stdlib Power Tools
    "collections":    demo_collections,
    "os":             demo_os,
    "typing":         demo_typing,
    # Part 11 — Pythonic Patterns
    "idioms":         demo_idioms,
    "performance":    demo_performance,
    "gotchas":        demo_gotchas,
    # Part 12 — Reference Tables
    "precedence":     demo_operator_precedence,
    "builtins":       demo_builtins,
    "exceptions_ref": demo_exception_tree,
    # Part 13 — Environment & Tooling
    "venv":           demo_venv,
    "debugging":      demo_debugging,
    # Part 14 — Real-World Recipes
    "recipes":        demo_recipes,
    # Appendix
    "cheatsheet":     demo_cheatsheet,
}


def run_all():
    """Run every demo section."""
    print("═" * 70)
    print("  PYTHON POWER USER — Complete Language Reference")
    print("  47 sections • Foundations → Advanced → Competitive Edge")
    print("═" * 70)

    for name, func in DEMO_REGISTRY.items():
        try:
            func()
        except Exception as e:
            print(f"\n  [ERROR in {name}]: {e}")

    print("\n" + "═" * 70)
    print("  ALL SECTIONS COMPLETE")
    print("  Run 'python python_poweruser.py test' for the self-test quiz")
    print("═" * 70)


if __name__ == "__main__":
    try:
        _parse_args_and_run()
    except KeyboardInterrupt:
        # Clean Ctrl+C at any point — never dump a traceback
        print("\n")
        sys.exit(0)
    except BrokenPipeError:
        # Piped to head/less that closed early — suppress
        sys.stderr.close()
        sys.exit(0)
