import kociemba
from rubik.cube import Cube
import os
import imageio.v2 as imageio
import matplotlib.pyplot as plt
import imageio.v2 as imageio

import tempfile

from visualizations import plot_cube

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

from main import initialize


SOLVED_STRING = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"

def main():
    with tempfile.TemporaryDirectory() as temp_dir:
        frame_paths = []

        cube, cube_string, num_scramble_moves = initialize()

        kc_moves = kociemba.solve(cube_string, SOLVED_STRING)
        rubiks_moves = solver_moves(kc_moves)
        constrained_solver_moves = constrained_moves(rubiks_moves)

        for i, move in enumerate(constrained_solver_moves.split()):
        # for i, move in enumerate(rubiks_moves.split()):
            cube.sequence(move)
            cube_string = "".join(color_to_pos[cell] for cell in cube_to_kc(cube))
            fig = plot_cube(cube_string)
            fig.suptitle(move, fontsize=20)

            frame_path = os.path.join(temp_dir, f"frame_{i:03d}.png")
            plt.savefig(frame_path, bbox_inches="tight")
            plt.close(fig)
            frame_paths.append(frame_path)

        images = [imageio.imread(path) for path in frame_paths]
        imageio.mimsave("constrained_simulation.gif", images, fps=5)

        
if __name__ == "__main__":
    main()
