import sys
import os

sys.path.append(os.path.abspath("./cube"))
sys.path.append(os.path.abspath("./kociemba"))

import kociemba
from rubik.cube import Cube

from cube_utils import scramble, SOLVED_STRING
from move_set_conversions import (
    solver_moves,
    constrained_moves,
    robot_moves,
)

def solve() -> None:
    """scramble and then solve the rubik's cube"""

    scramble_moves, cube_string = scramble(30)
    constrained_scramble_moves = constrained_moves(scramble_moves)
    robot_scramble_moves = robot_moves(constrained_scramble_moves)

    unconstrained_solver_moves = solver_moves(kociemba.solve(cube_string, SOLVED_STRING))
    constrained_solver_moves = constrained_moves(unconstrained_solver_moves)
    robot_solver_moves = robot_moves(constrained_solver_moves)

    full_move_set = " ".join(robot_scramble_moves + robot_solver_moves)
    with open("robot_moves.txt", "w") as file:
        for move in full_move_set.split():
            file.write(move + "\n")
    file.close()


if __name__ == "__main__":
    solve()
