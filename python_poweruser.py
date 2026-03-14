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
#  New to Python? Start with Part 1 (Foundations). Open the TUI (run this file
#  with no arguments) and work through sections 01–04, or run one section from
#  the terminal:  python python_poweruser.py -s variables
#
#  This file works as both a learning guide and a reference:
#    • Learn: read Part 1 → Part 2, run each section (press r in TUI), try the
#      "Try this" suggestions in the comments
#    • Refresh: skim a section when you need a reminder
#    • Look up: use Ctrl+F or the TUI search when you need a specific pattern
#    • Self-check: run  python python_poweruser.py test  after Part 2 or 3
#
#  A 15‑minute session looks like this:
#    1. Pick a section from  python python_poweruser.py -l  (or open the TUI and choose one).
#    2. Read the Goal (Beginner) or Goal (Power User) for that section at the top.
#    3. Predict answers to each #? and run the Try this or Speed run cells.
#    4. Every few sessions, run  -t  (quiz) and revisit the sections it suggests.
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
from __future__ import annotations

from typing import Any, Callable, Iterable, Iterator, List, Mapping, MutableMapping, Optional, Sequence, Tuple

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
#    05  Lists                     Ordered collections you can change
#    06  Tuples                    Ordered collections you keep fixed
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
import json
import math
from difflib import SequenceMatcher
from pathlib import Path

# ── Locale: ensure Unicode box-drawing chars render correctly everywhere ──
try:
    locale.setlocale(locale.LC_ALL, "")
except locale.Error:
    pass  # Hardened environments may block setlocale — that's fine

# ═══════════════════════════════════════════════════════════════════════════════
#  HELPER: Pretty section headers for terminal output
# ═══════════════════════════════════════════════════════════════════════════════

def _header(num: int, title: str) -> None:
    """Print a clean section header."""
    print(f"\n{'─' * 70}")
    print(f"  {num:02d} │ {title}")
    print(f"{'─' * 70}")


# ═══════════════════════════════════════════════════════════════════════════════
#  TUI — Interactive Terminal User Interface (curses-based)
# ═══════════════════════════════════════════════════════════════════════════════

_TUI_VERSION = "3.0"

# When True, the TUI viewer shows both the teaching docstring and a cleaned
# version of the underlying source code for each demo function. The cleaner
# strips leading docstrings and de-noises print-based plumbing so the viewer
# focuses on the *examples* rather than the formatting wrappers.
_TUI_SHOW_SOURCE = True

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

SECTION_BIG_PICTURE: Mapping[str, str] = {
    # Part 1 — Foundations
    "variables": (
        "Variables are names pointing at values; the real skill is seeing when "
        "multiple names share the same changeable value versus working on copies."
    ),
    "numbers": (
        "Integers are exact and unbounded, floats are fast approximations, and "
        "Decimal / math.isclose are how you stay honest about numeric comparisons."
    ),
    "strings": (
        "Strings are sequences of characters that never change once created; slicing and "
        "indexing are tools you’ll reuse on lists, tuples, ranges, and more."
    ),
    "booleans": (
        "Python has a small set of falsy values and a huge space of truthy ones; "
        "understanding truthiness, None, and short‑circuiting makes conditions readable."
    ),
    # Part 2 — Data Structures
    "lists": (
        "Lists are ordered, growable collections you can change — your go‑to tool for "
        "most groups of items when order matters and you need to append or remove."
    ),
    "tuples": (
        "Tuples are fixed‑size collections that you do not change after creating them; "
        "they work well for lightweight records, dictionary keys, and returning multiple values."
    ),
    "dicts": (
        "Dictionaries map keys to values with O(1) average lookup time and are the "
        "backbone of most real‑world Python data modeling."
    ),
    "sets": (
        "Sets hold unique elements and shine when you care about membership tests, "
        "deduplication, and classic set operations like union and intersection."
    ),
    "structures": (
        "Namedtuple, dataclass, and friends give structure and readability to your "
        "data without the ceremony of full classes."
    ),
    # Part 3 — Control Flow
    "conditionals": (
        "Conditionals express branching logic; the art is keeping them readable with "
        "clear predicates instead of deeply nested if/elif ladders."
    ),
    "loops": (
        "Loops let you walk collections; Pythonic style favors for‑loops with "
        "enumerate, zip, and early exits over manual index bookkeeping."
    ),
    "comprehensions": (
        "Comprehensions turn common loop‑and‑build patterns into compact, readable "
        "expressions that are both faster and easier to scan."
    ),
    # Part 4 — Functions
    "functions": (
        "Functions encapsulate behavior behind names so you can reuse, test, and "
        "reason about small units instead of giant scripts."
    ),
    "scope": (
        "Python looks up names in order: current function, then enclosing functions, "
        "then the module, then built-ins. That order explains closures and why 'nonlocal' matters."
    ),
    "lambda": (
        "Lambda and functional tools like map, filter, and reduce shine when you want "
        "to transform collections without explicit index‑based loops."
    ),
    "decorators": (
        "Decorators wrap functions to add behavior (logging, caching, auth) without "
        "changing the original call sites everywhere."
    ),
    "functools": (
        "functools provides battle‑tested building blocks like lru_cache and partial "
        "that let you optimize and adapt functions with minimal code."
    ),
    # Part 5 — OOP
    "classes": (
        "Classes bundle data and behavior together so related operations live next "
        "to the state they act on."
    ),
    "inheritance": (
        "Inheritance lets classes reuse and specialize behavior, but composition and "
        "interfaces often keep designs simpler."
    ),
    "dunders": (
        "Dunder methods (__init__, __repr__, __add__, etc.) define how your objects "
        "behave with core Python syntax and built‑ins."
    ),
    "properties": (
        "Properties and slots give you control over attribute access, validation, and "
        "memory usage without changing attribute syntax for callers."
    ),
    "abcs": (
        "Abstract base classes and protocols let you specify required behaviors so "
        "unrelated types can plug into the same APIs."
    ),
    # Part 6 — Error Handling
    "exceptions": (
        "Exceptions separate happy‑path code from error handling so failures can "
        "bubble up to a single, sensible place."
    ),
    "context": (
        "Context managers guarantee setup/teardown (like closing files or releasing "
        "locks) even when errors happen mid‑operation."
    ),
    "custom_errors": (
        "Custom exception types make it clear what went wrong and let callers catch "
        "exactly the failures they care about."
    ),
    # Part 7 — Iterators & Generators
    "iterators": (
        "Iterators power for‑loops under the hood; once you understand the protocol, "
        "you can stream data instead of materializing it all at once."
    ),
    "generators": (
        "Generators use yield to build lazy pipelines that handle large or infinite "
        "streams one item at a time."
    ),
    "itertools": (
        "itertools is a toolbox of composable building blocks for creating powerful "
        "iterator pipelines with little code."
    ),
    # Part 8 — File I/O & Data
    "files": (
        "File handling is about safely opening, reading, writing, and closing files "
        "without leaking resources or corrupting data."
    ),
    "json_csv": (
        "JSON and CSV are the everyday wire formats of data interchange; Python’s "
        "stdlib makes them easy to read, write, and validate."
    ),
    "pathlib": (
        "pathlib replaces stringly‑typed file paths with rich objects that know how "
        "to join, inspect, and manipulate paths portably."
    ),
    # Part 9 — Text Mastery
    "regex": (
        "Regular expressions match patterns in text; a few core constructs cover "
        "most real‑world parsing and validation tasks."
    ),
    "formatting": (
        "String formatting (especially f‑strings) gives you precise control over how "
        "values are presented to humans and other systems."
    ),
    "datetime": (
        "Datetime handling is about being explicit with timezones, durations, and "
        "formats so your code works beyond your own machine."
    ),
    # Part 10 — Stdlib Power Tools
    "collections": (
        "collections provides specialized containers like deque and Counter that solve "
        "common problems more cleanly than plain lists and dicts."
    ),
    "os": (
        "os and subprocess let your Python code talk to the operating system, run "
        "commands, and manage files and processes."
    ),
    "typing": (
        "Type hints document the shapes of your data and enable tools to catch whole "
        "classes of bugs before runtime."
    ),
    # Part 11 — Pythonic Patterns
    "idioms": (
        "Pythonic idioms are the small patterns (like unpacking, context managers, "
        "and EAFP) that make code both concise and clear."
    ),
    "performance": (
        "Performance work starts with measurement, then uses algorithms, data "
        "structures, and profiling to speed up real bottlenecks."
    ),
    "gotchas": (
        "Gotchas are the sharp edges of the language; knowing them means you can "
        "recognize and avoid surprising behavior in the wild."
    ),
    # Part 12 — Reference Tables
    "precedence": (
        "Operator precedence tables explain which operations bind tighter so complex "
        "expressions behave the way you expect."
    ),
    "builtins": (
        "Built‑in functions are the tiny utilities you reach for constantly; learning "
        "them saves reinventing wheels."
    ),
    "exceptions_ref": (
        "The exception hierarchy shows how error types relate so you can catch broad "
        "categories without masking unrelated bugs."
    ),
    # Part 13 — Env & Tooling / Recipes / Appendix
    "venv": (
        "Virtual environments isolate dependencies per project so upgrades and "
        "experiments don’t break other work."
    ),
    "debugging": (
        "Debugging and profiling tools (breakpoint, pdb, cProfile, timeit) reveal "
        "what your code is actually doing, not what you assume it does."
    ),
    "recipes": (
        "One‑liner recipes are battle‑tested snippets you can paste in and adapt "
        "for common day‑to‑day tasks."
    ),
    "cheatsheet": (
        "The cheat sheet is a compressed reference: answers at a glance once you’ve "
        "seen the full explanations elsewhere."
    ),
}

# Part-level "Why this matters" and TL;DR for power users (dual-purpose resource).
PART_WHY: Mapping[int, str] = {
    1: "Scripts, configs, and APIs all start with variables, numbers, strings, and booleans — get these right and the rest stacks.",
    2: "Real code is full of lists, dicts, and sets; picking the right structure is half the battle.",
    3: "Branching and looping are how you direct the program; Pythonic style keeps them readable and concise.",
    4: "Functions are the unit of reuse; decorators and functools are how pros add behavior without clutter.",
    5: "OOP in Python is about data + behavior in one place; dunders and protocols are what make your types feel native.",
    6: "Exceptions and context managers keep failure paths clean and resources safe.",
    7: "Iterators and generators power streaming and pipelines; itertools is the toolbox.",
    8: "Files, JSON, and paths are how Python talks to the world; pathlib and context managers keep it safe.",
    9: "Regex, formatting, and datetime cover most text and time tasks in the wild.",
    10: "collections, os, subprocess, and typing are the stdlib power tools you reach for daily.",
    11: "Idioms, performance, and gotchas separate readable, fast code from surprising bugs.",
    12: "Reference tables are Ctrl+F heaven when you need precedence, built-ins, or the exception tree.",
    13: "Virtual envs and debugging tools keep projects isolated and bugs findable.",
    14: "Recipes are copy-paste solutions for real-world micro-tasks.",
    15: "The appendix is the cheat sheet: everything at a glance.",
}

PART_TLDR: Mapping[int, List[str]] = {
    1: [
        "Variables are names; assignment never copies. int is unbounded, float approximate; use Decimal for money.",
        "str is immutable; slicing returns new strings. Only None, False, 0, '', (), [], {} are falsy.",
    ],
    2: [
        "Lists: ordered, mutable. Tuples: fixed, hashable, great for keys and multi-return. Dicts: O(1) lookup.",
        "Sets: unique, unordered. Prefer dict/set comps and built-ins (in, len) over manual loops.",
    ],
    3: [
        "match/case for multi-branch; ternary x if c else y. for with enumerate/zip; avoid while when for fits.",
        "Comprehensions > loop-and-append; generator expressions when you need lazy/one-pass.",
    ],
    4: [
        "Default args evaluated once at def time; use None + assign for mutables. *args/**kwargs for flex APIs.",
        "Decorators wrap functions; use functools.wraps. lru_cache and partial are your friends.",
    ],
    5: [
        "Composition over deep inheritance. __repr__ for devs, __str__ for users. Protocols/ABCs for interfaces.",
        "dataclass for data; __slots__ when you have many instances and care about memory.",
    ],
    6: [
        "Catch specific exceptions; let generic ones bubble. with for resources; __enter__/__exit__ for custom.",
        "Custom exceptions inherit from Exception; keep hierarchy shallow.",
    ],
    7: [
        "Iterators: __iter__ + __next__; for consumes them. Generators: yield = lazy; one-pass only.",
        "itertools.chain, islice, groupby for pipelines; avoid materializing huge lists.",
    ],
    8: [
        "Open files with with; use pathlib for paths. json.load/dump; csv.DictReader/DictWriter for CSV.",
        "Encoding: specify encoding='utf-8' explicitly for portability.",
    ],
    9: [
        "re: findall, search, sub; compile for repeated use. f-strings and .format for formatting.",
        "datetime: timezone-aware when you care; use datetime.timezone.utc or zoneinfo.",
    ],
    10: [
        "deque for queues/stacks; Counter for counts; ChainMap for layered config.",
        "subprocess.run with capture_output=True; avoid shell=True when possible.",
    ],
    11: [
        "EAFP over LBYL. Unpacking, with, and comprehensions over manual loops.",
        "Measure first; optimize algorithms and data structures before micro-optimizing.",
    ],
    12: [
        "Precedence: ** then * / // % then + -; use parens when in doubt.",
        "Know the exception tree so you don't catch BaseException or mask bugs.",
    ],
    13: [
        "One venv per project; pip freeze > requirements.txt. breakpoint() and pdb for debugging.",
        "cProfile for hotspots; timeit for small snippets.",
    ],
    14: [
        "One-liners: invert dict, merge configs, count frequencies — see section 46.",
    ],
    15: [
        "Cheat sheet: quick scan; details live in the sections above.",
    ],
}

