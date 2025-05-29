import cv2 as cv
import numpy as np
import numpy.typing as npt
from transform import color_to_pos
import time

from typing import List


# TODO: Needs to update based on orientation of the webcam compared to the cube in the robot housing
face_order = {
    "U": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "R": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "F": [3, 6, 9, 2, 5, 8, 1, 4, 7],
    "D": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "L": [9, 8, 7, 6, 5, 4, 3, 2, 1],
    "B": [3, 6, 9, 2, 5, 8, 1, 4, 7],
}

# TODO: Needs to update based on position of the webcam on the robot housing
cell_to_pixel = {
    1: (190, 140),
    2: (320, 140),
    3: (460, 140),
    4: (190, 260),
    5: (320, 260),
    6: (460, 260),
    7: (190, 380),
    8: (320, 380),
    9: (460, 380),
}

def determine_pixel_color(
    image: npt.NDArray[np.uint8], 
    cell: int
) -> str:
    """
    returns the pixel color for a cell on the cube face

    Args:
        image (ndarray): single frame from webcam
        cell (int): [1..9] determines which cell (x, y) to scan
    """

    x, y = cell_to_pixel[cell]
    b, g, r = image[x, y]
    h, s, v = cv.cvtColor(np.uint8([[[b, g, r]]]), cv.COLOR_BGR2HSV)[0][0]

    def classify_color(h, s, v):
        """helper function to determine color based on HSV"""
        if v > 200 and s < 30:
            return 'W'
        if h < 10 or h > 160:
            return 'R'
        if 10 < h < 25:
            return 'O'
        if 25 <= h < 35:
            return 'Y'
        if 35 <= h < 85:
            return 'G'
        if 85 <= h < 130:
            return 'B'
        return 'unknown'
    
    color = classify_color(h, s, v)
    return color


def open_webcam(
    face: str,
    debug: bool=True,
) -> npt.NDArray[np.uint8]:
    """
    opens webcam and scans one face

    Args: 
        face (str): str in the set {U, D, F, B, L, R} to determine the order of the cells
        debug (bool): keeps webcam open and draws points where it is scanning the color
    Returns: frame (ndarray): single frame
    """

    webcam = cv.VideoCapture(0)
    ret, frame = webcam.read()

    webcam.release()
    cv.destroyAllWindows()

    return frame


def scan_face(
    face: str,
    debug: bool=True,
) -> str:
    """
    for each cell on the cube face, scan the color

    Args:
        image (ndarray): single frame from webcam
        face (str): str in the set {U, D, F, B, L, R} to determine the order of the cells
    """
    image = open_webcam(face, debug)

    face_string = ""
    cell_order = face_order[face]
    for cell in cell_order:
        color = determine_pixel_color(image, cell)
        face_string += color

    return face_string


def get_scanner_moves() -> str:
    return "SU Y X SR Yi X SF Y X SD Yi X SL Y X SB Yi X"



if __name__ == "__main__":

    cube_string = ""
    for face in ["U", "R", "F", "D", "L", "B"]:
        face_string = scan_face(face)
        cube_string += face_string

        print(face_string)
        time.sleep(10) # TODO: base this on a state machine
        """
        States:
            - SCANNING_COLOR
            - EXTENDING_FORK
            - RETRACTING FORK
            ...
            - ROTATING_TRAY_CW
        """
    print(cube_string)
