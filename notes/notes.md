# Notes for Rubik's Cubot

## Solving Algorithm (python)
**kociemba solving algorithm**
- Resources: [kociemba algorithm](https://kociemba.org/), [kociemba package](https://github.com/muodov/kociemba)
- Cube String: Face by face ==> UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB
- Example: U R F D L B
**Display/Testing**
- Resources[rubik-cube](https://pypi.org/project/rubik-cube/)
- Displays cube
- Moves cube (D, U, L, R, B, ..., etc.)
- Cube String: Layer by layer ==> OOOOOOOOOYYYWWWGGGBBBYYYWWWGGGBBBYYYWWWGGGBBBRRRRRRRRR
- Example: U L1 F1 R1 B1 L2 F2 R2 B2 L3 F3 R3 B3 D

**Move Spaces**
- Rubik's Cube: This space represents the moves that a human would follow to solve a cube, all permutations of the cube are legal in this space
- Constrained Rubik's Cube: This space represents the moves that our robot (Rubik's Cubot) will follow to solve a cube, this cube can only rotate (Y), flip (X), and permute the bottom layer (D)
- Robot: This space represents the actions the robot (Rubik's Cubot) will have to follow to make the Constrained Rubik's Cube space moves work. (e.g. rotate tray, extend fork, flip, retract fork, etc.)

**Move Set**
- Rubik's Cube: U L F R B D U Li Fi Ri Bi Di
- Constrained Rubik's Cube: D Di X Y (idk if we will support inverted moves here or not)
- Robot: Rotate tray, Extend fork, Retract fork, Rotate fork, Lower hat, Raise hat (assumes only rotate one direction for fork and tray)

**Transformation**
- Rubik's Cube ==> Constrained Rubik's Cube: 
    - I think we can map each move in Rubik's Cube space to a "face rotation".
    - These "face rotations" can be turned into flip the cube so face is down followed by a permutation of that bottom layer.
    - We will need to keep track of the cube state in terms of what color faces are where and be able to take the optimal path to getting a new face on the bottom.
- Constrained Rubik's Cube ==> Robot:
    - This should be a simpler transformation to conceptualize.
    - All moves in Constrained Rubik's Cube space should have a direct mapping to Robot space.

## Random Notes
**Kociemba Solving Algorithm**
- Doesn't seem to do fantastic with already solved cubes that we just want to rotate
- Doesn't include (X, Y, Z) or (M, E, S)
- Solution: keep `rubik-cube` for functionality `cube.is_solved()`