# Section-level goals (Beginner = what you'll learn; Power User = what you'll sharpen).
SECTION_GOALS: Mapping[str, Tuple[str, str]] = {
    "variables": ("Understand that variables are names for values and how assignment works.", "Internalize that assignment never copies and when that matters."),
    "numbers": ("Use integers and floats safely and know when they behave oddly.", "Know int/float/Decimal trade-offs and use math.isclose for floats."),
    "strings": ("Create, slice, and combine strings without surprises.", "Use str methods and immutability to write clear, efficient code."),
    "booleans": ("Use True/False and None and write simple conditions.", "Master truthiness, short-circuiting, and the one way to test for None."),
    "lists": ("Build and change lists with append, slice, and loops.", "Choose lists vs other sequences; avoid mutating while iterating."),
    "tuples": ("Use tuples for fixed data and multiple return values.", "Know when to choose a list vs tuple in real code (keys, unpacking, immutability)."),
    "dicts": ("Store and look up key-value pairs with dicts.", "Use dicts as the default data structure; know .get, views, and merge patterns."),
    "sets": ("Store unique items and do simple set math.", "Use sets for membership and dedup; know hashability and set comps."),
    "structures": ("Use namedtuple and dataclass for readable structured data.", "Pick namedtuple/dataclass/defaultdict/Counter by use case."),
    "conditionals": ("Write if/elif/else and use simple match/case.", "Use match/case and ternary where they reduce noise."),
    "loops": ("Loop with for and while and use range.", "Use enumerate, zip, and early exit; avoid manual index loops."),
    "comprehensions": ("Write list comprehensions instead of simple loops.", "Use dict/set/gen comps; know when genex beats list comp."),
    "functions": ("Define functions with arguments and return values.", "Design APIs with *args/**kwargs and mutable default gotchas."),
    "scope": ("See where names are visible (local vs global).", "Apply LEGB and closures; use nonlocal when needed."),
    "lambda": ("Use lambda for tiny one-line functions.", "Know when lambda/map/filter help and when a loop is clearer."),
    "decorators": ("Wrap a function to add behavior without changing call sites.", "Write decorators that preserve metadata and take arguments."),
    "functools": ("Use lru_cache and partial for common patterns.", "Apply wraps, partial, and reduce where they simplify code."),
    "classes": ("Define classes with __init__ and methods.", "Use classes for data+behavior; prefer composition."),
    "inheritance": ("Reuse code with inheritance and super().", "Prefer composition and shallow hierarchies."),
    "dunders": ("Use __init__ and __repr__ correctly.", "Implement the right dunders so your types feel native."),
    "properties": ("Use @property for computed attributes.", "Choose @property vs __slots__ by clarity and memory."),
    "abcs": ("Understand interfaces and duck typing.", "Use ABCs and Protocol for optional static checks."),
    "exceptions": ("Use try/except to handle errors.", "Catch specific exceptions; use else/finally correctly."),
    "context": ("Use with for files and locks.", "Write __enter__/__exit__ or use contextlib."),
    "custom_errors": ("Define your own exception types.", "Keep custom exception hierarchies shallow and named clearly."),
    "iterators": ("See how for loops consume iterables.", "Implement __iter__/__next__ when you need custom streaming."),
    "generators": ("Use yield to produce values one at a time.", "Build lazy pipelines and avoid materializing huge lists."),
    "itertools": ("Use a few itertools functions for common loops.", "Compose chain, islice, groupby for iterator pipelines."),
    "files": ("Open, read, write, and close files safely.", "Use with and pathlib; specify encoding."),
    "json_csv": ("Read and write JSON and CSV files.", "Use json load/dump and csv.DictReader/Writer; handle encoding."),
    "pathlib": ("Use Path objects instead of string paths.", "Use pathlib everywhere for portable, readable paths."),
    "regex": ("Match and find patterns in text with re.", "Compile for repeated use; know character classes and groups."),
    "formatting": ("Format strings with f-strings and .format.", "Use alignment, width, and number formats where needed."),
    "datetime": ("Work with dates and times using datetime.", "Be timezone-aware; use zoneinfo or timezone.utc."),
    "collections": ("Use deque, Counter, and OrderedDict when they fit.", "Reach for collections before reinventing with dict/list."),
    "os": ("Run shell commands and use os for paths/env.", "Use subprocess.run; avoid shell=True when possible."),
    "typing": ("Add type hints to function signatures.", "Use typing for generics and Protocol; run mypy."),
    "idioms": ("Recognize common Pythonic patterns.", "Use EAFP, unpacking, and with routinely."),
    "performance": ("Know that measurement comes first.", "Profile then optimize algorithms and data structures."),
    "gotchas": ("Avoid classic traps (mutable defaults, is vs ==).", "Know mutability, scope, and reference semantics cold."),
    "precedence": ("Look up which operator runs first.", "Use parens when in doubt; know ** and unary bind tight."),
    "builtins": ("Use built-in functions instead of manual code.", "Scan the table when you're about to write a loop."),
    "exceptions_ref": ("Find the right exception type in the hierarchy.", "Catch specific types; don't catch BaseException."),
    "venv": ("Create and use a virtual environment per project.", "pip freeze > requirements.txt; use venv or virtualenv."),
    "debugging": ("Use breakpoint() and print to find bugs.", "Use pdb and cProfile when print isn't enough."),
    "recipes": ("Copy and adapt one-liners for common tasks.", "Invert dicts, merge configs, count items — then tweak."),
    "cheatsheet": ("Scan the cheat sheet for quick answers.", "Use it as a refresher; details are in the sections."),
}

# Short TUI hints (beginner, power user); keep each under ~80 chars.
SECTION_HINTS: Mapping[str, Tuple[str, str]] = {
    "variables": ("Tip: Say what you expect before running each cell.", "Tip: Try changing the value and predict which names change."),
    "numbers": ("Guess the result of 0.1 + 0.2 before running.", "Try math.isclose for float comparison."),
    "strings": ("Predict what each slice returns.", "Try rewriting a loop with a str method."),
    "booleans": ("Predict: what is truthy vs falsy for [], None, 0?", "Remember: 'is' for None, '==' for value."),
    "lists": ("Tip: Say what you expect before running each cell.", "Tip: Try rewriting this as a one-liner or comprehension."),
    "tuples": ("What happens if you try to change a tuple?", "Use a tuple as a dict key and see."),
    "dicts": ("Predict the value after .get on a missing key.", "Try merging two dicts with | or **."),
    "sets": ("What happens when you add a duplicate?", "Try set() on a string or list."),
    "structures": ("Create a small dataclass and print it.", "Compare namedtuple vs dataclass for your use."),
    "conditionals": ("Which branch runs? Say it before running.", "Rewrite with match/case or a ternary."),
    "loops": ("Count how many times the loop runs.", "Use enumerate or zip instead of range(len)."),
    "comprehensions": ("Convert a for-loop into a list comp.", "Try a generator expression (parens) and check type."),
    "functions": ("What does this return? Trace the arguments.", "Try a mutable default and see the gotcha."),
    "scope": ("Which x is used: local or global?", "Try nonlocal and see the difference."),
    "lambda": ("Replace a lambda with a def and back.", "When is a list comp clearer than map/filter?"),
    "decorators": ("What runs first: the wrapper or the function?", "Add @wraps and compare __name__."),
    "functools": ("Run the cached function twice; see the speedup.", "Use partial to fix one argument."),
    "classes": ("What is self? Trace one method call.", "Add a __repr__ and print the instance."),
    "inheritance": ("Which method runs: parent or child?", "Prefer composition: pass in a helper."),
    "dunders": ("What triggers __repr__ vs __str__?", "Implement __add__ and use + on your type."),
    "properties": ("Change the attribute and see the setter run.", "Compare memory with and without __slots__."),
    "abcs": ("What must a subclass implement?", "Use Protocol for structural typing."),
    "exceptions": ("Which except block catches this error?", "Add else and finally; see the order."),
    "context": ("What happens if an error occurs inside with?", "Write a tiny context manager with __enter__/__exit__."),
    "custom_errors": ("Catch your exception specifically.", "Add an attribute to the exception."),
    "iterators": ("Consume an iterator twice; what happens?", "Implement __next__ and use in for."),
    "generators": ("Is this evaluated once or on each next()?", "Pipe two generators together."),
    "itertools": ("Replace a loop with chain or islice.", "Build a pipeline: chain -> islice -> list."),
    "files": ("What happens if you don't close? Use with.", "Open with encoding='utf-8' explicitly."),
    "json_csv": ("Load JSON and print the type of the root.", "Write a CSV with DictWriter."),
    "pathlib": ("Use Path('.').cwd() and .glob('*.py').", "Replace string path logic with pathlib."),
    "regex": ("Predict what this pattern matches.", "Compile the pattern and use it twice."),
    "formatting": ("Format a number with commas and 2 decimals.", "Use f'{x:>10}' and see alignment."),
    "datetime": ("What timezone is this datetime in?", "Create a timezone-aware datetime."),
    "collections": ("Use Counter on a list of words.", "Use deque.popleft for a queue."),
    "os": ("Run a simple command with subprocess.run.", "Avoid shell=True; use list of args."),
    "typing": ("Add a type hint and run mypy.", "Use Optional[X] and List[X] correctly."),
    "idioms": ("Find one EAFP and one LBYL in the section.", "Rewrite a snippet the Pythonic way."),
    "performance": ("Time two approaches with timeit.", "Profile first; then optimize one hotspot."),
    "gotchas": ("Which examples surprise you? Run them.", "Fix the mutable default and the is vs ==."),
    "precedence": ("Add parens to make the order explicit.", "Look up ** and unary minus."),
    "builtins": ("Find a built-in that replaces a loop.", "Use any(), all(), or next() in a comp."),
    "exceptions_ref": ("Find the parent of ValueError.", "Don't catch Exception when you need specific."),
    "venv": ("Create a venv and install one package.", "pip freeze and inspect requirements.txt."),
    "debugging": ("Set breakpoint() and step once.", "Run under cProfile and find the hotspot."),
    "recipes": ("Paste one recipe and adapt it.", "Combine two recipes into a small script."),
    "cheatsheet": ("Find one item you didn't know.", "Use as a quick reference for a section."),
}

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


def _get_sections_for_part(part_index: int) -> List[Tuple[str, int, str, int, str]]:
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


def _build_parser() -> "_FaultTolerantParser":
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
    parser.add_argument(
        "--no-save",
        action="store_true",
        help="run quiz without saving progress (CI/shared machines)",
    )

    # ── Positional: bare section name for backward compat ──
    parser.add_argument(
        "section_name",
        nargs="?",
        default=None,
        help=argparse.SUPPRESS,  # Hidden — the -s flag is the documented way
    )

    return parser


def _cli_list() -> None:
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


def _cli_find(term: str) -> None:
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

def _can_use_curses() -> bool:
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


def _syntax_highlight_tokens(line: str) -> List[Tuple[str, str]]:
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


