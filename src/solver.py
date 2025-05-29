import kociemba
from rubik.cube import Cube

from color_scanner import get_scanner_moves, scan_face
from cube_utils import initialize, SOLVED_STRING
from transform import cube_to_kc
from move_set_conversions import (
    solver_moves,
    constrained_moves,
    robot_moves,
)

# TODO: We need to scan  before getting the solving moves
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

def solve() -> None:

    scanner_moves = get_scanner_moves()
    
    cube_string = ""
    for move in scanner_moves:
        if move.startswith("S"):
            cube_string += scan_face(move[-1])
        else:
            # TODO: move robot
            ...

    kc_moves = kociemba.solve(cube_string, SOLVED_STRING)
    constrained_solver_moves = constrained_moves(rubiks_moves)
    robot_solver_moves = robot_moves(constrained_solver_moves)

    for move in robot_solver_moves:
            # TODO: move robot
            ...

if __name__ == "__main__":
    solve()
