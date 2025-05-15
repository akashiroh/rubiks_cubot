import kociemba
from rubik.cube import Cube

"""
 U        W
LFRB ==> RBOG
 D        Y
"""
pos_to_color ={
    "U": "W",
    "L": "R",
    "F": "B",
    "R": "O",
    "B": "G",
    "D": "Y",
}
color_to_pos = {
    "W": "U",
    "R": "L",
    "B": "F",
    "O": "R",
    "G": "B",
    "Y": "D",
}


def kc_to_display_cube(kc_str: str):
    if len(kc_str) != 54:
        raise ValueError("KC string must be exactly 54 characters long.")

    # Split KC format into faces
    U = kc_str[0:9]
    R = kc_str[9:18]
    F = kc_str[18:27]
    D = kc_str[27:36]
    L = kc_str[36:45]
    B = kc_str[45:54]

    def row(face, i):  # i = 0, 1, 2
        return face[i*3:(i+1)*3]

    # Reconstruct display format
    display = (
        U +
        row(L, 0) + row(F, 0) + row(R, 0) + row(B, 0) +
        row(L, 1) + row(F, 1) + row(R, 1) + row(B, 1) +
        row(L, 2) + row(F, 2) + row(R, 2) + row(B, 2) +
        D
    )
    return display

def display_cube_to_kc(display_str: str):
    if len(display_str) != 54:
        raise ValueError("Display string must be exactly 54 characters long.")

    U = display_str[0:9]
    D = display_str[45:54]

    # The 36 characters in between are 3 rows of LFRB
    layers = display_str[9:45]

    # Extract rows
    L = layers[0:3] + layers[12:15] + layers[24:27]
    F = layers[3:6] + layers[15:18] + layers[27:30]
    R = layers[6:9] + layers[18:21] + layers[30:33]
    B = layers[9:12] + layers[21:24] + layers[33:36]

    # Combine into KC format: U R F D L B
    return U + R + F + D + L + B



def kc_moves(moves: str):
    """
    This function reorders the solver moves to be compatible with rubik-cube
    """
    moves = moves.split()
    
    collect = []
    for move in moves:
        if move[-1] == "'":
            collect.append(
                move[0] + "i"
            )
        elif move[-1] == "2":
            collect.append(move[0])
            collect.append(move[0])
        else:
            collect.append(move[0])

    return " ".join(collect)


# Update orientation based on cube rotation
ROTATIONS = {
    'X': {
        'U': 'B', 
        'D': 'F', 
        'F': 'U', 
        'B': 'D', 
        'L': 'L', 
        'R': 'R',
    },
    'Xi': {
        'U': 'F',
        'D': 'B',
        'F': 'D',
        'B': 'U',
        'L': 'L',
        'R': 'R',
    },
    'Y': {
        'F': 'L',
        'B': 'R',
        'L': 'B',
        'R': 'F',
        'U': 'U',
        'D': 'D',
    },
    'Yi': {
        'F': 'R',
        'B': 'L',
        'L': 'F',
        'R': 'B',
        'U': 'U',
        'D': 'D',
    }
}

# Moves to rotate a face to the bottom
ROTATE_TO_BOTTOM = {
    'U': ['X', 'X'],
    'D': [],
    'F': ['Xi'],
    'B': ['X'],
    'L': ['Y', 'X'],
    'R': ['Yi', 'X']
}

def apply_rotation(orientation, rot):
    """Apply a single cube rotation to current orientation."""
    new_orientation = {}
    for face in orientation:
        new_orientation[face] = ROTATIONS[rot].get(orientation[face], orientation[face])
    return new_orientation

def constrained_moves(moves: str):
    """Convert moves: Rubik's Cube ==> Constrained Rubik's Cube"""
    moves = moves.strip().split()
    orientation = {
        'U': 'U',
        'R': 'R',
        'F': 'F',
        'D': 'D',
        'L': 'L',
        'B': 'B'
    }
    output_moves = []

    for move in moves:
        face = move[0]
        prime = move.endswith('i')
        target_face = face

        current_position = orientation[target_face]

        needed_rotations = ROTATE_TO_BOTTOM[current_position]
        output_moves.extend(needed_rotations)

        for rot in needed_rotations:
            orientation = apply_rotation(orientation, rot)

        output_moves.append('Di' if prime else 'D')

    return ' '.join(output_moves)
