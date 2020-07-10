# A Star Tile Solver

This is a small program that utilizes an [A* search algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm) to solve an 8 tile puzzle game.

Run test_code.py to see an example output.

```console
foo@bar:~$ python3 test_code.py
Actions:

  1 4 2    1 4 2
  6 3 7 -> 6 3 7
  8 5      8   5

  1 4 2    1 4 2
  6 3 7 -> 6 3 7
  8   5      8 5

  1 4 2    1 4 2
  6 3 7 ->   3 7
    8 5    6 8 5

  1 4 2    1 4 2
    3 7 -> 3   7
  6 8 5    6 8 5

  1 4 2    1 4 2
  3   7 -> 3 7  
  6 8 5    6 8 5

  1 4 2    1 4 2
  3 7   -> 3 7 5
  6 8 5    6 8  

  1 4 2    1 4 2
  3 7 5 -> 3 7 5
  6 8      6   8

  1 4 2    1 4 2
  3 7 5 -> 3   5
  6   8    6 7 8

  1 4 2    1   2
  3   5 -> 3 4 5
  6 7 8    6 7 8

  1   2      1 2
  3 4 5 -> 3 4 5
  6 7 8    6 7 8

Total cost: 10 moves.
```