def _strip_leading_docstring(src: str) -> str:
    """Remove a leading triple-quoted docstring from a function source.

    The TUI already renders the function's docstring as teaching content
    above the source code. Showing the docstring again inside the source
    makes the comments appear duplicated in the viewer. This helper
    strips only the first top-level triple-quoted block immediately
    following the def line, if present.
    """
    lines = src.split("\n")
    if not lines:
        return src

    new_lines: List[str] = []
    in_doc = False
    saw_def = False

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.lstrip()

        if not saw_def:
            new_lines.append(line)
            if stripped.startswith("def ") or stripped.startswith("async def "):
                saw_def = True
            i += 1
            continue

        if not in_doc:
            if stripped.startswith('"""') or stripped.startswith("'''"):
                quote = '"""' if stripped.startswith('"""') else "'''"
                # Single-line docstring: def ...: \"\"\"doc\"\"\"
                if stripped.count(quote) >= 2:
                    i += 1
                    # docstring fully consumed on this line
                    break
                in_doc = True
                i += 1
                continue
            else:
                # First non-docstring line after def
                new_lines.append(line)
                i += 1
                break
        else:
            # Inside docstring: look for closing triple quotes
            if '"""' in stripped or "'''" in stripped:
                in_doc = False
                i += 1
                break
            i += 1

    # Append the rest of the lines unchanged
    if i < len(lines):
        new_lines.extend(lines[i:])

    return "\n".join(new_lines)


def _tui_pretty_source_line(line: str) -> str:
    """Transform noisy demo lines into cleaner examples for the TUI viewer.

    Keeps assignments and expressions as-is, but:
      - For common print-based demo lines like:
            print(f"2 + 3   = {2 + 3}")
        show just the inner expression:
            2 + 3
      - For other print() calls that don't follow this pattern, leave the
        line unchanged so advanced demos still show their real code.
    """
    stripped = line.lstrip()

    # Only touch obvious print(...) demo lines
    if not stripped.startswith("print("):
        return line

    # Heuristic: extract the first {...} expression from an f-string print
    m = re.match(r'print\(\s*f["\'].*\{(.+?)\}["\']\s*\)', stripped)
    if not m:
        return line

    expr = m.group(1).strip()
    indent = line[: len(line) - len(stripped)]
    return indent + expr



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

    def __init__(self, stdscr: Any, registry: Mapping[str, Callable[[], None]]) -> None:
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
        self.search_results: List[Tuple[str, int, int]] = []
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

        # For the TUI viewer, prefer the teaching-oriented demo_* function
        # if it exists; fall back to the runtime registry function otherwise.
        func = None
        try:
            demo_name = f"demo_{sec_key}"
            func = globals().get(demo_name)
        except Exception:
            func = None
        if func is None:
            func = self.registry[sec_key]

        def _safe_tokenize(line):
            try:
                return _syntax_highlight_tokens(line)
            except Exception:
                return [(line, "normal")]

        # Global "Big picture" summary for this section (if available)
        overview = SECTION_BIG_PICTURE.get(sec_key)
        if overview:
            self.viewer_lines.append(_safe_tokenize("Big picture:"))
            for line in textwrap.fill(overview, width=max(60, self.w - 10)).split("\n"):
                self.viewer_lines.append(_safe_tokenize("  " + line))
            self.viewer_lines.append(_safe_tokenize(""))
            self.viewer_lines.append(_safe_tokenize("# " + "-" * 60))
            self.viewer_lines.append(_safe_tokenize(""))

        # Section goals (dual-purpose: beginner vs power user)
        goals = SECTION_GOALS.get(sec_key)
        if goals:
            beg, pwr = goals
            self.viewer_lines.append(_safe_tokenize("#* Goal (Beginner): " + beg))
            self.viewer_lines.append(_safe_tokenize("#* Goal (Power User): " + pwr))
            self.viewer_lines.append(_safe_tokenize(""))

        # Docstring next (teaching content specific to the demo)
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

        # Source code (optional in TUI viewer)
        if _TUI_SHOW_SOURCE:
            try:
                src = inspect.getsource(func)
                src = textwrap.dedent(src)
                src = _strip_leading_docstring(src)
                for line in src.split("\n"):
                    pretty = _tui_pretty_source_line(line)
                    self.viewer_lines.append(_safe_tokenize(pretty))
            except (OSError, TypeError):
                self.viewer_lines.append(
                    [("(Source not available -- running from .pyc or frozen)", "comment")]
                )
            except Exception:
                self.viewer_lines.append(
                    [("(Could not read source code)", "comment")]
                )

        # Teaching hints at bottom (beginner + power user, ~80 chars each)
        hints = SECTION_HINTS.get(sec_key)
        if hints:
            self.viewer_lines.append(_safe_tokenize(""))
            self.viewer_lines.append(_safe_tokenize("# " + "-" * 60))
            self.viewer_lines.append(_safe_tokenize("Tip (beginner): " + hints[0]))
            self.viewer_lines.append(_safe_tokenize("Tip (power): " + hints[1]))

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


def _launch_tui(registry: Mapping[str, Callable[[], None]]) -> None:
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


def _parse_args_and_run() -> None:
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
        run_self_tests(no_save=getattr(args, "no_save", False))
    elif args.find:
        _cli_find(args.find)
    elif args.section_name:
        _run_section_or_suggest(args.section_name)
    else:
        # No flags, no args → launch interactive TUI
        _launch_tui(DEMO_REGISTRY)


def _run_section_or_suggest(name: str) -> None:
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
#* Why this Part matters: Scripts, configs, and APIs all start with variables, numbers, strings, and booleans — get these right and the rest stacks.
#* TL;DR for power users:
#* • Variables are names; assignment never copies. int is unbounded, float approximate; use Decimal for money.
#* • str is immutable; slicing returns new strings. Only None, False, 0, '', (), [], {} are falsy.

# %% 01 — Variables & Types
#* Goal (Beginner): Understand that variables are names for values and how assignment works.
#* Goal (Power User): Internalize that assignment never copies and when that matters.
#* Big idea: names point at objects (not boxes); shared references vs copies are what to "see" here.
#! Power tip: assignment never copies; a = b makes both names point at the same object — matters for lists/dicts.
# Global idea: names point at objects (not boxes),
# and shared references vs copies are the core thing to “see” here.
def demo_variables():
    """01 — Variables & Types: names pointing to objects.

    Big picture:
      - A “variable” is just a name pointing at a value in memory.
      - Two names can point at the same value (shared reference) or at
        separate-but-equal values (copies).
      - Many beginner bugs come from accidentally sharing a changeable
        value (like a list or dict) between multiple names.
    """
    _header(1, "VARIABLES & TYPES")

    # Think of a variable as a sticky note with a name on it.
    # The arrow (=) tells Python which value that sticky note should point to.
    name = "Stewart"  # the sticky note called "name" now points at this text
    age = 49          # "age" points at the number 49

    # type(thing).__name__ asks “what kind of thing is this?” in plain English.
    print("name:", name, "type:", type(name).__name__)
    print("age: ", age,  "type:", type(age).__name__)

    # A list is an ordered collection of values written in square brackets.
    # Here we create ONE list object and give it the sticky note "a".
    a = [1, 2, 3]

    # Now we make a SECOND sticky note "b" that points at the SAME list.
    b = a            # no new list is created here
    #? What do you think a and b will show after the next line? Same list or two lists?

    # When we change the list through "b", we are changing the single shared list.
    b.append(4)
    print("\nshared list a:", a)
    print("shared list b:", b)
    print("same object?", id(a) == id(b))  # True → both names point at one list

    # If we really want a separate list, we must ask Python to make a copy.
    c = a.copy()     # new list that starts with the same contents as a
    c.append(5)      # only c changes this time
    print("\ncopy c:", c)
    print("original a:", a)

    # Try this: change a to [10, 20, 30], run again, and watch b and c.


# %% #* Try this (Beginner)
# 1. Change a to [10, 20, 30] and run the demo again; watch what b and c print.
# 2. Create d = a.copy(), then d.append(99). Print a and d — is a unchanged?
# 3. Try x = "hi"; y = x; y = y + "!" then print(x). Does x change? Why?
# %% #* Speed run (Power User)
# 1. In one line, build a list of three names and assign it to both p and q; mutate via q; confirm p changed.
# 2. Write a line that makes an independent copy of a list L (without using .copy()) using slicing.
# %% #* Answers:
# Beginner: (1) b follows a so both show [10,20,30,4]; c is a copy. (2) a is unchanged; d is a new list. (3) x stays "hi" — strings are immutable; y = y + "!" creates a new string.
# Power: (1) p = q = ["a","b","c"]; q.append("d"); print(p) → same list. (2) L_copy = L[:]


# %% 02 — Numbers & Math
#* Goal (Beginner): Use integers and floats safely and know when they behave oddly.
#* Goal (Power User): Know int/float/Decimal trade-offs and use math.isclose for floats.
#* Big idea: ints are exact and unbounded; floats are fast but approximate — 0.1 + 0.2 != 0.3 in float.
#! Power tip: use math.isclose for float comparison; use Decimal for money or exact base-10.
# Global idea: ints are exact and unbounded, floats are approximate,
# and Decimal / math.isclose are the tools to reason safely about numbers.
def demo_numbers():
    """02 — Numbers & Math: ints vs floats vs Decimal.

    Big picture:
      - Python integers are exact and can grow arbitrarily large.
      - Floats trade exactness for speed and range; many decimals cannot
        be represented exactly, so equality checks are fragile.
      - For serious work, you combine `math.isclose` (tolerant compare)
        and `Decimal` (exact base‑10 arithmetic) to avoid surprises.
    """
    _header(2, "NUMBERS & MATH")

    # Integers are whole numbers (…,-2,-1,0,1,2,…). In Python they can grow
    # as big as you like — Python will quietly use more memory for you.
    big = 2 ** 1000              # “2 to the power of 1000”
    # We turn the number into text with str(...) so we can count how many digits it has.
    print("2**1000 has", len(str(big)), "digits")

    # Floats are “numbers with a decimal point”. Inside the computer they are
    # stored in binary, which cannot represent 0.1 exactly.
    #? What do you think this prints? True or False?
    print("\n0.1 + 0.2 == 0.3 ?", 0.1 + 0.2 == 0.3)   # looks like it should be True…
    print("0.1 + 0.2 gives     ", 0.1 + 0.2)          # …but the tiny tail proves otherwise

    # math.isclose says “these two floats are close enough” using a small tolerance.
    import math
    print(
        "math.isclose(0.1 + 0.2, 0.3) →",
        math.isclose(0.1 + 0.2, 0.3),
    )

    # Decimal stores decimal digits the way humans write them, so money like
    # $0.10 + $0.20 adds up exactly.
    from decimal import Decimal

    amount = Decimal("0.10") + Decimal("0.20")
    print("\nDecimal('0.10') + Decimal('0.20') =", amount)

    # Try this: change 0.1 and 0.2 to other decimals and see when isclose still helps.


# %% #* Try this (Beginner)
# 1. In the REPL, type 0.1 + 0.2 and then 0.1 + 0.2 == 0.3. What do you get?
# 2. Use math.isclose(0.1 + 0.2, 0.3) and print the result.
# 3. Try int(1e10) and 2**100; confirm integers can be huge.
# %% #* Speed run (Power User)
# 1. Compare two floats with a relative tolerance using math.isclose(a, b, rel_tol=1e-5).
# 2. Use Decimal("0.1") + Decimal("0.2") and print the result; compare to 0.1 + 0.2.
# %% #* Answers:
# Beginner: (1) 0.30000000000000004 and False — float representation. (2) True. (3) Both work; ints are unbounded.
# Power: (1) rel_tol for relative comparison. (2) Decimal gives 0.3 exactly; use for money.


# %% 03 — Strings
#* Goal (Beginner): Create, slice, and combine strings without surprises.
#* Goal (Power User): Use str methods and immutability to write clear, efficient code.
#* Big idea: strings are immutable; slicing and methods return new strings, they never change in place.
#! Power tip: prefer str methods (join, split, strip) and f-strings over concatenation and %.
# Global idea: strings never change once created; slicing is the same
# universal pattern you’ll use on many sequence types, not just text.
def demo_strings():
    """03 — Strings & slicing: index, slice, reverse.

    Big picture:
      - Strings are sequences of characters that never change once created;
        actions that “modify” a string really create a new string.
      - Slicing `[start:stop:step]` is the common language for working
        with any sequence (strings, lists, tuples, ranges, etc.).
      - Once you “see” how indexes map to characters, reversing and
        sub‑selecting pieces of text becomes automatic.
    """
    _header(3, "STRINGS & SLICING")
    text = "Hello, Python"

    # A “string” is just text. repr(text) shows it the way Python sees it,
    # including the quotes, so spaces and punctuation are easy to spot.
    print("text =", repr(text))

    # You can think of a string as a row of letter “slots”.
    # Index 0 is the first slot, index 1 the second, and so on.
    print("\ntext[0]   =", text[0],   " # first character (index 0)")
    print("text[-1]  =", text[-1],  " # last character (index -1: one from the end)")

    # A slice cuts out a piece of the string: text[start:stop]
    # starts at start and stops *before* stop.
    print("text[0:5] =", text[0:5], " # characters 0–4 → 'Hello'")
    print("text[7:]  =", text[7:],  " # from index 7 all the way to the end → 'Python'")

    # Negative indices count from the right; a third “step” part lets you skip.
    print("\ntext[-6:]  =", text[-6:],  " # last 6 characters → 'Python'")
    print("text[::-1] =", text[::-1], " # the whole string, but stepped backwards (reversed)")
    print("text[::2]  =", text[::2],  " # every second character: keep 0,2,4,… and skip the rest")

    # Try this: change text to your name and guess what text[0:3] and text[-2:] are before running.


