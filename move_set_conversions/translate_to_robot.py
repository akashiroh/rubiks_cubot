from typing import List

# TODO: define global and motor coordinate systems

ROBOT_MOVES = {
    "X": ["rotate_tray_cw_90"],
    "Xi": ["rotate_tray_ccw_90"],
    "Y": ["extend_fork", "rotate_fork_cw_90", "retract_fork"],
    "Yi": ["extend_fork", "rotate_fork_ccw_90", "retract_fork"],
    "D": ["lower_hand", "rotate_fork_??_90", "raise_hand"],
    "Di": ["lower_hand", "rotate_fork_??_90", "raise_hand"],
}

def robot_moves(moves: str) -> List[str]:
    """Convert moves: Constrained Rubik's Cube ==> Robot"""
    moves = moves.split()
    output_moves = []

    for move in moves:
        output_moves.extend(ROBOT_MOVES[move])

    return output_moves
