from enum import Enum


class Color(Enum):
    BLACK = (0, 0, 0)  # Black for empty cells
    CYAN = (0, 255, 255)  # I piece
    BLUE = (0, 0, 255)  # J piece
    ORANGE = (255, 165, 0)  # L piece
    YELLOW = (255, 255, 0)  # O piece
    GREEN = (0, 255, 0)  # S piece
    PURPLE = (128, 0, 128)  # T piece
    RED = (255, 0, 0)  # Z piece
