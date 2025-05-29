import cv2 as cv
import numpy as np
import numpy.typing as npt
from transform import color_to_pos
from move_set_conversions import robot_moves

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

    window_size = 5

    x_start = max(x - window_size, 0)
    x_end = min(x + window_size + 1, image.shape[0])
    y_start = max(y - window_size, 0)
    y_end = min(y + window_size + 1, image.shape[1])

    region = image[x_start:x_end, y_start:y_end]
    hsv_region = cv.cvtColor(region, cv.COLOR_BGR2HSV)

    h_mean = int(np.mean(hsv_region[:, :, 0]))
    s_mean = int(np.mean(hsv_region[:, :, 1]))
    v_mean = int(np.mean(hsv_region[:, :, 2]))
    
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
        return '?'
    
    color = classify_color(h_mean, s_mean, v_mean)
    return color


def open_webcam(
    face: str,
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
    image: npt.NDArray[np.uint8] = None,
    kc: bool=True,
) -> str:
    """
    for each cell on the cube face, scan the color

    Args:
        image (ndarray): single frame from webcam
        face (str): str in the set {U, D, F, B, L, R} to determine the order of the cells
    """
    if image is None:
        image = open_webcam(face)

    face_string = ""
    cell_order = face_order[face]
    for cell in cell_order:
        color = determine_pixel_color(image, cell)
        face_string += color
    
    # if kc:
    #     face_string = "".join([color_to_pos[x] for x in face_string])
    return face_string


def get_scanner_moves() -> str:
    return robot_moves("SU Y X SR Yi X SF Y X SD Yi X SL Y X SB Yi X")


def debug_webcam(
) -> npt.NDArray[np.uint8]:
    """
    opens webcam and scans one face

    Args: 
        face (str): str in the set {U, D, F, B, L, R} to determine the order of the cells
        debug (bool): keeps webcam open and draws points where it is scanning the color
    Returns: frame (ndarray): single frame
    """

    webcam = cv.VideoCapture(0)

    while True:
        ret, frame = webcam.read()

        face_string = scan_face("U", frame)

        for i in range(1, 10):
            point = cell_to_pixel[i]
            face_image = cv.circle(frame, point, radius=5, color=(0, 255, 0), thickness=-1)

        frame = cv.putText(
            frame, 
            face_string,
            (50,50), 
            cv.FONT_HERSHEY_SIMPLEX,
            1, 
            (0, 255, 0), 
            2, 
            cv.LINE_AA,
        )

        cv.imshow("Webcam", frame)

        if cv.waitKey(1) == ord("q"):
            break

    webcam.release()
    cv.destroyAllWindows()

    return frame


if __name__ == "__main__":
    debug_webcam()
