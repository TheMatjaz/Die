DnD-style dice rolling command line utility
===========================================

Python 3.10 or higher required. Just type a list of dice
rolls in the Die shell, using the format "NdS" where N is the
amount of dice to roll (1 if unspecified) and S is the 
amount of sides (6 if unspecified).

```bash
$ python3 die.py
Die> 4 d2 4d20 1d
1D4 | 2
1D2 | 1
4D20 | Orig: 12, 5, 4, 12
4D20 | Sort: 4, 5, 12, 12
4D20 | Sum: 33
1D6 | 4
Die> exit
$ 
```

