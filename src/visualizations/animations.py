import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter
from typing import List

import matplotlib
matplotlib.use('Agg')

import kociemba
from rubik.cube import Cube

from cube_utils import initialize
from move_set_conversions import (
    solver_moves,
    constrained_moves,
)
from transform import (
    kc_to_display_cube,
    display_cube_to_kc,
    cube_to_kc,
    pos_to_color,
    color_to_pos,
)

import sys

SOLVED_STRING = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"

# === Cube setup ===
letter_to_color = {
    'U': 'white', 'D': 'yellow', 'F': 'blue',
    'B': 'green', 'L': 'red', 'R': 'orange'
}

face_order = ['U', 'R', 'F', 'D', 'L', 'B']

face_positions = {
    'U': (lambda i: (i % 3, 2, i // 3), (0, 1, 0)),
    'D': (lambda i: (i % 3, 0, 2 - i // 3), (0, -1, 0)),
    'F': (lambda i: (i % 3, 2 - i // 3, 2), (0, 0, 1)),
    'B': (lambda i: (2 - i % 3, 2 - i // 3, 0), (0, 0, -1)),
    'L': (lambda i: (0, 2 - i // 3, i % 3), (-1, 0, 0)),
    'R': (lambda i: (2, 2 - i // 3, 2 - i % 3), (1, 0, 0)),
}

# === Move definitions ===
MOVE_DEFINITIONS = {}

# R / Ri
MOVE_DEFINITIONS['Ri'] = {
    'axis': (1, 0, 0),
    'center': (2, 1, 1),
    'facelets': [
        ('R', list(range(9))),
        ('U', [2, 5, 8]),
        ('F', [2, 5, 8]),
        ('D', [2, 5, 8]),
        ('B', [6, 3, 0]),
    ]
}
MOVE_DEFINITIONS['R'] = {
    **MOVE_DEFINITIONS['Ri'], 'reverse': True
}

# L / Li
MOVE_DEFINITIONS['Li'] = {
    'axis': (-1, 0, 0),
    'center': (0, 1, 1),
    'facelets': [
        ('L', list(range(9))),
        ('U', [0, 3, 6]),
        ('B', [8, 5, 2]),
        ('D', [0, 3, 6]),
        ('F', [0, 3, 6])
    ]
}
MOVE_DEFINITIONS['L'] = {
    **MOVE_DEFINITIONS['Li'], 'reverse': True
}

# U / Ui
MOVE_DEFINITIONS['Ui'] = {
    'axis': (0, 1, 0),
    'center': (1, 2, 1),
    'facelets': [
        ('U', list(range(9))),
        ('B', [2, 1, 0]),
        ('R', [2, 1, 0]),
        ('F', [2, 1, 0]),
        ('L', [2, 1, 0])
    ]
}
MOVE_DEFINITIONS['U'] = {
    **MOVE_DEFINITIONS['Ui'], 'reverse': True
}

# D / Di
MOVE_DEFINITIONS['Di'] = {
    'axis': (0, -1, 0),
    'center': (1, 0, 1),
    'facelets': [
        ('D', list(range(9))),
        ('F', [6, 7, 8]),
        ('R', [6, 7, 8]),
        ('B', [6, 7, 8]),
        ('L', [6, 7, 8])
    ]
}
MOVE_DEFINITIONS['D'] = {
    **MOVE_DEFINITIONS['Di'], 'reverse': True
}

# F / Fi
MOVE_DEFINITIONS['Fi'] = {
    'axis': (0, 0, 1),
    'center': (1, 1, 2),
    'facelets': [
        ('F', list(range(9))),
        ('U', [6, 7, 8]),
        ('R', [0, 3, 6]),
        ('D', [2, 1, 0]),
        ('L', [8, 5, 2])
    ]
}
MOVE_DEFINITIONS['F'] = {
    **MOVE_DEFINITIONS['Fi'], 'reverse': True
}

# B / Bi
MOVE_DEFINITIONS['Bi'] = {
    'axis': (0, 0, -1),
    'center': (1, 1, 0),
    'facelets': [
        ('B', list(range(9))),
        ('U', [0, 1, 2]),
        ('L', [0, 3, 6]),
        ('D', [8, 7, 6]),
        ('R', [8, 5, 2])
    ]
}
MOVE_DEFINITIONS['B'] = {
    **MOVE_DEFINITIONS['Bi'], 'reverse': True
}

# Define X rotation: rotate entire cube around X axis clockwise
MOVE_DEFINITIONS['Xi'] = {
    'axis': (1, 0, 0),
    'center': (1, 1, 1),  # center of the cube
    'facelets': [  # all facelets rotate
        ('U', list(range(9))),
        ('D', list(range(9))),
        ('F', list(range(9))),
        ('B', list(range(9))),
        ('L', list(range(9))),
        ('R', list(range(9))),
    ]
}

# Xi: inverse X (counter-clockwise)
MOVE_DEFINITIONS['X'] = {**MOVE_DEFINITIONS['Xi'], 'reverse': True}

# Define Y rotation: rotate entire cube around Y axis clockwise
MOVE_DEFINITIONS['Yi'] = {
    'axis': (0, 1, 0),
    'center': (1, 1, 1),
    'facelets': [
        ('U', list(range(9))),
        ('D', list(range(9))),
        ('F', list(range(9))),
        ('B', list(range(9))),
        ('L', list(range(9))),
        ('R', list(range(9))),
    ]
}

# Yi: inverse Y (counter-clockwise)
MOVE_DEFINITIONS['Y'] = {**MOVE_DEFINITIONS['Yi'], 'reverse': True}



# === Utility functions ===
def get_face_vertices(center, normal):
    x, y, z = center
    d = 0.48
    if normal[0] != 0:
        return [[x + 0.5 * normal[0], y - d, z - d],
                [x + 0.5 * normal[0], y + d, z - d],
                [x + 0.5 * normal[0], y + d, z + d],
                [x + 0.5 * normal[0], y - d, z + d]]
    elif normal[1] != 0:
        return [[x - d, y + 0.5 * normal[1], z - d],
                [x + d, y + 0.5 * normal[1], z - d],
                [x + d, y + 0.5 * normal[1], z + d],
                [x - d, y + 0.5 * normal[1], z + d]]
    elif normal[2] != 0:
        return [[x - d, y - d, z + 0.5 * normal[2]],
                [x + d, y - d, z + 0.5 * normal[2]],
                [x + d, y + d, z + 0.5 * normal[2]],
                [x - d, y + d, z + 0.5 * normal[2]]]

def rotate_vertices(vertices, axis, angle_deg, center):
    angle_rad = np.radians(angle_deg)
    axis = np.array(axis)
    axis = axis / np.linalg.norm(axis)
    cos_a = np.cos(angle_rad)
    sin_a = np.sin(angle_rad)
    ux, uy, uz = axis
    R = np.array([
        [cos_a + ux**2 * (1 - cos_a), ux*uy*(1 - cos_a) - uz*sin_a, ux*uz*(1 - cos_a) + uy*sin_a],
        [uy*ux*(1 - cos_a) + uz*sin_a, cos_a + uy**2 * (1 - cos_a), uy*uz*(1 - cos_a) - ux*sin_a],
        [uz*ux*(1 - cos_a) - uy*sin_a, uz*uy*(1 - cos_a) + ux*sin_a, cos_a + uz**2 * (1 - cos_a)]
    ])
    return [((R @ (np.array(v) - center)) + center).tolist() for v in vertices]

# === Animation function ===
def animate_cube_sequence(cube_strings: List[str], moves: List[str], save_to: str):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')

    frames_per_move = 8
    total_frames = frames_per_move * (len(moves))

    def build_facelet_map(cube_str):
        facelet_map = []
        idx = 0
        for face in face_order:
            func, normal = face_positions[face]
            for i in range(9):
                pos = func(i)
                color = letter_to_color.get(cube_str[idx], 'gray')
                facelet_map.append(((face, i), pos, normal, color))
                idx += 1
        return facelet_map

    def get_rotating_facelets(move):
        base_move = move[0]
        move_def = MOVE_DEFINITIONS[base_move]
        rotating = set()
        for f, ids in move_def['facelets']:
            for i in ids:
                rotating.add((f, i))
        return rotating

    def draw_frame(frame):
        ax.cla()
        ax.set_xlim(-0.5, 3.5)
        ax.set_ylim(-0.5, 3.5)
        ax.set_zlim(-0.5, 3.5)
        ax.set_box_aspect([1, 1, 1])
        # TO CHANGE THE VIEWPOINT OF THE CUBE IN THE ANIMATION
        ax.view_init(roll=0, azim=45, elev=30, vertical_axis='y')
        ax.axis('off')

        move_idx = frame // frames_per_move
        frame_in_move = frame % frames_per_move

        if move_idx >= len(moves):
            # draw last cube state static
            facelet_map = build_facelet_map(cube_strings[-1])
            for (face, i), pos, normal, color in facelet_map:
                verts = get_face_vertices(pos, normal)
                poly = Poly3DCollection([verts], facecolors=color, edgecolor='black')
                ax.add_collection3d(poly)
            return

        move = moves[move_idx]
        start_cube = cube_strings[move_idx]
        end_cube = cube_strings[move_idx + 1]

        rotating_facelets = get_rotating_facelets(move)
        base_move = move[0]
        move_def = MOVE_DEFINITIONS[base_move]
        axis, center = move_def['axis'], move_def['center']
        reverse = move_def.get('reverse', False)
        if move.endswith('i'):
            reverse = not reverse

        # Interpolate rotation angle from 0 to 90 degrees
        angle_deg = 90 * (frame_in_move / frames_per_move)
        if reverse:
            angle_deg = -angle_deg

        # Build facelet map from start_cube string
        facelet_map = build_facelet_map(start_cube)

        for (face, i), pos, normal, color in facelet_map:
            verts = get_face_vertices(pos, normal)
            if (face, i) in rotating_facelets:
                verts = rotate_vertices(verts, axis, angle_deg, center)
            poly = Poly3DCollection([verts], facecolors=color, edgecolor='black')
            ax.add_collection3d(poly)

    ani = FuncAnimation(fig, draw_frame, frames=total_frames + frames_per_move, interval=5, repeat=False)
    ani.save(save_to, writer=PillowWriter(fps=30))

# === Test in __main__ ===
if __name__ == '__main__':
    cube_strings = []

    cube = initialize()
    cube_string = cube_to_kc(cube)
    kc_moves = kociemba.solve(cube_string, SOLVED_STRING)
    rubiks_moves = solver_moves(kc_moves)
    constrained_solver_moves = constrained_moves(rubiks_moves)
    cube_strings.append(cube_string)

    for i, move in enumerate(constrained_solver_moves.split()):
    # for i, move in enumerate(rubiks_moves.split()):
        cube.sequence(move)
        cube_strings.append(cube_string)
    # animate_cube_sequence(cube_strings, moves=rubiks_moves.split())
    animate_cube_sequence(cube_strings, moves=constrained_solver_moves.split())
