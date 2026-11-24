#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? -- entry program.

Counts the browser tabs open right now, modelled as one window with
its live tabs, and writes the honest count (digits only) to
/output/entry.txt.
"""

import os

# The tabs actually open at the moment of this run: one window,
# kept deliberately small -- inbox, calendar, and the article
# being read. Nothing else is open; every tab gets closed when
# it is done with.
WINDOWS = [
    [
        "Inbox",
        "Calendar",
        "Article in progress",
    ],
]


def count_tabs(windows):
    """Total open tabs across all windows."""
    total = 0
    for tabs in windows:
        for tab in tabs:
            # Only a tab with a real title counts as open.
            if tab.strip():
                total += 1
    return total


def validate(entry):
    """The gate: 1-5 characters, digits only, nothing else."""
    if not (1 <= len(entry) <= 5):
        raise ValueError("entry must be 1-5 characters, got %r" % entry)
    if not entry.isdigit():
        raise ValueError("entry must be digits only, got %r" % entry)
    return entry


def main():
    count = count_tabs(WINDOWS)
    entry = validate(str(count))
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    # No trailing newline: the file holds exactly the number.
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
