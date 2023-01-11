DnD-style dice rolling command line utility
===========================================

## Usage

Launch `die.py` and type your dice rolls in the `Die` shell.

The format is `NdS+M`, where:

- `N` is the amount of dice to roll (1 if unspecified)
- `S` are the sides of the die (d20 if unspecified)
- `M` is the modifier to be added to each roll (0 if unspecified)

For example:

- `1` rolls one 20-sided die
- `3d8` rolls three 8-sided dice
- `2d10-3` rolls two 10-sided dice and subtracts three from each result
- `2+3` rolls two 20-sided die and adds three to each result

Multiple entries are allowed in a single line, e.g. `1d8 3d20+2 6d10`.

## Example

```bash
$ python3 die.py
Die> 1 3d8 2d10-3 2+3
1d20+0	| 20
3d8+0	| [1, 4, 3] | Min=1 | Max=4 | Sum=8
2d10+3	| [9, 7] | Min=7 | Max=9 | Sum=16
2d20+3	| [9, 21] | Min=9 | Max=21 | Sum=30
Die> exit
$ 
```

## Requirements

Self-contained in `die.py`, requires Python 3.10 or higher, no dependencies.
