import kociemba
from rubik.cube import Cube
from rubik.solve import Solver

import random

from transform import kc_to_display_cube, display_cube_to_kc, kc_moves, pos_to_color, color_to_pos

MOVES = ["U", "L", "F", "R", "B", "D"]

def scramble(cube: Cube, k: int):
    """Scramble a cube with k random moves"""
    shuffle_moves = random.choices(MOVES, k=k)
    cube.sequence(" ".join(shuffle_moves))
    return cube

def main():

    solved = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"

    init_cube = scramble(
        Cube("".join(list(map(pos_to_color.get, [x for x in kc_to_display_cube(solved)])))),
        k=100,
    )
    goal_cube = Cube(
        "".join(
            list(map(pos_to_color.get, [x for x in kc_to_display_cube(solved)]))
        )
    )

    initial = display_cube_to_kc(''.join(str(init_cube).split()).replace("\n", ""))
    initial = "".join(
            list(map(color_to_pos.get, [x for x in initial]))
        )

    print("Scrambled Cube.")
    print(init_cube, "\n")

    moves = kociemba.solve(initial, solved)
    solver_moves = kc_moves(moves)

    print("Moves:\t", solver_moves, "\n")
    
    init_cube.sequence(solver_moves)

    print("Solved Cube.")
    print(init_cube)

if __name__ == "__main__":
    main()
