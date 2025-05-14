import kociemba
from rubik.cube import Cube

from transform import kc_to_display_cube, display_cube_to_kc, kc_moves, pos_to_color, color_to_pos

import random
import sys

SOLVED_STRING = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"

MOVES = ["U", "L", "F", "R", "B", "D"] # rubiks move space
GOAL_MOVES = ["X", "Y", "D", "Di"] # constrained robot rubiks move space

def scramble(cube: Cube, k: int):
    """Scramble a cube with k random moves."""
    shuffle_moves = random.choices(MOVES, k=k)
    cube.sequence(" ".join(shuffle_moves))
    return cube


def initialize():
    """initialize a cube with some scramble."""

    scramble_moves = random.randint(1, 100)
    # cube to solve
    init_cube = scramble(
        Cube("".join(list(map(pos_to_color.get, [x for x in kc_to_display_cube(SOLVED_STRING)])))),
        k=scramble_moves,
    )

    # initial cube string
    initial = display_cube_to_kc(''.join(str(init_cube).split()).replace("\n", ""))
    initial = "".join(
        list(map(color_to_pos.get, [x for x in initial]))
    )

    return init_cube, initial, scramble_moves


def main():
    assert len(sys.argv) == 2, f"Please enter the number of time you want to solve as a cli."

    for _ in range(int(sys.argv[1])):
        cube, cube_string, scramble_moves = initialize()

        # print(f"Scrambled Cube.\n{cube}\n")

        moves = kociemba.solve(cube_string, SOLVED_STRING)
        solver_moves = kc_moves(moves)

        # print("Moves:\t", solver_moves, "\n")
        
        cube.sequence(solver_moves)
        
        if cube.is_solved():
            num_moves = len(solver_moves.split())
            print(f"Success! In {num_moves} moves. {100 * num_moves / scramble_moves:.2f}")
            # print(f"Solved Cube.\n{cube}\n")
        else:
            print("Uh Oh!")

if __name__ == "__main__":
    main()
