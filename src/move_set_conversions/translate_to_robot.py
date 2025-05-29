from typing import List

ROBOT_MOVES = {
    "X": ["extend_fork", "rotate_fork_cw_90", "retract_fork"],
    "Xi": ["extend_fork", "rotate_fork_ccw_90", "retract_fork"],
    "Y": ["rotate_tray_cw_90"],
    "Yi": ["rotate_tray_ccw_90"],
    "D": ["lower_hand", "rotate_tray_cw_90", "raise_hand"],
    "Di": ["lower_hand", "rotate_tray_ccw_90", "raise_hand"],
}

def robot_moves(moves: str) -> List[str]:
    """Convert moves: Constrained Rubik's Cube ==> Robot"""
    moves = moves.split()
    output_moves = []

    for move in moves:
        output_moves.extend(ROBOT_MOVES[move])

    return output_moves
