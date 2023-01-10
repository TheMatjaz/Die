#!/usr/bin/env python3
# encoding: utf-8

# Copyright © 2023, Matjaž Guštin <dev@matjaz.it> <https://matjaz.it>
# Released under the BSD 3-Clause License

import secrets


def repl():
    while True:
        try:
            commands = input("Die> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            break
        if commands in ('exit', 'quit'):
            break
        for command in commands.split():
            try:
                amount, sides = parse(command)
                prompt = f"{amount:d}D{sides:d} | "
                rolls = roll_dice(amount, sides)
                if len(rolls) == 1:
                    print(f"{prompt}{rolls[0]}")
                else:
                    print(
                        f"{prompt}Orig: " + ", ".join(f"{r:d}" for r in rolls))
                    print(f"{prompt}Sort: " + ", ".join(
                        f"{r:d}" for r in sorted(rolls)))
                    print(f"{prompt}Sum: {sum(rolls)}")
            except ValueError as e:
                print(f"Bad command: {str(e)}")
                continue


def roll_dice(amount: int = 1, sides: int = 6) -> list[int]:
    if amount <= 0:
        raise ValueError("Can't roll no dice.")
    if sides <= 1:
        raise ValueError("Can't roll fewer than 2 sides.")
    return [secrets.randbelow(sides) + 1 for _ in range(amount)]


def parse(text: str) -> tuple[int, int]:
    fields = text.strip().lower().split('d')
    match len(fields):
        case 1:  # Just the sides, like "6"
            amount = ''
            sides = fields[0]
        case 2:  # "NdS", N=amount, S=sides. N could be empty string.
            amount = fields[0]
            sides = fields[1]
        case _:
            raise ValueError("Invalid roll text format")
    if len(amount) == 0:
        amount = 1
    else:
        amount = int(amount)
    if len(sides) == 0:
        sides = 6
    else:
        sides = int(sides)
    return amount, sides


if __name__ == "__main__":
    repl()
