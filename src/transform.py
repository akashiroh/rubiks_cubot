import kociemba
from rubik.cube import Cube

import re

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

def cube_to_kc(cube: Cube):
    display_str = ''.join(re.findall(r'[A-Z]', str(cube)))
    return display_cube_to_kc(display_str)