# %% #* Try this (Beginner)
# 1. Set text to your name; predict text[0:3] and text[-2:] before running.
# 2. Try text[::-1] and text[::2]; say what each does in words.
# 3. Intentionally use an index that is too large (e.g. text[99]) and see the error.
# %% #* Speed run (Power User)
# 1. Reverse a string in one expression (no loop). Check that the original is unchanged.
# 2. Use str.join to combine a list of words with " " and with "-".
# %% #* Answers:
# Beginner: (1) first 3 chars; last 2 chars. (2) reversed; every other char. (3) IndexError — strings don't grow to fit.
# Power: (1) text[::-1]; strings are immutable. (2) " ".join(words); "-".join(words).


# %% 04 — Booleans & None
#* Goal (Beginner): Use True/False and None and write simple conditions.
#* Goal (Power User): Master truthiness, short-circuiting, and the one way to test for None.
#* Big idea: Python asks "is this empty/zero/None?" (truthiness), not "is it exactly True?".
#! Power tip: test for None with "x is None"; use "if x:" for "has content", "if not x:" for empty.
#* Quiz tag: booleans, truthiness, None. See also: 01 Variables, 05 Lists, 07 Dictionaries.
def demo_booleans():
    """04 — Booleans & None: truthiness and 'None' done right.

    Big picture:
      - Python treats a small set of values as *falsy* (False, 0, 0.0, "", [], {}, set(), None, 0j);
        everything else is *truthy*.
      - `None` is a singleton object meaning “no value”; you check it with `is` / `is not`,
        not `==`, because equality can be overloaded.
      - `and` / `or` short-circuit and return one of their operands, which lets you write
        compact defaulting and guard patterns.

    04 — BOOLEANS & NONE

    HOW IT WORKS:
      • In `if` and `while`, Python doesn’t just use True/False literals — it
        treats certain values as *falsy* (False, 0, 0.0, "", [], {}, set(), None, 0j).
      • Everything else is *truthy* (non‑empty, non‑zero values).
      • `None` is a singleton object used to mean “no value”; you test it with
        `is` and `is not`, not `==`.
      • `and` and `or` return one of their operands, not just True/False
        (short‑circuit evaluation).

    WHY IT MATTERS:
      • Lets you write Pythonic checks like `if not items:` instead of
        `if len(items) == 0:`.
      • Prevents subtle bugs when comparing against None with `==` instead
        of `is`.
      • Helps you reason about chained conditions that use `and` / `or`.

    EXAMPLES (code → result):

      bool([])        → False
      bool([0])       → True
      bool("")        → False
      bool(" ")       → True
      bool(0)         → False
      bool(-1)        → True

      items = []
      if not items:   # empty list
          ...         # branch runs

      x = None
      x is None       → True
      x == None       → True  (works, but prefer `is`)

      "" or "default" → "default"
      "hi" or "default" → "hi"
      0 or 42         → 42
      "a" and "b"     → "b"
    """
    _header(4, "BOOLEANS & NONE")
    #? Is [] truthy or falsy? What about [0]? (Python asks "is this empty?" not "are its contents truthy?")
    # When Python sees code like “if something: …”, it quietly asks bool(something).
    # Some values answer “I count as False”, everything else counts as True.
    falsy_values = [False, 0, 0.0, "", [], {}, set(), None, 0j]
    print("Falsy values (all behave like False in an if-statement):")
    for val in falsy_values:
        # str(val) shows how the value prints; bool(val) shows how it behaves in a condition.
        print(f"  bool({str(val):>10}) → {bool(val)}")

    # A few surprising examples of things that count as True.
    print(f"\nbool([0])    → {bool([0])}   ← list is not empty, even though it holds 0")
    print(f"bool(' ')    → {bool(' ')}   ← a space is still one character")
    print(f"bool(-1)     → {bool(-1)}   ← any non‑zero number is True")

    # Instead of writing “len(items) == 0”, Python style is to ask “is this empty?”
    # by using the value directly in an if.
    items = []
    if not items:                           # reads as “if there are no items”
        print("\nPythonic: 'if not items' checks emptiness")

    name = ""
    if not name:                            # reads as “if the name is empty”
        print("Pythonic: 'if not name' checks empty string")

    # None is Python’s special “no value yet” marker.
    x = None
    print(f"\nx is None → {x is None}")     # 'is' asks “are these the very same object?”
    print(f"x == None → {x == None}")       # works, but '==' can be redefined by classes

    # 'or' and 'and' don’t just return True/False — they return one of the original values.
    # This makes it easy to say “use this value, or fall back to that one”.
    print(f"\n'' or 'default'     → {'default'}")           # empty string → use default
    print(f"'hello' or 'default' → {'hello' or 'default'}") # 'hello' is non‑empty → keep it
    print(f"0 or 42              → {0 or 42}")              # 0 is False‑ish → use 42
    print(f"'hello' and 'world'  → {'hello' and 'world'}")  # both True‑ish → last value
    print(f"'' and 'world'       → {'' and 'world'!r}")     # first False‑ish → stop early

    # A very common pattern: provide a default value when the caller passes nothing in.
    def greet(name=None):
        # If name is empty/None, use 'World' instead.
        name = name or "World"
        return f"Hello, {name}"

    print(f"\ngreet()         → {greet()}")
    print(f"greet('Stewart') → {greet('Stewart')}")

    # Try this: call greet("") and see which branch runs (empty string is falsy).


# %% #* Try this (Beginner)
# 1. Call greet("") and see which branch runs (empty string is falsy).
# 2. In the REPL, try bool(""), bool(" "), bool([]), bool([0]). Predict first.
# 3. Write if not score: and set score = 0 — run with score = 0 and with score = 100.
# %% #* Speed run (Power User)
# 1. Use one short-circuit expression to get the first truthy of (None, 0, "", "fallback").
# 2. Write "x is None" and "x == None" in a tiny script; when would they differ for a custom class?
# %% #* Answers:
# Beginner: (1) greet("") uses "World" because "" is falsy. (2) False, True, False, True — container emptiness. (3) Only when score is 0 (or falsy) does the block run.
# Power: (1) None or 0 or "" or "fallback" → "fallback". (2) A class can override __eq__ so == None is True while is None is False; always use is None.


# ═════════════════════════════════════════════════════════════════════════════
# ██████╗  █████╗ ██████╗ ████████╗    ██████╗
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ╚════██╗
# ██████╔╝███████║██████╔╝   ██║        █████╔╝
# ██╔═══╝ ██╔══██║██╔══██╗   ██║       ██╔═══╝
# ██║     ██║  ██║██║  ██║   ██║       ███████╗
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚══════╝
#  DATA STRUCTURES — Your toolbox for organizing information
# ═════════════════════════════════════════════════════════════════════════════
#* Why this Part matters: Real code is full of lists, dicts, and sets; picking the right structure is half the battle.
#* TL;DR for power users:
#* • Lists: ordered, mutable. Tuples: fixed, hashable, great for keys and multi-return. Dicts: O(1) lookup.
#* • Sets: unique, unordered. Prefer dict/set comps and built-ins (in, len) over manual loops.

# %% 05 — Lists
#* Goal (Beginner): Build and change lists with append, slice, and loops.
#* Goal (Power User): Choose lists vs other sequences; avoid mutating while iterating.
#* Big idea: lists are ordered and mutable; indexing and slicing are the same pattern as strings.
#! Power tip: don't mutate a list while iterating over it; build a new list or iterate over a copy/slice.
def demo_lists():
    """
    05 — LISTS

    HOW IT WORKS:
      • Lists are ordered, mutable sequences — you can add, remove, and
        reorder elements in place.
      • Index lookup (`lst[i]`) is O(1); inserting/removing in the middle
        is O(n) because everything after the index must shift.
      • `append()` and `pop()` at the end are O(1) on average and are the
        building blocks for stacks and simple queues.

    WHY IT MATTERS:
      • Lists are the default data structure in Python — you’ll use them
        more than anything else.
      • Understanding the cost of insert vs append helps you avoid
        accidental O(n²) behavior.

    EXAMPLES (code → result):

      nums = [1, 2, 3, 4, 5]
      nums.append(6)          → [1, 2, 3, 4, 5, 6]
      nums.insert(0, 0)       → [0, 1, 2, 3, 4, 5, 6]
      nums.remove(0)          → [1, 2, 3, 4, 5, 6]

      nums[1:4]               → [2, 3, 4]
      nums[::2]               → elements at even indices
      nums[::-1]              → reversed copy

      numbers = [3, 1, 4, 1, 5]
      sorted(numbers)         → [1, 1, 3, 4, 5]        # new list
      list(reversed(numbers)) → [5, 1, 4, 1, 3]

      original = [[1, 2], [3, 4]]
      shallow = original.copy()
      shallow[0].append(99)
      original                   → [[1, 2, 99], [3, 4]]   # inner list shared
    """
    _header(5, "LISTS")

    #* ── CREATING ──
    empty = []
    nums = [1, 2, 3, 4, 5]
    mixed = [1, "two", 3.0, True, None]    # can mix types (but usually don't)

    #* ── ADDING ──
    nums.append(6)              # add to end — fast no matter how long the list is
    nums.insert(0, 0)           #! add at position 0 — Python has to shift the rest; slower on long lists
    nums.extend([7, 8])         # add multiple — same as += [7, 8]

    #* ── REMOVING ──
    nums.remove(0)              # remove first occurrence by VALUE
    popped = nums.pop()         # remove and return last — fast
    popped_at = nums.pop(2)     # remove and return at index — shifting makes this slower on long lists
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

    #* POWER USER: Use a list like a stack (“last thing in is the first out”)
    stack = []
    stack.append("first")
    stack.append("second")
    stack.append("third")
    print(f"\nStack pop: {stack.pop()}")     # "third" — last in, first out

    # Try this: try nums[1:4] = [] and see what happens (or use a slice on the left of =).


# %% #* Try this (Beginner)
# 1. Try nums[1:4] = [] and see what happens (slice on the left of =).
# 2. Append one item to a list, then use .pop() and print the result.
# 3. Intentionally call .index(99) on a list that has no 99; see the error.
# %% #* Speed run (Power User)
# 1. Build a list of squares with a list comprehension: [x**2 for x in range(6)].
# 2. Will sorted(my_list) change my_list? Predict, then run.
# %% #* Answers:
# Beginner: (1) Removes elements at indices 1,2,3. (2) .pop() removes and returns the last item. (3) ValueError — 99 not in list.
# Power: (1) [0,1,4,9,16,25]. (2) No — sorted() returns a new list; list is unchanged.


