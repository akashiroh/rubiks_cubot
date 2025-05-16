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
    return {face: ROTATIONS[rot][orientation[face]] for face in orientation}

def constrained_moves(moves: str) -> str:
    """Convert moves: Rubik's Cube ==> Constrained Rubik's Cube"""
    moves = moves.split()
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

        current_position = orientation[face]

        needed_rotations = ROTATE_TO_BOTTOM[current_position]
        output_moves.extend(needed_rotations)

        for rot in needed_rotations:
            orientation = apply_rotation(orientation, rot)

        output_moves.append('Di' if prime else 'D')

    return ' '.join(output_moves)
