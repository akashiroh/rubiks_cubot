import kociemba
from rubik.cube import Cube
import random

from transform import (
    kc_to_display_cube,
    cube_to_kc,
    pos_to_color,
    color_to_pos,
)

from typing import List

SOLVED_STRING = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
MOVES = ["U", "L", "F", "R", "B", "D"]

def scramble(
    k: int,
) -> List[str]:
    """Scramble a cube with k random moves."""
    shuffle_moves = random.choices(MOVES, k=k)
    cube = Cube(kc_to_display_cube(SOLVED_STRING))
    cube.sequence(" ".join(shuffle_moves))

    cube_string = cube_to_kc(cube)

    return " ".join(shuffle_moves), cube_string