# %% 06 — Tuples
#* Goal (Beginner): Use tuples for fixed data and multiple return values.
#* Goal (Power User): Know when to choose a list vs tuple in real code (keys, unpacking, immutability).
#* Big idea: tuples are fixed-size and hashable; use them where "this stays the same" matters.
#! Power tip: tuples as dict keys, function multi-return, and in "in" checks are O(1) with set/dict.
def demo_tuples():
    """
    06 — TUPLES

    HOW IT WORKS:
      • Tuples are sequences whose contents you do not change after creating
        them; they stay the same for their whole lifetime.
      • Because they stay the same, Python can use them as dictionary keys and
        set members (unlike lists, which can change).
      • Multiple assignment and unpacking (`a, b = point`) are powered
        by tuples.

    WHY IT MATTERS:
      • Use tuples for fixed collections of values (coordinates, RGB,
        database rows, etc.).
      • Because you never change a tuple, you can pass it around without
        worrying that some other part of the code will modify it.

    EXAMPLES (code → result):

      point = (3, 4)
      single = (42,)
      type(single).__name__        → "tuple"
      type((42)).__name__          → "int"

      x, y = point                 → x = 3, y = 4
      a, b = 1, 2
      a, b = b, a                  → a = 2, b = 1

      (40.7128, -74.0060) as dict key:
        {(40.7128, -74.0060): "New York"}
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

    # Try this: add another (lat, lon) pair to location_data and look it up by key.


# %% 07 — Dictionaries
#* Goal (Beginner): Store and look up key-value pairs with dicts.
#* Goal (Power User): Use dicts as the default data structure; know .get, views, and merge patterns.
#* Big idea: dicts map keys to values with fast lookup; keys must be hashable (no lists).
#! Power tip: .get(key, default) avoids KeyError; dict | other and ** merge; use views for keys/values/items.
#* Quiz tag: dicts, .get, KeyError. See also: 05 Lists, 08 Sets.
def demo_dicts():
    """
    07 — DICTIONARIES

    HOW IT WORKS:
      • Dicts map keys to values like a phone book: you look up one thing
        (the key) to get another (the value), and Python makes this lookup
        very fast under the hood.
      • Keys must be “stable” values that don’t change over time
        (things like strings, numbers, or tuples of those); values can be
        anything.
      • `.get()` and `.setdefault()` are your friends for “maybe present”
        keys.

    WHY IT MATTERS:
      • Dicts are the most important data structure in Python — configs,
        JSON, records, indexes, caches, and more.
      • Understanding dict patterns (counting, grouping, merging) makes
        real‑world code much simpler.

    EXAMPLES (code → result):

      person = {"name": "Stewart", "age": 49}
      person["name"]                 → "Stewart"
      person.get("email")            → None
      person.get("email", "N/A")     → "N/A"

      # Updating:
      person["email"] = "stew@example.com"
      person.update({"age": 50})

      # Counting words:
      counts = {}
      for w in "the cat sat on the mat the cat".split():
          counts[w] = counts.get(w, 0) + 1
      counts                         → {"the": 3, "cat": 2, "sat": 1, ...}

      # Grouping by first letter:
      by_letter.setdefault("A", []).append("Alice")
    """
    _header(7, "DICTIONARIES")

    #* ── CREATING ──
    person = {"name": "Stewart", "age": 49, "city": "Whitsett"}
    from_pairs = dict([("a", 1), ("b", 2)])       # from list of tuples
    from_kwargs = dict(x=10, y=20)                  # keyword style

    #* ── ACCESSING ──
    #? What do you think person.get('email') returns? What about person.get('email', 'N/A')?
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

    # Try this: build a dict that counts how many times each letter appears in "hello world".


# %% #* Try this (Beginner)
# 1. Build a dict that counts how many times each letter appears in "hello world".
# 2. Use .get(key, 0) in a loop to count; then print the dict.
# 3. Try person["missing_key"] and see the error; use .get("missing_key", "N/A") instead.
# %% #* Speed run (Power User)
# 1. Invert a dict: {v: k for k, v in d.items()} (assume unique values).
# 2. Merge two dicts with d1 | d2 (Python 3.9+) or {**d1, **d2}.
# %% #* Answers:
# Beginner: (1) Loop over the string, counts[c] = counts.get(c, 0) + 1. (2) .get returns 0 when key missing. (3) KeyError; .get avoids it.
# Power: (1) New dict with values as keys. (2) | or ** merge; later keys overwrite.


# %% 08 — Sets
#* Goal (Beginner): Store unique items and do simple set math.
#* Goal (Power User): Use sets for membership and dedup; know hashability and set comps.
#* Big idea: sets are unordered and unique; membership is O(1); elements must be hashable.
#! Power tip: set() on a list dedupes; use & | - ^ for intersection, union, difference, symmetric diff.
def demo_sets():
    """
    08 — SETS

    HOW IT WORKS:
      • Sets are unordered collections of unique elements — duplicates
        are automatically removed.
      • Membership checks (`x in my_set`) are very fast even on large sets,
        whereas checking "x in list" can be slow when the list is long.
      • Support set operations: union (`|`), intersection (`&`), difference
        (`-`), and symmetric difference (`^`).

    WHY IT MATTERS:
      • Great for “does this exist?” checks, deduping, and comparing
        collections (e.g., required vs. current skills).
      • Set math makes many logic problems much simpler and more readable.

    EXAMPLES (code → result):

      set([1, 2, 2, 3, 3, 3])   → {1, 2, 3}

      a = {1, 2, 3, 4, 5}
      b = {4, 5, 6, 7, 8}
      a | b                     → {1, 2, 3, 4, 5, 6, 7, 8}
      a & b                     → {4, 5}
      a - b                     → {1, 2, 3}
      a ^ b                     → {1, 2, 3, 6, 7, 8}

      required = {"python", "sql", "git", "docker"}
      have = {"python", "git", "linux"}
      required - have           → {"sql", "docker"}
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

    #  "Is 99999 in here?" — list scans; set looks up in one step
    print(f"\n99999 in big_set → {99999 in big_set}")   # instant

    #* ── PRACTICAL: Finding differences between collections ──
    required = {"python", "sql", "git", "docker"}
    have = {"python", "git", "linux"}
    need = required - have
    print(f"\nSkills to learn: {need}")

    #* ── FROZEN SETS: sets you don’t change (can be dict keys) ──
    frozen = frozenset([1, 2, 3])
    # frozen.add(4)   #! AttributeError — can't modify

    # Try this: build two sets of your own (e.g. favorite fruits vs. today's snacks) and try a - b and a & b.


# %% 09 — Advanced Structures
#* Goal (Beginner): Use namedtuple and dataclass for readable structured data.
#* Goal (Power User): Pick namedtuple/dataclass/defaultdict/Counter by use case.
#* Big idea: namedtuple and dataclass give you "records with names" without full class ceremony.
#! Power tip: dataclass for mutable records; defaultdict for "missing key = default"; Counter for counts.
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

    #* ── NAMEDTUPLE: Tuple with names (lightweight, stays the same) ──
    from collections import namedtuple

    Point = namedtuple("Point", ["x", "y"])
    p = Point(3, 4)
    print(f"NamedTuple: p.x={p.x}, p.y={p.y}")
    print(f"  Still a tuple: p[0]={p[0]}")
    # p.x = 5   #! Can't assign here — namedtuples are not meant to change

    #* ── DATACLASS (Python 3.7+): The modern way to make data holders ──
    from dataclasses import dataclass, field

    @dataclass
    class Employee:
        name: str
        title: str
        salary: float
        skills: list = field(default_factory=list)   #* use default_factory for changeable defaults

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

    # Try this: create a Counter from a string (e.g. "mississippi") and call .most_common(3).


# ═════════════════════════════════════════════════════════════════════════════
# ██████╗  █████╗ ██████╗ ████████╗    ██████╗
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ╚════██╗
# ██████╔╝███████║██████╔╝   ██║        █████╔╝
# ██╔═══╝ ██╔══██║██╔══██╗   ██║        ╚═══██╗
# ██║     ██║  ██║██║  ██║   ██║       ██████╔╝
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚═════╝
#  CONTROL FLOW — Directing the program's path
# ═════════════════════════════════════════════════════════════════════════════
#* Why this Part matters: Branching and looping are how you direct the program; Pythonic style keeps them readable and concise.
#* TL;DR for power users:
#* • match/case for multi-branch; ternary x if c else y. for with enumerate/zip; avoid while when for fits.
#* • Comprehensions > loop-and-append; generator expressions when you need lazy/one-pass.

# %% 10 — Conditionals
#* Goal (Beginner): Write if/elif/else and use simple match/case.
#* Goal (Power User): Use match/case and ternary where they reduce noise.
#* Big idea: conditions choose which branch runs; keep predicates clear and avoid deep nesting.
#! Power tip: match/case for multiple values or patterns; "x if c else y" for one expression.
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

    # Try this: add a new case to handle_command for "drop item" and run it.


# %% 11 — Loops
#* Goal (Beginner): Loop with for and while and use range.
#* Goal (Power User): Use enumerate, zip, and early exit; avoid manual index loops.
#* Big idea: for consumes iterables; enumerate/zip give you index or parallel iteration without range(len).
#! Power tip: for i, x in enumerate(it): ...; for a, b in zip(xs, ys): ...; avoid while when for fits.
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

    # Try this: use enumerate to print only every other fruit (e.g. 0, 2, 4) from the fruits list.


# %% 12 — Comprehensions
#* Goal (Beginner): Write list comprehensions instead of simple loops.
#* Goal (Power User): Use dict/set/gen comps; know when genex beats list comp.
#* Big idea: comprehensions are "build a collection in one expression"; genex is lazy, list comp is eager.
#! Power tip: (x for x in it) is a generator — one-pass, memory-friendly; [...] materializes a list.
#* See also: 05 Lists, 07 Dictionaries, 08 Sets, 27 Generators.
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

    # Try this: write a list comprehension that keeps only words longer than 3 characters from a list of words.


# ═════════════════════════════════════════════════════════════════════════════
# ██████╗  █████╗ ██████╗ ████████╗    ██╗  ██╗
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ██║  ██║
# ██████╔╝███████║██████╔╝   ██║       ███████║
# ██╔═══╝ ██╔══██║██╔══██╗   ██║       ╚════██║
# ██║     ██║  ██║██║  ██║   ██║            ██║
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝            ╚═╝
#  FUNCTIONS — Reusable building blocks
# ═════════════════════════════════════════════════════════════════════════════
#* Why this Part matters: Functions are the unit of reuse; decorators and functools are how pros add behavior without clutter.
#* TL;DR for power users:
#* • Default args evaluated once at def time; use None + assign for mutables. *args/**kwargs for flex APIs.
#* • Decorators wrap functions; use functools.wraps. lru_cache and partial are your friends.

# %% 13 — Function Basics
#* Goal (Beginner): Define functions with arguments and return values.
#* Goal (Power User): Design APIs with *args/**kwargs and mutable default gotchas.
#* Big idea: def binds a name to a callable; default values are evaluated once at definition time.
#! Power tip: mutable default (e.g. def f(x, L=[])) is evaluated once; use def f(x, L=None): L = L or [] (or L = [] if L is None else L).
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

    #! DANGER: A default value that is a list (or dict) is created once and shared across every call!
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

    # Try this: write a function that takes *args and returns their sum. Call it with sum_all(1, 2, 3).


# %% 14 — Scope & Closures
#* Goal (Beginner): See where names are visible (local vs global).
#* Goal (Power User): Apply LEGB and closures; use nonlocal when needed.
#* Big idea: Python looks up names in order: Local, Enclosing, Global, Built-in (LEGB).
#! Power tip: closures capture variables by name; reassigning in inner scope needs nonlocal (or global).
def demo_scope():
    """
    ┌─────────────────────────────────────────────────────────────────────┐
    │  14 — SCOPE & CLOSURES                                             │
    │                                                                     │
    │  Einstein says: "God does not play dice with the universe."        │
    │  Python looks up names in a fixed order: your current function,   │
    │  then any enclosing function, then the module (global), then     │
    │  built-in names. That order is what people mean by "LEGB."       │
    │                                                                     │
    │  A closure is a function that remembers variables from its         │
    │  enclosing scope even after that scope has finished executing.     │
    │  Think of it as a function with a backpack of captured variables.  │
    └─────────────────────────────────────────────────────────────────────┘
    """
    _header(14, "SCOPE & CLOSURES")

    #* ── Where does Python look for a name? (Local → Enclosing → Global → Built-in) ──
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

    # Try this: change the starting value in make_counter_v2(10) to 0 and run again.


# %% 15 — Lambda & Functional
#* Goal (Beginner): Use lambda for tiny one-line functions.
#* Goal (Power User): Know when lambda/map/filter help and when a loop is clearer.
#* Big idea: lambda is a one-expression function; map/filter/reduce apply functions over iterables.
#! Power tip: list comprehensions are often clearer than map/filter; use lambda where a callback is required.
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

    # Try this: use sorted() with key=lambda x: -x to sort a list of numbers descending.


# %% 16 — Decorators
#* Goal (Beginner): Wrap a function to add behavior without changing call sites.
#* Goal (Power User): Write decorators that preserve metadata and take arguments.
#* Big idea: a decorator is a function that takes a function and returns a (usually wrapped) function.
#! Power tip: use functools.wraps(f) inside your wrapper so __name__ and __doc__ are preserved.
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

    # Try this: add a simple decorator that prints "before" and "after" around any function you call.


