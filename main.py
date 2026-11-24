#!/usr/bin/env python3
"""One odd occupation, judged blind.

Emits exactly one job title into /output/entry.txt.
Every invocation yields the same string, nothing else.
"""

import os

# A believable trade taken one step too far: hired grief, aimed at
# a pet its bearer never knew, in a miniature ceremony. The role
# sounds plausible at first hearing, then lands as absurd.
ROLE = "Professional Mourner"
CHARGE = "Strangers' Goldfish"
JOB_TITLE = ROLE + " for " + CHARGE


def check_line(candidate: str) -> str:
    cleaned = candidate.strip()
    if not cleaned:
        raise ValueError("entry line is empty")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry must fit on one line")
    if len(cleaned) > 60:
        raise ValueError("entry exceeds 60 characters")
    if "  " in cleaned:
        raise ValueError("entry has a doubled space")
    if len(cleaned.split()) < 3:
        raise ValueError("entry needs at least three words")
    return cleaned


def main() -> None:
    verified = check_line(JOB_TITLE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(verified)


if __name__ == "__main__":
    main()
