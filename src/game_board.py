from tile import TileGenerator
import random


class GameBoard:
    """
    GameBoard represents the actual Tetris grid and
    stores which cells are currently occupied.
    """

    def __init__(self, width=10, height=22):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.tile_generator = TileGenerator()
        self.spawn_x = width // 2
        self.spawn_y = 0
        self.tile_queue = [self.tile_generator.next_tile(0, 0)]

    def is_game_over(self):
        # Check the two hidden rows (20 and 21 if 0-based indexing)
        return any(
            [
                self.grid[row][col]
                for col in range(self.width)
                for row in range(self.height - 2, self.height)
            ]
        )

    def add_tile(self):
        # Get the next tile from the queue and set it as active
        self.active_tile = self.tile_queue.pop()

        # Add a new tile to the front of the queue
        self.tile_queue.append(
            self.tile_generator.next_tile(self.spawn_x, self.spawn_y)
        )
