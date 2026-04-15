#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "python_poweruser.py"
OUT = ROOT / "docs" / "content" / "sections.json"


SECTION_HEADER_RE = re.compile(r"^# %%\s+(?P<num>\d{2})\s+—\s+(?P<title>.+?)\s*$")
GOAL_BEGINNER_RE = re.compile(r"^#\*\s+Goal\s+\(Beginner\):\s*(?P<txt>.+?)\s*$")
GOAL_POWER_RE = re.compile(r"^#\*\s+Goal\s+\(Power User\):\s*(?P<txt>.+?)\s*$")
TRY_THIS_HEADER_RE = re.compile(r"^# %%\s+#\*\s+Try this\s+\(Beginner\)\s*$")
SPEED_RUN_HEADER_RE = re.compile(r"^# %%\s+#\*\s+Speed run\s+\(Power User\)\s*$")
ANSWERS_HEADER_RE = re.compile(r"^# %%\s+#\*\s+Answers:\s*$")
PROMPT_RE = re.compile(r"^\s*#\?\s+(?P<q>.+?)\s*$")
DEMO_DEF_RE = re.compile(r"^def\s+demo_(?P<key>[a-z0-9_]+)\s*\(\)\s*:\s*$")


@dataclass
class Section:
    key: str
    number: int
    title: str
    goal_beginner: str
    goal_power: str
    prompts: list[str]
    demo_source: str
    try_this_source: str
    speed_run_source: str


def _grab_block(lines: list[str], start_idx: int, stop_res: list[re.Pattern[str]]) -> tuple[str, int]:
    buf: list[str] = []
    i = start_idx
    while i < len(lines):
        line = lines[i]
        if any(r.match(line) for r in stop_res):
            break
        buf.append(line.rstrip("\n"))
        i += 1
    return "\n".join(buf).rstrip(), i


def _grab_def(lines: list[str], def_idx: int) -> str:
    i = def_idx
    buf: list[str] = []
    buf.append(lines[i].rstrip("\n"))
    i += 1
    while i < len(lines):
        line = lines[i]
        if line.startswith("def ") and not line.startswith("def demo_"):
            break
        if line.startswith("# %% ") and SECTION_HEADER_RE.match(line):
            break
        buf.append(line.rstrip("\n"))
        i += 1
    return "\n".join(buf).rstrip()


def build() -> dict[str, Any]:
    raw = SRC.read_text(encoding="utf-8")
    lines = raw.splitlines(keepends=True)

    # Map: key -> (num, title) from SECTION_META (keeps canonical ordering)
    meta_m = re.search(r"^SECTION_META\s*=\s*\[(?P<body>[\s\S]*?)^\]\s*$", raw, flags=re.MULTILINE)
    if not meta_m:
        raise SystemExit("Could not find SECTION_META in python_poweruser.py")

    meta: list[tuple[str, int, str]] = []
    for m in re.finditer(r'^\s*\("(?P<key>[^"]+)",\s*(?P<num>\d+),\s*"(?P<title>[^"]+)"', meta_m.group("body"), flags=re.MULTILINE):
        meta.append((m.group("key"), int(m.group("num")), m.group("title")))

    # Scan for each section’s content blocks by header markers.
    # We rely on the fact that sections appear in numeric order in the file.
    header_positions: list[tuple[int, int, str]] = []  # (idx, num, title)
    for idx, line in enumerate(lines):
        hm = SECTION_HEADER_RE.match(line.rstrip("\n"))
        if hm:
            header_positions.append((idx, int(hm.group("num")), hm.group("title")))

    header_by_num: dict[int, tuple[int, str]] = {num: (idx, title) for idx, num, title in header_positions}

    demo_by_key: dict[str, str] = {}
    for idx, line in enumerate(lines):
        dm = DEMO_DEF_RE.match(line.rstrip("\n"))
        if dm:
            key = dm.group("key")
            demo_by_key[key] = _grab_def(lines, idx)

    out_sections: list[dict[str, Any]] = []
    for key, num, title in meta:
        if num not in header_by_num:
            continue
        start_idx, _header_title = header_by_num[num]
        end_idx = len(lines)
        # Find the next header after start
        for idx2, num2, _t2 in header_positions:
            if idx2 > start_idx:
                end_idx = idx2
                break

        chunk = [l.rstrip("\n") for l in lines[start_idx:end_idx]]

        goal_beg = ""
        goal_pwr = ""
        prompts: list[str] = []

        try_this_src = ""
        speed_run_src = ""

        for line in chunk:
            gb = GOAL_BEGINNER_RE.match(line)
            if gb:
                goal_beg = gb.group("txt").strip()
            gp = GOAL_POWER_RE.match(line)
            if gp:
                goal_pwr = gp.group("txt").strip()
            pm = PROMPT_RE.match(line)
            if pm:
                prompts.append(pm.group("q").strip())

        # Extract Try this / Speed run blocks (best-effort)
        joined = "\n".join(chunk) + "\n"
        joined_lines = joined.splitlines(keepends=True)
        for i, line in enumerate(joined_lines):
            if TRY_THIS_HEADER_RE.match(line.rstrip("\n")):
                block, _ = _grab_block(
                    joined_lines,
                    i + 1,
                    [SPEED_RUN_HEADER_RE, ANSWERS_HEADER_RE, SECTION_HEADER_RE],
                )
                try_this_src = block
            if SPEED_RUN_HEADER_RE.match(line.rstrip("\n")):
                block, _ = _grab_block(
                    joined_lines,
                    i + 1,
                    [ANSWERS_HEADER_RE, SECTION_HEADER_RE],
                )
                speed_run_src = block

        out_sections.append(
            {
                "key": key,
                "number": num,
                "title": title,
                "goal_beginner": goal_beg,
                "goal_power": goal_pwr,
                "prompts": prompts[:12],
                "demo_source": demo_by_key.get(key, ""),
                "try_this_source": try_this_src.strip(),
                "speed_run_source": speed_run_src.strip(),
            }
        )

    return {
        "source": "python_poweruser.py",
        "generated_by": "tools/build_web_content.py",
        "sections": out_sections,
    }


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    payload = build()
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)} ({len(payload['sections'])} sections)")


if __name__ == "__main__":
    main()

