#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright © 2023, Matjaž Guštin <dev@matjaz.it> <https://matjaz.it>
# Released under the BSD 3-Clause License

"""DnD-style dice rolling command line utility."""

import re
import secrets  # For fair, unpredictable randomness.

VERSION = '1.0.0'
PATTERN = re.compile(R"([0-9]+)?(?:d([0-9]+))?([+-][0-9]+)?")
HELP_TEXT = """Type your dice rolls in the format `NdS+M`, where:

- `N` is the amount of dice to roll (1 if unspecified)
- `S` are the sides of the die (d20 if unspecified)
- `M` is the modifier to be added to each roll (0 if unspecified)

For example:

- `1` rolls one 20-sided die
- `3d8` rolls three 8-sided dice
- `2d10-3` rolls two 10-sided dice and subtracts three from each result
- `2+3` rolls two 20-sided die and adds three to each result

Multiple entries are allowed in a single line, e.g. `1d8 3d20+2 6d10`.
"""


def repl() -> None:
    """Runs a REPL which parses user-typed dice-rolling commands and
    prints the roll results. The ``help`` command provides an explanation
    on the accepted input format."""
    while True:
        try:
            commands = input("Die> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            break
        if commands in ('exit', 'quit'):
            break
        elif commands in ('v', 'version'):
            print(f"Die, v{VERSION}")
        elif commands in ('?', 'h', 'help'):
            print(f"Die, v{VERSION}")
            print(HELP_TEXT)
        else:
            for command in commands.split():
                try:
                    amount, sides, modifier = parse_roll_cmd(command)
                    rolls = roll_dice(amount, sides, modifier)
                    prompt = f"{amount}d{sides}{modifier:+}\t| "
                    if len(rolls) == 1:
                        print(f"{prompt}{rolls[0]}")
                    else:
                        print(f"{prompt}{rolls}"
                              f" | Min={min(rolls)}"
                              f" | Max={max(rolls)}"
                              f" | Sum={sum(rolls)}")
                except ValueError as e:
                    print(f"Bad command: {str(e)}")


def roll_dice(amount: int = 1,
              sides: int = 20,
              modifier: int = 0) -> list[int]:
    """Generates ``amount`` (secure) random numbers in [1, ``sides``]
    and adds ``modifier`` to each of them.

    The amount must be at least 1, the sides must be at least 2."""
    if amount <= 0:
        raise ValueError("Can't roll no dice.")
    if sides <= 1:
        raise ValueError("Can't roll fewer than 2 sides.")
    return [secrets.randbelow(sides) + 1 + modifier for _ in range(amount)]


def parse_roll_cmd(text: str) -> tuple[int, int, int]:
    """Parses amount (of dice to roll), sides (of the die), and modifier
    (to add-subtract from each roll) from a text string.

    The format is defined in ``PATTERN`` and explained in ``HELP_TEXT``.
    Unspecified fields have defaults 1, 20, 0 respectively."""
    match = PATTERN.fullmatch(text.strip().lower())
    if match:
        amount, sides, modifier = match.groups()
        amount = int(amount or 1)
        sides = int(sides or 20)
        modifier = int(modifier or 0)
    else:
        raise ValueError("Invalid roll command format")
    return amount, sides, modifier


if __name__ == "__main__":
    repl()
