import kociemba
from rubik.cube import Cube

from color_scanner import get_scanner_moves
from cube_utils import initialize, SOLVED_STRING
from transform import cube_to_kc
from move_set_conversions import (
    solver_moves,
    constrained_moves,
    robot_moves,
)


def get_robot_moves(
    debug: bool=True,
) -> str or None:
    """
    returns a list of moves needed to solve the cube
    """
    
    cube = initialize()
    kc_moves = kociemba.solve(cube_to_kc(cube), SOLVED_STRING)

    rubiks_moves = solver_moves(kc_moves)
    constrained_solver_moves = constrained_moves(rubiks_moves)
    robot_solver_moves = robot_moves(constrained_solver_moves)

    cube.sequence(constrained_solver_moves)
    
    return get_scanner_moves() + " " + constrained_solver_moves if cube.is_solved() else None
