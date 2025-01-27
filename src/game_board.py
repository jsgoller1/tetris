from typing import List, Tuple
from src.tile import Tile, TileGenerator
from src.tile import Color
from src.render_data import GameBoardRenderData


class GameBoard:
    """
    GameBoard represents the actual Tetris grid and
    stores which cells are currently occupied.
    """

    def __init__(self, width=10, height=22):
        self.width = width
        self.height = height
        self.grid: List[List[Color | None]] = [
            [None for _ in range(width)] for _ in range(height)
        ]
        self.tile_generator = TileGenerator()
        self.spawn_x = width // 2
        self.spawn_y = 0
        self.active_tile: Tile = self.tile_generator.next_tile(
            self.spawn_x, self.spawn_y
        )
        self.tile_queue = [self.tile_generator.next_tile(self.spawn_x, self.spawn_y)]

    def is_game_over(self):
        # Check the two hidden rows (20 and 21 if 0-based indexing)
        return any(
            [
                self.grid[row][col]
                for col in range(self.width)
                for row in range(self.height - 2, self.height)
            ]
        )

    def _add_tile(self):
        # Get the next tile from the queue and set it as active
        self.active_tile = self.tile_queue.pop()

        # Add a new tile to the front of the queue
        self.tile_queue.append(
            self.tile_generator.next_tile(self.spawn_x, self.spawn_y)
        )

    def _active_tile_will_collide(self):
        for block in self.active_tile.get_blocks():
            # Check if block would hit bottom of screen
            if block[1] + 1 >= self.height:
                return True
            # Check if block would collide with existing blocks
            if (
                block[1] + 1 < self.height
                and self.grid[block[1] + 1][block[0]] is not None
            ):
                return True
        return False

    def _lock_active_tile(self):
        if self.active_tile:
            for block in self.active_tile.get_blocks():
                self.grid[block[1]][block[0]] = self.active_tile.get_color()
            self._add_tile()

    def _is_row_full(self, row_idx: int):
        return all(self.grid[row_idx])

    def _clear_rows(self) -> int:
        """Clear full rows and return number of rows cleared"""
        rows_cleared = 0
        y = self.height - 1
        while y >= 0:
            if self._is_row_full(y):
                # Move all rows above down
                for row in range(y, 0, -1):
                    self.grid[row] = self.grid[row - 1][:]
                # Clear top row
                self.grid[0] = [None for _ in range(self.width)]
                rows_cleared += 1
            else:
                y -= 1
        return rows_cleared

    def on_loop(self) -> int:
        """
        Update game board state and return number of rows cleared
        Returns:
            int: Number of rows cleared in this update
        """
        if self._active_tile_will_collide():
            self._lock_active_tile()
            return self._clear_rows()
        else:
            self.active_tile.move_down()
            return 0

    def get_render_data(self) -> GameBoardRenderData:
        """Get the current game board state for rendering"""
        return GameBoardRenderData(
            grid_colors=self.grid,
            active_piece_positions=self.active_tile.get_blocks(),
            active_piece_color=self.active_tile.get_color(),
            next_piece_positions=self.tile_queue[0].get_blocks(),
            next_piece_color=self.tile_queue[0].get_color(),
        )
