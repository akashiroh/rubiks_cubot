import kociemba
from rubik.cube import Cube
import random

from transform import (
    kc_to_display_cube,
    cube_to_kc,
    pos_to_color,
    color_to_pos,
)

SOLVED_STRING = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
MOVES = ["U", "L", "F", "R", "B", "D"]

def scramble(
    cube: Cube, 
    k: int,
) -> Cube:
    """Scramble a cube with k random moves."""
    shuffle_moves = random.choices(MOVES, k=k)
    cube.sequence(" ".join(shuffle_moves))
    return cube

def initialize() -> Cube:
    """initialize a cube with some scramble."""

    scramble_moves = random.randint(1, 30)

    cube = scramble(
        Cube("".join(list(map(pos_to_color.get, [x for x in kc_to_display_cube(SOLVED_STRING)])))),
        k=scramble_moves,
    )

    return cube
