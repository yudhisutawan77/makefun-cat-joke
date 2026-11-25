"""Write the competition entry: one line, one cat joke, to entry.txt.

The sealed gate accepts UTF-8 text of 1-200 characters that is not only
whitespace. This program checks the joke against that gate first, then
writes exactly the joke (plus a trailing newline) to the output path.
"""

import os
import sys

ENTRY_TEXT = "My cat knocked my phone off the table, watched it shatter, then looked at me like I'd dropped it."

GATE_MIN = 1
GATE_MAX = 200


def passes_gate(line):
    """True when a line passes the sealed gate: 1-200 chars, not blank."""
    if not isinstance(line, str):
        return False
    if not (GATE_MIN <= len(line) <= GATE_MAX):
        return False
    if not line.strip():
        return False
    return True


def resolve_entry_path():
    """Resolve where entry.txt goes, honouring the documented env vars."""
    out_dir = os.environ.get("ENTRY_OUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    out_path = os.environ.get("ENTRY_OUT")
    if out_path:
        if os.path.isdir(out_path):
            return os.path.join(out_path, "entry.txt")
        return out_path
    return "/output/entry.txt"


def write_entry(line, path):
    """Create parent dirs as needed and write the line plus one newline."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as out_file:
        out_file.write(line + "\n")


def run():
    if not passes_gate(ENTRY_TEXT):
        print(f"entry failed the gate: {len(ENTRY_TEXT)} chars", file=sys.stderr)
        return 1
    destination = resolve_entry_path()
    write_entry(ENTRY_TEXT, destination)
    print(f"wrote {len(ENTRY_TEXT)}-char entry to {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
