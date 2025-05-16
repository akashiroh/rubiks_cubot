# Move Spaces

## Rubik's Cube Space

**Notation and Rotations**
- [Rubik's Cube Notation](https://www.speedcube.us/blogs/notation-guides/3x3-rubiks-cube-notation)
- Moves and Inversions (Primes)
    - e.g., U -> look at U face and turn clockwise | U' -> look at U face and turn counter clockwise
- Cube rotations
    - e.g., X -> flip cube along R | Y ->  flip cube along U | Z -> flip cube along F

**Kociemba** [✔]
- Resources: [kociemba algorithm](https://kociemba.org/), [kociemba package](https://github.com/muodov/kociemba)
- Kociemba Move Set: {U R F L B D U' R' F' L' B' D'}
- This move set is what the solver utilizes
- Cube String: Face by face ==> UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB

**Rubik's** [✔]
- Resources[rubik-cube](https://pypi.org/project/rubik-cube/)
- Rubiks Move Set: {U R F L B D Ui Ri Fi Li Bi Di X Y Z M E S}
- This move set is what the display package uses
- Cube String: Layer by layer ==> OOOOOOOOOYYYWWWGGGBBBYYYWWWGGGBBBYYYWWWGGGBBBRRRRRRRRR

**Constrained Rubik's** [✔]
- Constrained Rubiks Move Set: {D Di X Y Xi Yi}
- This move set follows a subset of the Rubik's move set that the robot will be able to handle
    - X rotations (tray)
    - Y rotations (fork)
    - D face rotations (tray + hand)

## Robot Space

**Todo**
[ ] Define coordinate system for robot (cw, ccw)

- Robot Move set: {extend/retract fork, rotate tray, lower/raise hand}
