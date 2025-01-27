from abc import ABC, abstractmethod
from color import Color
from random import choice


class Tile(ABC):
    def __init__(self, root_x, root_y):
        self.root_x = root_x
        self.root_y = root_y
        self.rotation = 0

    @abstractmethod
    def rotate(self):
        """Rotate the tile 90 degrees clockwise"""
        pass

    @abstractmethod
    def get_blocks(self):
        """Return list of (x,y) coordinates of blocks relative to root position"""
        pass

    @abstractmethod
    def get_color(self):
        """Return the Color enum for this tile type"""
        pass


class ITile(Tile):
    """
    ...
    ###
    ...
    """

    def rotate(self):
        self.rotation = (self.rotation + 1) % 2

    def get_blocks(self):
        if self.rotation == 0:
            return [
                (self.root_x - 1, self.root_y),
                (self.root_x, self.root_y),
                (self.root_x + 1, self.root_y),
                (self.root_x + 2, self.root_y),
            ]
        else:
            return [
                (self.root_x, self.root_y - 1),
                (self.root_x, self.root_y),
                (self.root_x, self.root_y + 1),
                (self.root_x, self.root_y + 2),
            ]

    def get_color(self):
        return Color.CYAN


class JTile(Tile):
    """
    #..
    ###
    ...
    """

    def rotate(self):
        self.rotation = (self.rotation + 1) % 4

    def get_blocks(self):
        if self.rotation == 0:
            return [
                (self.root_x - 1, self.root_y - 1),
                (self.root_x - 1, self.root_y),
                (self.root_x, self.root_y),
                (self.root_x + 1, self.root_y),
            ]
        elif self.rotation == 1:
            return [
                (self.root_x, self.root_y - 1),
                (self.root_x, self.root_y),
                (self.root_x, self.root_y + 1),
                (self.root_x - 1, self.root_y + 1),
            ]
        elif self.rotation == 2:
            return [
                (self.root_x - 1, self.root_y),
                (self.root_x, self.root_y),
                (self.root_x + 1, self.root_y),
                (self.root_x + 1, self.root_y + 1),
            ]
        else:
            return [
                (self.root_x + 1, self.root_y - 1),
                (self.root_x, self.root_y - 1),
                (self.root_x, self.root_y),
                (self.root_x, self.root_y + 1),
            ]

    def get_color(self):
        return Color.BLUE


class LTile(Tile):
    """
    ..#
    ###
    ...
    """

    def rotate(self):
        self.rotation = (self.rotation + 1) % 4

    def get_blocks(self):
        if self.rotation == 0:
            return [
                (self.root_x + 1, self.root_y - 1),
                (self.root_x - 1, self.root_y),
                (self.root_x, self.root_y),
                (self.root_x + 1, self.root_y),
            ]
        elif self.rotation == 1:
            return [
                (self.root_x, self.root_y - 1),
                (self.root_x, self.root_y),
                (self.root_x, self.root_y + 1),
                (self.root_x + 1, self.root_y + 1),
            ]
        elif self.rotation == 2:
            return [
                (self.root_x - 1, self.root_y),
                (self.root_x, self.root_y),
                (self.root_x + 1, self.root_y),
                (self.root_x - 1, self.root_y + 1),
            ]
        else:
            return [
                (self.root_x - 1, self.root_y - 1),
                (self.root_x, self.root_y - 1),
                (self.root_x, self.root_y),
                (self.root_x, self.root_y + 1),
            ]

    def get_color(self):
        return Color.ORANGE


class OTile(Tile):
    """
    ##
    ##
    ..
    """

    def rotate(self):
        pass  # O tile doesn't rotate

    def get_blocks(self):
        return [
            (self.root_x, self.root_y),
            (self.root_x + 1, self.root_y),
            (self.root_x, self.root_y + 1),
            (self.root_x + 1, self.root_y + 1),
        ]

    def get_color(self):
        return Color.YELLOW


