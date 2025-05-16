# Move Set Conversions


**Kociemba => Rubik's** [✔]
Since `rubik-cube` can display and manipulate the code, I wanted to convert moves and cube strings to this package.
This entails updating notation slightly to (e.g, R' -> Ri, R2 -> R R)


**Rubik's => Constrained Rubik's** [✔]
From a move set that solves the cube, assuming the cube exists floating in space and all 6 faces can turn, we need to define a move set that only performs actions that the robot can take.
Since the robot will only be able to rotate the cube with the tray and the fork, it can only perform the X and Y moves (we are also assuming it can rotate both directions so we get Xi and Yi).
We can only manipulate the bottom face, so it can only perform the D and Di moves.
To convert to this space, we need to keep track of where each face is oriented on the cube after each move. 
We can then semantically call each move a face to update and define a set of moves needed to rotate each face to the bottom:
```
ROTATE_TO_BOTTOM = {
    'U': ['X', 'X'],
    'D': [],
    'F': ['Xi'],
    'B': ['X'],
    'L': ['Y', 'X'],
    'R': ['Yi', 'X']
}
```

After each rotation, we just need to update the orientation to reflect the move taken.

**Constrained Rubik's => Robot** [✔]
Now that we have a move set that the robot can actually perform we must convert from general rubik's cube notation into robot motor control instructions.
These controls will still be an abstraction for the actual commands that the motors will recieve.
For each move, what does the robot need to do? (e.g., lower the hand -> rotate the tray -> raise the hand)

**Robot => Motor Control** [ ]
These are the commands that the motors actually recieve.
e.g., rotate the tray this many degrees, rotate the rack and pinion gear this many degrees to extend the fork this many of millimeters
etc.
