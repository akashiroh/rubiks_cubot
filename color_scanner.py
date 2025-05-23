import cv2 as cv
import numpy as np
from transform import color_to_pos

face_order = {
    "U": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "R": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "F": [3, 6, 9, 2, 5, 8, 1, 4, 7],
    "D": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "L": [9, 8, 7, 6, 5, 4, 3, 2, 1],
    "B": [3, 6, 9, 2, 5, 8, 1, 4, 7],
}

cell_to_pixel = {
    1: (180, 180),
    2: (541, 180),
    3: (902, 180),
    4: (180, 541),
    5: (541, 541),
    6: (902, 541),
    7: (180, 902),
    8: (541, 902),
    9: (902, 902),
}

def determine_pixel_color(image, cell: int):
    x, y = cell_to_pixel[cell]
    b, g, r = image[x, y]
    h, s, v = cv.cvtColor(np.uint8([[[b, g, r]]]), cv.COLOR_BGR2HSV)[0][0]

    def classify_color(h, s, v):
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

def scan_face(image, face: str):
    face_string = ""
    cell_order = face_order[face]
    for cell in cell_order:
        color = determine_pixel_color(image, cell)
        face_string += color
    return face_string

if __name__ == "__main__":
    cube_string = ""
    for face in ["U", "R", "F", "D", "L", "B"]:
        face_image = cv.imread("rubiks_cube.jpg")

        # for i in range(1, 10):
        #     point = cell_to_pixel[i]
        #     face_image = cv.circle(face_image, point, radius=5, color=(0, 255, 0), thickness=-1)
        # cv.imshow("display", face_image)
        # cv.waitKey(0)
        # cv.destroyAllWindows()

        face_string = scan_face(face_image, face)
        cube_string += face_string
        print(face_string)
    cube_string = "".join([color_to_pos[c] for c in cube_string])
    print(cube_string)
