import kociemba
from rubik.cube import Cube

from color_scanner import get_scanner_moves, scan_face
from cube_utils import initialize, SOLVED_STRING
from transform import cube_to_kc
from visualizations.animations import animate_cube_sequence
from move_set_conversions import (
    solver_moves,
    constrained_moves,
    robot_moves,
)


def solve(
    scan: bool=False,
    save_to: str=None,
) -> None:
    
    if scan:
        scanner_moves = get_scanner_moves()
        
        cube_string = ""
        for move in scanner_moves:
            if move.startswith("S"):
                cube_string += scan_face(move[-1])
            else:
                # TODO: move robot
                ...
    else:
        cube = initialize()
        cube_string = cube_to_kc(cube)

    kc_moves = kociemba.solve(cube_string, SOLVED_STRING)
    rubiks_moves = solver_moves(kc_moves)
    constrained_solver_moves = constrained_moves(rubiks_moves)
    robot_solver_moves = robot_moves(constrained_solver_moves)

    cube_strings = []

    cube_strings.append(cube_string)
    for move in constrained_solver_moves.split():
        # TODO: move robot
        cube.sequence(move)
        cube_strings.append(cube_to_kc(cube))

    if save_to is not None:
        animate_cube_sequence(cube_strings, moves=constrained_solver_moves.split(), save_to=save_to)


if __name__ == "__main__":
    solve(scan=False, save_to="animation.gif")