# %% 17 — Functools
#* Goal (Beginner): Use lru_cache and partial for common patterns.
#* Goal (Power User): Apply wraps, partial, and reduce where they simplify code.
#* Big idea: lru_cache memoizes; partial fixes some arguments; wraps copies metadata to the wrapper.
#! Power tip: @lru_cache(maxsize=None) for pure functions with hashable args; partial for callback APIs.
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

    # Try this: use @lru_cache(maxsize=128) on a function that takes one argument and run it twice with the same value.


# ═════════════════════════════════════════════════════════════════════════════
# ██████╗  █████╗ ██████╗ ████████╗    ███████╗
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ██╔════╝
# ██████╔╝███████║██████╔╝   ██║       ███████╗
# ██╔═══╝ ██╔══██║██╔══██╗   ██║       ╚════██║
# ██║     ██║  ██║██║  ██║   ██║       ███████║
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚══════╝
#  OOP — Object-Oriented Programming
# ═════════════════════════════════════════════════════════════════════════════
#* Why this Part matters: OOP in Python is about data + behavior in one place; dunders and protocols make your types feel native.
#* TL;DR for power users:
#* • Composition over deep inheritance. __repr__ for devs, __str__ for users. Protocols/ABCs for interfaces.
#* • dataclass for data; __slots__ when you have many instances and care about memory.

# %% 18 — Classes
#* Goal (Beginner): Define classes with __init__ and methods.
#* Goal (Power User): Use classes for data+behavior; prefer composition.
#* Big idea: a class is a blueprint; instances get their own data; self is the instance.
#! Power tip: __repr__ should be unambiguous (for devs); __str__ for pretty print; implement __repr__ first.
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

    # Try this: add a method transfer(self, other, amount) that moves money between two accounts.


# %% 19 — Inheritance
#* Goal (Beginner): Reuse code with inheritance and super().
#* Goal (Power User): Prefer composition and shallow hierarchies.
#* Big idea: subclass inherits methods; super() delegates to the parent; override to specialize.
#! Power tip: composition ("has-a") often beats inheritance ("is-a"); use ABCs/Protocols for interfaces.
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

    # Try this: add a Triangle class that also inherits from Shape and give it an area() method.


# %% 20 — Dunder Methods
#* Goal (Beginner): Use __init__ and __repr__ correctly.
#* Goal (Power User): Implement the right dunders so your types feel native.
#* Big idea: dunders hook into language features (+, in, len, with); they're the protocol Python uses.
#! Power tip: __eq__ without __hash__ makes the type unhashable; implement both for value objects in sets/dicts.
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

    # Try this: add __add__ to Vector2D so that v1 + v2 returns a new Vector2D with summed x, y.


# %% 21 — Properties & Slots
#* Goal (Beginner): Use @property for computed attributes.
#* Goal (Power User): Choose @property vs __slots__ by clarity and memory.
#* Big idea: @property lets you run code on attribute access; __slots__ fixes the instance dict for memory.
#! Power tip: __slots__ saves memory when you have many small instances; no __dict__ means no dynamic attributes.
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

    # Try this: add a property that returns the distance from (0,0) for the PointWithSlots instance.


# %% 22 — ABCs & Protocols
#* Goal (Beginner): Understand interfaces and duck typing.
#* Goal (Power User): Use ABCs and Protocol for optional static checks.
#* Big idea: ABCs declare "must implement these methods"; Protocol is structural (duck typing for type checkers).
#! Power tip: from typing import Protocol; class P(Protocol): def method(self): ... then any class with method() satisfies P.
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

    # Try this: define a Protocol that requires a .name attribute and use it as a type hint.


# ═════════════════════════════════════════════════════════════════════════════
# ██████╗  █████╗ ██████╗ ████████╗     ██████╗
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ██╔════╝
# ██████╔╝███████║██████╔╝   ██║       ███████╗
# ██╔═══╝ ██╔══██║██╔══██╗   ██║       ██╔═══██╗
# ██║     ██║  ██║██║  ██║   ██║       ╚██████╔╝
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝        ╚═════╝
#  ERROR HANDLING — Graceful failure
# ═════════════════════════════════════════════════════════════════════════════
#* Why this Part matters: Exceptions and context managers keep failure paths clean and resources safe.
#* TL;DR for power users:
#* • Catch specific exceptions; let generic ones bubble. with for resources; __enter__/__exit__ for custom.
#* • Custom exceptions inherit from Exception; keep hierarchy shallow.

# %% 23 — Exceptions
#* Goal (Beginner): Use try/except to handle errors.
#* Goal (Power User): Catch specific exceptions; use else/finally correctly.
#* Big idea: try/except separates "what we try" from "what we do when it fails"; exceptions bubble until caught.
#! Power tip: except Exception (not BaseException); use else for code that runs only when no exception; finally always runs.
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

    # Try this: wrap a division (a / b) in try/except and catch ZeroDivisionError; print a friendly message.


# %% 24 — Context Managers
#* Goal (Beginner): Use with for files and locks.
#* Goal (Power User): Write __enter__/__exit__ or use contextlib.
#* Big idea: with guarantees setup and teardown; the context manager runs __enter__ then __exit__ (even on exception).
#! Power tip: @contextlib.contextmanager + yield is the quick way to write a manager; __exit__ receives exception info.
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

    # Try this: use the Timer context manager around a loop that runs 1000 times to see the elapsed time.


# %% 25 — Custom Exceptions
#* Goal (Beginner): Define your own exception types.
#* Goal (Power User): Keep custom exception hierarchies shallow and named clearly.
#* Big idea: subclass Exception (or a specific built-in); raise and catch by type; add attributes for details.
#! Power tip: one module or package of custom exceptions; inherit from ValueError/TypeError when that fits.
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

    # Try this: add a custom exception TimeoutError that inherits from AppError and raise it in a try block.


# ═════════════════════════════════════════════════════════════════════════════
# ██████╗  █████╗ ██████╗ ████████╗    ███████╗
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ╚════██║
# ██████╔╝███████║██████╔╝   ██║          ██╔╝
# ██╔═══╝ ██╔══██║██╔══██╗   ██║         ██╔╝
# ██║     ██║  ██║██║  ██║   ██║         ██║
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝         ╚═╝
#  ITERATORS & GENERATORS — Lazy evaluation
# ═════════════════════════════════════════════════════════════════════════════
#* Why this Part matters: Iterators and generators power streaming and pipelines; itertools is the toolbox.
#* TL;DR for power users:
#* • Iterators: __iter__ + __next__; for consumes them. Generators: yield = lazy; one-pass only.
#* • itertools.chain, islice, groupby for pipelines; avoid materializing huge lists.

# %% 26 — Iterators
#* Goal (Beginner): See how for loops consume iterables.
#* Goal (Power User): Implement __iter__/__next__ when you need custom streaming.
#* Big idea: iterables have __iter__; iterators also have __next__; for calls both; iterators are one-pass.
#! Power tip: iter(it) gets an iterator; calling next() exhausts it; a second for would see nothing.
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

    # Try this: change Countdown(5) to Countdown(10) and run; then iterate over the same Countdown(10) twice in a row and see the second loop is empty.


# %% 27 — Generators
#* Goal (Beginner): Use yield to produce values one at a time.
#* Goal (Power User): Build lazy pipelines and avoid materializing huge lists.
#* Big idea: a function with yield is a generator; it runs until the first yield, then pauses until next().
#! Power tip: generator expressions (x for x in it) are one-pass and memory-friendly; list(gen) materializes.
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

    # Try this: write a generator that yields the first n even numbers (0, 2, 4, ...) and take the first 5 with list(...).


# %% 28 — itertools
#* Goal (Beginner): Use a few itertools functions for common loops.
#* Goal (Power User): Compose chain, islice, groupby for iterator pipelines.
#* Big idea: itertools returns iterators (lazy); chain, islice, cycle, groupby are building blocks.
#! Power tip: chain.from_iterable(iterables) avoids unpacking; islice(it, n) takes first n without consuming all.
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

    # Try this: use it.chain to combine two lists, then use it.islice to take only the first 3 elements.


# ═════════════════════════════════════════════════════════════════════════════
# ██████╗  █████╗ ██████╗ ████████╗     █████╗
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ██╔══██╗
# ██████╔╝███████║██████╔╝   ██║       ╚█████╔╝
# ██╔═══╝ ██╔══██║██╔══██╗   ██║       ██╔══██╗
# ██║     ██║  ██║██║  ██║   ██║       ╚█████╔╝
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝        ╚════╝
#  FILE I/O & DATA — Reading and writing the world
# ═════════════════════════════════════════════════════════════════════════════
#* Why this Part matters: Files, JSON, and paths are how Python talks to the world; pathlib and context managers keep it safe.
#* TL;DR for power users:
#* • Open files with with; use pathlib for paths. json.load/dump; csv.DictReader/DictWriter for CSV.
#* • Encoding: specify encoding='utf-8' explicitly for portability.

# %% 29 — File Operations
#* Goal (Beginner): Open, read, write, and close files safely.
#* Goal (Power User): Use with and pathlib; specify encoding.
#* Big idea: open() returns a file object; with closes it even on error; always pass encoding for text.
#! Power tip: Path from pathlib is preferred over string paths; open(Path(...), encoding='utf-8').
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

    # Try this: open a file in 'a' mode and append one more line, then read the file and print it.


# %% 30 — JSON & CSV
#* Goal (Beginner): Read and write JSON and CSV files.
#* Goal (Power User): Use json load/dump and csv.DictReader/Writer; handle encoding.
#* Big idea: json turns dict/list/str/numbers to text and back; CSV is row-based, use DictReader for headers.
#! Power tip: json.dumps(obj, indent=2) for readable files; csv.DictWriter with fieldnames for clean writes.
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

    # Try this: use json.dumps with indent=2 on a small dict and print the result.


# %% 31 — Pathlib
#* Goal (Beginner): Use Path objects instead of string paths.
#* Goal (Power User): Use pathlib everywhere for portable, readable paths.
#* Big idea: Path is an object that knows how to join, exists(), glob, read_text; / operator joins.
#! Power tip: Path.cwd(), path.iterdir(), path.glob('*.py'), path.read_text(encoding='utf-8').
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

    # Try this: use Path.home() / "Desktop" (or "Documents") and check .exists().


# ═════════════════════════════════════════════════════════════════════════════
# ██████╗  █████╗ ██████╗ ████████╗     █████╗
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ██╔══██╗
# ██████╔╝███████║██████╔╝   ██║       ╚██████║
# ██╔═══╝ ██╔══██║██╔══██╗   ██║        ╚═══██║
# ██║     ██║  ██║██║  ██║   ██║       █████╔╝
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚════╝
#  TEXT MASTERY — Regex, formatting, dates
# ═════════════════════════════════════════════════════════════════════════════
#* Why this Part matters: Regex, formatting, and datetime cover most text and time tasks in the wild.
#* TL;DR for power users:
#* • re: findall, search, sub; compile for repeated use. f-strings and .format for formatting.
#* • datetime: timezone-aware when you care; use datetime.timezone.utc or zoneinfo.

# %% 32 — Regex
#* Goal (Beginner): Match and find patterns in text with re.
#* Goal (Power User): Compile for repeated use; know character classes and groups.
#* Big idea: re compiles a pattern; search/findall/sub apply it; raw strings r'...' avoid backslash surprises.
#! Power tip: re.compile(pattern) when using the same pattern in a loop; capture groups with ().
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

    # Try this: use re.findall(r'\d+', 'I have 2 apples and 5 oranges') and print the result.


# %% 33 — String Formatting
#* Goal (Beginner): Format strings with f-strings and .format.
#* Goal (Power User): Use alignment, width, and number formats where needed.
#* Big idea: f'{x}' and .format() interpolate values; :.2f, :>10, :, for decimals, alignment, thousands.
#! Power tip: f'{n:,.2f}' for money; f'{s:>20}' right-align; f'{x:.2%}' for percentage.
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

    # Try this: format the number 1234567.89 with commas and two decimal places using an f-string.


# %% 34 — Datetime
#* Goal (Beginner): Work with dates and times using datetime.
#* Goal (Power User): Be timezone-aware; use zoneinfo or timezone.utc.
#* Big idea: datetime has date, time, datetime; naive vs aware (timezone); timedelta for duration.
#! Power tip: from zoneinfo import ZoneInfo; dt.astimezone(ZoneInfo('UTC')) for conversion.
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

    # Try this: create a date one week ago with today - timedelta(days=7) and print it.


