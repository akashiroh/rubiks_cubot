import kociemba
from rubik.cube import Cube

from move_set_conversions import (
    solver_moves,
    constrained_moves,
    robot_moves,
)

from transform import (
    kc_to_display_cube,
    display_cube_to_kc,
    pos_to_color,
    color_to_pos,
)

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

    scramble_moves = random.randint(1, 200)

    # scrambled cube
    init_cube = scramble(
        Cube("".join(list(map(pos_to_color.get, [x for x in kc_to_display_cube(SOLVED_STRING)])))),
        k=scramble_moves,
    )

    # srambled cube string
    initial = display_cube_to_kc(''.join(str(init_cube).split()).replace("\n", ""))
    initial = "".join(
        list(map(color_to_pos.get, [x for x in initial]))
    )

    return init_cube, initial, scramble_moves


def main():
    assert len(sys.argv) == 2, f"Please enter the number of time you want to solve: uv run main.py 1"
    
    scramble_moves, solve_moves = [], []
    for _ in range(int(sys.argv[1])):
        cube, cube_string, num_scramble_moves = initialize()

        print(f"Scrambled Cube.\n{cube}\n")

        kc_moves = kociemba.solve(cube_string, SOLVED_STRING) # initial ==> goal
        rubiks_moves = solver_moves(kc_moves) # R' => Ri | R2 => R R
        constrained_solver_moves = constrained_moves(rubiks_moves) # rubiks_space => constrained_rubiks_space
        robot_solver_moves = robot_moves(constrained_solver_moves) # constrained_rubiks_space => robot_space

        print(f"\nKC Moves: {len(kc_moves)} moves ->", kc_moves)
        print(f"Rubiks Moves: {len(rubiks_moves)} moves ->", rubiks_moves)
        print(f"Constrained Moves: {len(constrained_solver_moves)} moves ->", constrained_solver_moves)
        print(f"Robot Moves: {len(robot_solver_moves)} moves ->", robot_solver_moves, "\n")

        cube.sequence(constrained_solver_moves)
        
        if cube.is_solved():
            num_solve_moves = len(constrained_solver_moves.split())
            scramble_moves.append(num_scramble_moves)
            solve_moves.append(num_solve_moves)
            print(f"Success! In {num_solve_moves} moves | {100 * num_solve_moves / num_scramble_moves:.2f}% solve moves as scramble moves")
        else:
            print("Uh Oh!")
    print(f"Average scramble moves: {sum(scramble_moves) / len(scramble_moves):.0f} \t Average Constrained Solve Moves: {sum(solve_moves) / len(solve_moves):.0f}")

if __name__ == "__main__":
    main()
