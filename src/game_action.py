from enum import Enum


class GameAction(Enum):
    MoveLeft = 1
    MoveRight = 2
    Rotate = 3
    HardDrop = 4
    Pause = 5
    Quit = 6
    NoAction = 7