# ═════════════════════════════════════════════════════════════════════════════
# ██████╗  █████╗ ██████╗ ████████╗    ██╗ ██████╗
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ██║██╔═══██╗
# ██████╔╝███████║██████╔╝   ██║       ██║██║   ██║
# ██╔═══╝ ██╔══██║██╔══██╗   ██║       ██║██║   ██║
# ██║     ██║  ██║██║  ██║   ██║       ██║╚██████╔╝
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚═╝ ╚═════╝
#  STANDARD LIBRARY POWER TOOLS
# ═════════════════════════════════════════════════════════════════════════════
#* Why this Part matters: collections, os, subprocess, and typing are the stdlib power tools you reach for daily.
#* TL;DR for power users:
#* • deque for queues/stacks; Counter for counts; ChainMap for layered config.
#* • subprocess.run with capture_output=True; avoid shell=True when possible.

# %% 35 — Collections
#* Goal (Beginner): Use deque, Counter, and OrderedDict when they fit.
#* Goal (Power User): Reach for collections before reinventing with dict/list.
#* Big idea: deque is list-like with fast append/pop from both ends; Counter counts; ChainMap layers dicts.
#! Power tip: Counter(list_of_items).most_common(n); deque(maxlen=k) for a sliding window.
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

    # Try this: create a deque, append a few items, then use .popleft() and .pop() and print the results.


# %% 36 — OS & Subprocess
#* Goal (Beginner): Run shell commands and use os for paths/env.
#* Goal (Power User): Use subprocess.run; avoid shell=True when possible.
#* Big idea: subprocess.run() runs another program; capture_output=True gets stdout/stderr; pass a list, not a string.
#! Power tip: subprocess.run([cmd, arg1], check=True, capture_output=True, text=True); shell=True is a security risk.
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

    # Try this: run subprocess.run(["ls", "-la"], capture_output=True, text=True) and print .stdout (or use "dir" on Windows).


# %% 37 — Typing & Type Hints
#* Goal (Beginner): Add type hints to function signatures.
#* Goal (Power User): Use typing for generics and Protocol; run mypy.
#* Big idea: annotations don't run at runtime; they document and enable static checkers (mypy, pyright).
#! Power tip: Optional[X] = Union[X, None]; List[str], Dict[K,V]; Protocol for structural typing.
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

    # Try this: add a type hint to a function that takes a list of strings and returns the longest one.


# ═════════════════════════════════════════════════════════════════════════════
# ██████╗  █████╗ ██████╗ ████████╗    ██╗  ██╗
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ██║ ██╔╝
# ██████╔╝███████║██████╔╝   ██║       █████╔╝
# ██╔═══╝ ██╔══██║██╔══██╗   ██║       ██╔═██╗
# ██║     ██║  ██║██║  ██║   ██║       ██║  ██╗
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═╝
#  PYTHONIC PATTERNS — The edge
# ═════════════════════════════════════════════════════════════════════════════
#* Why this Part matters: Idioms, performance, and gotchas separate readable, fast code from surprising bugs.
#* TL;DR for power users:
#* • EAFP over LBYL. Unpacking, with, and comprehensions over manual loops.
#* • Measure first; optimize algorithms and data structures before micro-optimizing.

# %% 38 — Idioms
#* Goal (Beginner): Recognize common Pythonic patterns.
#* Goal (Power User): Use EAFP, unpacking, and with routinely.
#* Big idea: "Easier to Ask Forgiveness than Permission" — try then except; unpack for clarity.
#! Power tip: for k, v in d.items(); a, *rest = seq; try/except for control flow, not just errors.
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

    # Try this: use dict(zip(keys, values)) to build a small lookup table from two lists you choose.


# %% 39 — Performance
#* Goal (Beginner): Know that measurement comes first.
#* Goal (Power User): Profile then optimize algorithms and data structures.
#* Big idea: don't guess — use timeit for snippets, cProfile for whole runs; fix the bottleneck.
#! Power tip: the right algorithm and data structure beat micro-optimization; avoid premature optimization.
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

    # Try this: time a list comprehension vs a for-loop that appends (use time.perf_counter() and a large N).


# %% 40 — Gotchas
#* Goal (Beginner): Avoid classic traps (mutable defaults, is vs ==).
#* Goal (Power User): Know mutability, scope, and reference semantics cold.
#* Big idea: mutable default args, is vs ==, late-binding closures, and "list += vs list = list +" trip people up.
#! Power tip: x is None for None; == for value; default=None then if x is None: x = [] inside the function.
#* Quiz tag: mutability, default args, is vs ==. See also: 01 Variables, 05 Lists, 13 Function Basics.
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

    #* ── GOTCHA 1: Default argument that is a list or dict is shared across every call ──
    print("1. Default argument that is a list or dict is shared across every call:")
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

    #* ── GOTCHA 5: Strings never change in place ──
    print("\n5. Strings never change in place:")
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

    # Try this: fix the append_to function using the None-default pattern and verify the second call returns ['b'] only.


# ═════════════════════════════════════════════════════════════════════════════
# ██████╗  █████╗ ██████╗ ████████╗    ██╗██████╗
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ██║╚════██╗
# ██████╔╝███████║██████╔╝   ██║       ██║ █████╔╝
# ██╔═══╝ ██╔══██║██╔══██╗   ██║       ██║██╔═══╝
# ██║     ██║  ██║██║  ██║   ██║       ██║███████╗
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚═╝╚══════╝
#  CHEAT SHEET — Quick reference
# ═════════════════════════════════════════════════════════════════════════════
#* Why this Part matters: The appendix is the cheat sheet: everything at a glance.
#* TL;DR for power users:
#* • Cheat sheet: quick scan; details live in the sections above.

# %% 41 — Quick Reference  (Appendix: section 47)
#* Goal (Beginner): Scan the cheat sheet for quick answers.
#* Goal (Power User): Use it as a refresher; details are in the sections.
#* Big idea: one-page scan for syntax and patterns; dive into the section for "why".
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

    # Try this: pick one pattern from the cheat sheet (e.g. dict(zip(keys, values))) and use it in a 3-line script.




# ═══════════════════════════════════════════════════════════════════════════════
# ██████╗  █████╗ ██████╗ ████████╗    ██╗██████╗
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ██║╚════██╗
# ██████╔╝███████║██████╔╝   ██║       ██║ █████╔╝
# ██╔═══╝ ██╔══██║██╔══██╗   ██║       ██║██╔═══╝
# ██║     ██║  ██║██║  ██║   ██║       ██║███████╗
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚═╝╚══════╝
#  REFERENCE TABLES — Ctrl+F heaven
# ═══════════════════════════════════════════════════════════════════════════════
#* Why this Part matters: Reference tables are Ctrl+F heaven when you need precedence, built-ins, or the exception tree.
#* TL;DR for power users:
#* • Precedence: ** then * / // % then + -; use parens when in doubt.
#* • Know the exception tree so you don't catch BaseException or mask bugs.

# %% 41 — Operator Precedence
#* Goal (Beginner): Look up which operator runs first.
#* Goal (Power User): Use parens when in doubt; know ** and unary bind tight.
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

    # Try this: try 2 + 3 * 4 and (2 + 3) * 4 in the REPL and see how precedence changes the result.

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
#* Goal (Beginner): Use built-in functions instead of manual code.
#* Goal (Power User): Scan the table when you're about to write a loop.
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
    frozenset(x)      → set you do not plan to change
    bytes(x)          → bytes of data that stay the same
    bytearray(x)      → bytes of data you can change in place
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

    # Try this: in the REPL, try zip([1,2], ['a','b','c']) and list(zip(...)) to see how zip stops at the shortest.


# %% 43 — Exception Hierarchy
#* Goal (Beginner): Find the right exception type in the hierarchy.
#* Goal (Power User): Catch specific types; don't catch BaseException.
#* See also: 23 Exceptions, 25 Custom Exceptions.
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

    # Try this: write a try/except that catches LookupError and prints "missing key or index".



# ═══════════════════════════════════════════════════════════════════════════════
# ██████╗  █████╗ ██████╗ ████████╗    ██╗██████╗
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ██║╚════██╗
# ██████╔╝███████║██████╔╝   ██║       ██║ █████╔╝
# ██╔═══╝ ██╔══██║██╔══██╗   ██║       ██║ ╚═══██╗
# ██║     ██║  ██║██║  ██║   ██║       ██║██████╔╝
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚═╝╚═════╝
#  ENVIRONMENT & TOOLING — The stuff around the code
# ═══════════════════════════════════════════════════════════════════════════════
#* Why this Part matters: Virtual envs and debugging tools keep projects isolated and bugs findable.
#* TL;DR for power users:
#* • One venv per project; pip freeze > requirements.txt. breakpoint() and pdb for debugging.
#* • cProfile for hotspots; timeit for small snippets.

# %% 44 — Virtual Environments
#* Goal (Beginner): Create and use a virtual environment per project.
#* Goal (Power User): pip freeze > requirements.txt; use venv or virtualenv.
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

    # Try this: create a new folder, run python3 -m venv .venv inside it, then activate and run pip list.


# %% 45 — Debugging & Profiling
#* Goal (Beginner): Use breakpoint() and print to find bugs.
#* Goal (Power User): Use pdb and cProfile when print isn't enough.
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

    # Try this: add breakpoint() in a small script, run it, and practice 'n', 'p variable_name', and 'c' in pdb.



# ═══════════════════════════════════════════════════════════════════════════════
# ██████╗  █████╗ ██████╗ ████████╗    ██╗██╗  ██╗
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ██║██║  ██║
# ██████╔╝███████║██████╔╝   ██║       ██║███████║
# ██╔═══╝ ██╔══██║██╔══██╗   ██║       ██║╚════██║
# ██║     ██║  ██║██║  ██║   ██║       ██║     ██║
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚═╝     ╚═╝
#  REAL-WORLD RECIPES — Copy-paste solutions
# ═══════════════════════════════════════════════════════════════════════════════
#* Why this Part matters: Recipes are copy-paste solutions for real-world micro-tasks.
#* TL;DR for power users:
#* • One-liners: invert dict, merge configs, count frequencies — see section 46.

# %% 46 — One-Liner Recipes
#* Goal (Beginner): Copy and adapt one-liners for common tasks.
#* Goal (Power User): Invert dicts, merge configs, count items — then tweak.
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

    # Try this: use the "Dedup preserving order" pattern on a list of words and print the result.

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

# NLP-enhanced answer matching
_ANSWER_ALIASES: dict[str, str] = {
    "true": "True", "false": "False", "yes": "True", "no": "False",
    "1": "True", "0": "False",
    "none": "None", "null": "None", "nil": "None",
    "integer": "int", "string": "str", "boolean": "bool",
    "dictionary": "dict", "list": "list", "tuple": "tuple",
    "3.0": "3.0", "5.0": "5.0",
}

_TYPE_PHRASINGS: dict[str, str] = {
    "float": "float", "int": "int", "str": "str", "tuple": "tuple",
    "list": "list", "dict": "dict", "bool": "bool", "set": "set",
    "a float": "float", "floating point": "float", "decimal": "float",
    "an integer": "int", "whole number": "int",
    "a string": "str", "text": "str",
    "a tuple": "tuple", "a list": "list",
    "a dict": "dict", "a dictionary": "dict",
    "a bool": "bool", "a boolean": "bool",
}

# So eval() can resolve True/False/None inside user answers (e.g. (1, [2,3,4], 5) with None)
_SAFE_EVAL_GLOBALS: dict[str, Any] = {
    "__builtins__": {},
    "True": True,
    "False": False,
    "None": None,
}

PROGRESS_SCHEMA_VERSION = 1


def _normalize(text: str) -> str:
    """Strip whitespace, quotes, and normalize Python literals for comparison."""
    t = text.strip()
    if len(t) >= 2 and t[0] == t[-1] and t[0] in ('"', "'"):
        t = t[1:-1]
    return t


def _tokens_match(user_str: str, expected_repr: str) -> bool:
    """Token-level unordered comparison for sets and simple dicts."""
    def tokenize(s: str) -> list:
        s = s.strip().strip("{}").strip()
        return sorted(t.strip() for t in s.split(",") if t.strip())

    try:
        return tokenize(user_str) == tokenize(expected_repr)
    except Exception:
        return False


def _hint_tier(user_input: str, expected: Any) -> Optional[str]:
    """Return a short hint if the answer was close or right type; else None."""
    norm = _normalize(user_input)
    exp_norm = _normalize(repr(expected))
    ratio = SequenceMatcher(None, norm, exp_norm).ratio()
    if ratio >= 0.60:
        return "  (Almost! You were close — check the exact syntax.)"
    try:
        user_val = eval(user_input.strip(), _SAFE_EVAL_GLOBALS, {})
        if type(user_val) == type(expected) and user_val != expected:
            return f"  (Right type ({type(expected).__name__}), wrong value — good instinct!)"
    except Exception:
        pass
    return None


