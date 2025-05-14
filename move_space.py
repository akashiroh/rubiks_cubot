
class RubiksMoveSpace():
    """Class defines the moves in Rubik's Cube space"""

    def __init__(self):
        self.moves = [
            "U", # Up
            "L", # Left
            "F", # Front
            "R", # Right
            "B", # Back
            "D", # Down
            "Ui", # Up Inverted
            "Li", # Left Inverted
            "Fi", # Front Inverted
            "Ri", # Right Inverted
            "Bi", # Back Inverted
            "Di", # Down Inverted
        ]

class ConstrainedRubiksMoveSpace():
    """Class defines the moves in robot-constrained Rubik's Cube space"""

    def __init__(self):
        self.moves = [
            "D", # Down
            "Di", # Down Inverted
            "X", # Flip Cube R
            "Y", # Flip Cube U
        ]
