# Rubiks Cubot

A Rubik's Cube Solving Robot.

**Contributors**
- Andrew Holmes
- Dylan Scott Carroll
- Tarnivir Virk
- Jonathon Ly

## Environment Set Up

- This branch is the barebones solver for the pico board
- Instead of pip installing, follow these instructions:

```
git@github.com:akashiroh/rubiks_cubot.git
cd rubiks_cubot

git clone git@github.com:pglass/cube.git
git clone git@github.com:muodov/kociemba.git

cd kociemba
python3 setup.py build_ext --inplace
```

## Running

- The following function will return a list of string commands for the robot
```
python3 src/solver.py
```

