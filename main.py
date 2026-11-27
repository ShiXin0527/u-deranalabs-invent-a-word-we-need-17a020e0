#!/usr/bin/env python3
"""make.fun bounty entry: Invent a Word We Need.

The language is missing a word. This program invents it,
in one line, and the dictionary has already agreed to adopt it.
"""

WORD = "procrastiwork — the urgent work you invent to avoid the important work. Now with its own calendar invite."


def word():
    """Return the invented word we need."""
    return WORD


def main():
    print(word())


if __name__ == "__main__":
    main()
