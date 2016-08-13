# Noughts and Crosses

A simple framework for a noughts and crosses (tic-tac-toe) game.

### How to play:

```python
from noughts_and_crosses import X0

game = X0()

game.place("X", [0,0])

game.place("0", [1,1])

```

Pieces are placed at x,y co-ordinates

```
+-----+-----+-----+
| 0,0 | 0,1 | 0,2 |
+-----+-----+-----+
| 1,0 | 1,1 | 1,2 |
+-----+-----+-----+
| 2,0 | 2,1 | 2,2 |
+-----+-----+-----+
```

## Task

To develop a computational opponent that can place an item in the optimal position on the board.

This can be achieved through a simple search tree - though more creative solutions are encouraged!

Feel free to add to, and modify the `X0` class. It's only a simple framework to get you started.