class STile(Tile):
    """
    .##
    ##.
    ...
    """

    def rotate(self):
        self.rotation = (self.rotation + 1) % 2

    def get_blocks(self):
        if self.rotation == 0:
            return [
                (self.root_x, self.root_y - 1),
                (self.root_x + 1, self.root_y - 1),
                (self.root_x - 1, self.root_y),
                (self.root_x, self.root_y),
            ]
        else:
            return [
                (self.root_x, self.root_y - 1),
                (self.root_x, self.root_y),
                (self.root_x + 1, self.root_y),
                (self.root_x + 1, self.root_y + 1),
            ]

    def get_color(self):
        return Color.GREEN


class TTile(Tile):
    """
    .#.
    ###
    ...
    """

    def rotate(self):
        self.rotation = (self.rotation + 1) % 4

    def get_blocks(self):
        if self.rotation == 0:
            return [
                (self.root_x, self.root_y - 1),
                (self.root_x - 1, self.root_y),
                (self.root_x, self.root_y),
                (self.root_x + 1, self.root_y),
            ]
        elif self.rotation == 1:
            return [
                (self.root_x, self.root_y - 1),
                (self.root_x, self.root_y),
                (self.root_x + 1, self.root_y),
                (self.root_x, self.root_y + 1),
            ]
        elif self.rotation == 2:
            return [
                (self.root_x - 1, self.root_y),
                (self.root_x, self.root_y),
                (self.root_x + 1, self.root_y),
                (self.root_x, self.root_y + 1),
            ]
        else:
            return [
                (self.root_x, self.root_y - 1),
                (self.root_x - 1, self.root_y),
                (self.root_x, self.root_y),
                (self.root_x, self.root_y + 1),
            ]

    def get_color(self):
        return Color.PURPLE


class ZTile(Tile):
    """
    ##.
    .##
    ...
    """

    def rotate(self):
        self.rotation = (self.rotation + 1) % 2

    def get_blocks(self):
        if self.rotation == 0:
            return [
                (self.root_x - 1, self.root_y - 1),
                (self.root_x, self.root_y - 1),
                (self.root_x, self.root_y),
                (self.root_x + 1, self.root_y),
            ]
        else:
            return [
                (self.root_x + 1, self.root_y - 1),
                (self.root_x, self.root_y),
                (self.root_x + 1, self.root_y),
                (self.root_x, self.root_y + 1),
            ]

    def get_color(self):
        return Color.RED


def get_random_tile(root_x, root_y):
    """Return a random tile type positioned at the given coordinates"""
    tile_types = [ITile, JTile, LTile, OTile, STile, TTile, ZTile]
    selected_type = choice(tile_types)
    return selected_type(root_x, root_y)


class TileGenerator:
    """Generates tiles following classic Tetris rules"""

    def __init__(self):
        self.tile_types = [ITile, JTile, LTile, OTile, STile, TTile, ZTile]
        self.history = []

    def next_tile(self, root_x, root_y):
        """
        Generate next piece using rules similar to NES Tetris:
        - Tries to avoid repeating pieces
        - Tries to avoid long droughts of I pieces
        """
        while True:
            selected_type = choice(self.tile_types)

            # Avoid repeating the last piece
            if self.history and selected_type == self.history[-1]:
                continue

            # Avoid repeating any of last 4 pieces
            if len(self.history) >= 4 and selected_type in self.history[-4:]:
                # 50% chance to reroll
                if choice([True, False]):
                    continue

            # Special handling for I piece
            if selected_type == ITile:
                # If no I piece in last 12 pieces, force one
                if len(self.history) >= 12 and ITile not in self.history[-12:]:
                    selected_type = ITile
                # If we got I piece recently, 50% chance to reroll
                elif len(self.history) >= 2 and ITile in self.history[-2:]:
                    if choice([True, False]):
                        continue

            self.history.append(selected_type)
            if len(self.history) > 12:
                self.history.pop(0)
            return selected_type(root_x, root_y)