# %% Self-Test
def run_self_tests(no_save: bool = False) -> tuple[int, int]:
    """
    Interactive quiz — type your prediction, get instant feedback.

    Teaches through encouragement: when you miss one, the explanation
    helps you understand WHY, not just WHAT.  Designed so you walk
    away smarter every time, even on a perfect score.

    If no_save is True, progress is not written to ~/.python_poweruser_progress.json (CI/shared machines).
    """

    # ── Quiz questions ──────────────────────────────────────────────────
    # (name, code_shown, answer, section, teach_right, teach_wrong, difficulty)
    #  difficulty: "beginner" | "intermediate" | "advanced"
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
            "         stop is where you STOP (not where you include).",
            "beginner",
        ),
        (
            "Negative index",
            "[10, 20, 30, 40][-2]",
            [10, 20, 30, 40][-2],
            "lists",
            "Exactly. Negative indices count from the end: -1 is last, -2 is second-last.",
            "Close — negative indices count backward from the end.\n"
            "         -1 is the last element (40), -2 is second-to-last (30).\n"
            "         Think of it as len(list) + index: 4 + (-2) = index 2.",
            "beginner",
        ),
        (
            "Nested length",
            "len([1, [2, 3], 4])",
            len([1, [2, 3], 4]),
            "lists",
            "Right — [2, 3] is ONE element.  len() counts top-level items, not contents.",
            "Good instinct, but [2, 3] counts as a single element.\n"
            "         The outer list has three items: 1, [2,3], and 4.\n"
            "         len() only counts the top level — it doesn't peek inside.",
            "beginner",
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
            "         which would raise a KeyError.",
            "beginner",
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
            "         'if my_list:' instead of 'if len(my_list) > 0:'.",
            "beginner",
        ),
        (
            "Bool of [0]",
            "bool([0])",
            bool([0]),
            "booleans",
            "Nice catch — the list isn't empty, so it's truthy. The 0 inside doesn't matter.",
            "Python asks 'is the container empty?' not 'are the contents truthy?'\n"
            "         [0] has one element, so the list is not empty → True.",
            "intermediate",
        ),
        (
            "Division type",
            "type(10 / 2).__name__",
            type(10 / 2).__name__,
            "numbers",
            "Got it — / ALWAYS returns float in Python 3, even for 10/2.  Use // for int.",
            "Careful — in Python 3, / always gives you a float.\n"
            "         Even 10 / 2 = 5.0, not 5.  This changed from Python 2.\n"
            "         If you want integer division, use //: 10 // 2 = 5.",
            "beginner",
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
            "         because floor() goes toward negative infinity.",
            "beginner",
        ),
        (
            "Ternary",
            '"yes" if "" else "no"',
            "yes" if "" else "no",
            "conditionals",
            "Exactly — empty string is falsy, so the else branch fires.",
            "Remember Python's truthiness: empty string '' is falsy.\n"
            "         The ternary pattern is: VALUE_IF_TRUE if CONDITION else VALUE_IF_FALSE.\n"
            "         Since '' is falsy, the condition fails → 'no'.",
            "beginner",
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
            "         Once you see it, you never forget it.",
            "intermediate",
        ),
        (
            "Not a tuple",
            "type((42)).__name__",
            type((42)).__name__,
            "tuples",
            "Exactly — no comma, no tuple.  (42) is just 42 in parentheses.",
            "This is the flip side of the comma rule: without a trailing comma,\n"
            "         parentheses are just grouping.  (42) == 42, which is an int.\n"
            "         To make a single-element tuple: (42,) — note the comma.",
            "intermediate",
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
            "         n numbers starting from 0.",
            "beginner",
        ),
        (
            "Chained compare",
            "1 < 2 < 3",
            1 < 2 < 3,
            "conditionals",
            "Yes — Python chains comparisons naturally.  It means (1<2) and (2<3).",
            "Python lets you chain comparisons like math notation.\n"
            "         1 < 2 < 3 means (1 < 2) AND (2 < 3) — both True → True.\n"
            "         This works with any comparisons: a <= b < c == d.",
            "beginner",
        ),
        (
            "String repeat",
            '"ha" * 3',
            "ha" * 3,
            "strings",
            "Right — * repeats strings.  Works on lists too: [0] * 5 = [0, 0, 0, 0, 0].",
            "The * operator repeats sequences.  'ha' * 3 = 'hahaha'.\n"
            "         Works on lists too: [0] * 3 = [0, 0, 0].\n"
            "         But be careful when the repeated item is a list or dict:\n"
            "         [[]] * 3 creates three references to the SAME inner list.",
            "beginner",
        ),
        (
            "Substring",
            '"py" in "python"',
            "py" in "python",
            "strings",
            "Yes — 'in' checks for substring containment in strings.",
            "The 'in' operator checks for substrings in strings.\n"
            "         'py' appears at the start of 'python' → True.\n"
            "         For lists, 'in' checks for element membership instead.",
            "beginner",
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
            "         Result: {1: 'a', 2: 'c'}.",
            "intermediate",
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
            "         where you need the value AND the test.",
            "intermediate",
        ),
        (
            "Set intersection",
            "{1,2,3} & {2,3,4}",
            {1,2,3} & {2,3,4},
            "sets",
            "Right — & gives you elements in BOTH sets.  Set math is underrated.",
            "& is set intersection — elements that appear in BOTH sets.\n"
            "         {1,2,3} and {2,3,4} share 2 and 3 → {2, 3}.\n"
            "         Other set ops: | (union), - (difference), ^ (symmetric diff).",
            "beginner",
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
            "         Works anywhere: first, *rest = [1,2,3] → rest = [2,3].",
            "intermediate",
        ),
        (
            "Default list/dict shared",
            "def f(x=[]):\n             x.append(1)\n             return x\n"
            "         f(); f(); f()  — what does the last call return?",
            [1, 1, 1],
            "gotchas",
            "You spotted the trap! Default args are evaluated ONCE — the same list persists.",
            "This is Python's most famous gotcha.  Default arguments are\n"
            "         evaluated ONCE when the function is defined, not on each call.\n"
            "         So every call to f() appends to the SAME list object.\n"
            "         After three calls: [1, 1, 1].\n"
            "         Fix: use 'def f(x=None): x = x or []'.",
            "advanced",
        ),
    ]

    def _check_answer(user_input: str, expected: Any) -> bool:
        """Compare user's text answer against the expected Python value.

        Order: alias norm → type phrasings → direct repr → eval → token (set/dict)
        → float tolerance → fuzzy difflib.
        """
        raw = user_input.strip()
        if not raw:
            return False

        norm = _normalize(raw)
        exp_str = repr(expected)
        exp_norm = _normalize(exp_str)

        # 1. Alias normalization (restrict yes/no and 1/0 to bool-expected only)
        norm_lower = norm.lower()
        if norm_lower in ("yes", "no") and not isinstance(expected, bool):
            pass
        elif norm_lower in _ANSWER_ALIASES:
            if norm_lower in ("1", "0") and not isinstance(expected, bool):
                pass
            else:
                norm = _ANSWER_ALIASES[norm_lower]

        # 2. Type-name phrasing (when expected is a type name string)
        if isinstance(expected, str) and expected in {"float", "int", "str", "tuple", "list", "dict", "bool", "set"}:
            norm = _TYPE_PHRASINGS.get(norm.lower(), norm)

        # 3. Direct match against repr
        if norm == exp_norm:
            return True

        # 4. eval()-based match (safe globals so True/False/None resolve in tuples, etc.)
        try:
            user_val = eval(raw, _SAFE_EVAL_GLOBALS, {})
            if user_val == expected:
                return True
        except Exception:
            pass

        # 5. Token-order-insensitive (sets/dicts) when earlier checks failed
        if isinstance(expected, (set, dict)) and "{" in exp_str:
            if _tokens_match(raw, exp_str):
                return True

        # 6. Float tolerance
        if isinstance(expected, float):
            try:
                return math.isclose(float(norm), expected, rel_tol=1e-6, abs_tol=1e-6)
            except (ValueError, TypeError):
                pass
        if isinstance(expected, int):
            try:
                return int(norm) == expected
            except (ValueError, TypeError):
                pass

        # 7. Fuzzy difflib (last resort; only for longer answers to avoid type-name false positives)
        ratio = SequenceMatcher(None, norm, exp_norm).ratio()
        if len(exp_norm) >= 6 and ratio >= 0.80:
            return True

        return False

    # ── Spaced-repetition: load progress (schema-aware), reorder full list ─────
    progress_path = Path.home() / ".python_poweruser_progress.json"
    prev_weak: list[str] = []
    prev_missed_questions: list[str] = []
    try:
        if progress_path.exists():
            data = json.loads(progress_path.read_text(encoding="utf-8"))
            if data.get("schema_version", 0) != PROGRESS_SCHEMA_VERSION:
                data = {"schema_version": PROGRESS_SCHEMA_VERSION, "sessions": []}
            sessions = data.get("sessions", [])
            if sessions:
                last = sessions[-1]
                score, total_prev = last.get("score", 0), last.get("total", 20)
                date_prev = last.get("date", "?")
                prev_weak = last.get("weak_sections", [])
                prev_missed_questions = last.get("missed_questions", [])
                print(f"  Last session: {score}/{total_prev} on {date_prev}.", end="")
                if prev_weak:
                    print(f"  Weak areas: {', '.join(prev_weak)}.")
                    print("  Tip: Questions from those sections will appear first today.")
                else:
                    print()
                # Sort full list so weak sections and previously missed questions come first
                tests = sorted(
                    tests,
                    key=lambda t: (t[3] in prev_weak, t[0] in prev_missed_questions),
                    reverse=True,
                )
    except Exception:
        pass

    # ── Difficulty filter (after reorder so repetition still applies) ─────────
    print("\n" + "─" * 70)
    print("  SELF-TEST QUIZ")
    print("─" * 70)
    try:
        diff_in = input(
            "  Difficulty filter? [A]ll / [B]eginner / [I]ntermediate / [Adv]anced (default: All): "
        ).strip().lower() or "a"
    except (EOFError, KeyboardInterrupt):
        diff_in = "a"
    diff_map = {"a": None, "all": None, "b": "beginner", "beginner": "beginner",
                "i": "intermediate", "intermediate": "intermediate",
                "adv": "advanced", "advanced": "advanced"}
    diff_filter = diff_map.get(diff_in, None)
    filtered_tests = [t for t in tests if t[6] == diff_filter] if diff_filter else tests
    if not filtered_tests:
        filtered_tests = tests
    tests = filtered_tests

    print("  Type your answer for each expression.  No peeking at the REPL!")
    print("  Press Enter with no answer to skip.  Ctrl+C to quit early.\n")

    passed = 0
    skipped = 0
    wrong = 0
    weak_areas = []  # (section_key, question_name) for missed questions
    total = len(tests)

    for i, (name, code, answer, section, teach_right, teach_wrong, _diff) in enumerate(tests, 1):
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
            hint = _hint_tier(user, answer)
            if hint:
                print(hint)
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

        print("\n  Next step: revisit these sections and re‑run the quiz tomorrow.")
        print("  Sections worth revisiting:")
        for sec_key, title in sections_to_review:
            print(f"    → {title}  (python python_poweruser.py -s {sec_key})")

    # ── Append session to progress JSON (unless --no-save) ─────────────────────
    if not no_save:
        try:
            from datetime import date as date_module
            session = {
                "date": date_module.today().isoformat(),
                "score": passed,
                "total": total,
                "weak_sections": list(dict.fromkeys(sec for sec, _ in weak_areas)),
                "missed_questions": [q for _, q in weak_areas],
            }
            data = {"schema_version": PROGRESS_SCHEMA_VERSION, "sessions": []}
            if progress_path.exists():
                data = json.loads(progress_path.read_text(encoding="utf-8"))
                if data.get("schema_version", 0) != PROGRESS_SCHEMA_VERSION:
                    data = {"schema_version": PROGRESS_SCHEMA_VERSION, "sessions": []}
            data.setdefault("sessions", []).append(session)
            progress_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
        except Exception:
            pass

    print(f"\n{'─' * 70}")
    return passed, total


# ═══════════════════════════════════════════════════════════════════════════════
#  DEMO REGISTRY & MAIN
# ═══════════════════════════════════════════════════════════════════════════════

DEMO_REGISTRY: Mapping[str, Callable[[], None]] = {
    # Part 1 — Foundations (each demo_* is a self-contained example)
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


def main() -> None:
    """Entry point used by both `python python_poweruser.py` and the console script."""
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


if __name__ == "__main__":
    main()
