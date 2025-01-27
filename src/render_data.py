from dataclasses import dataclass
from typing import Optional
from src.color import Color


@dataclass
class GameBoardRenderData:
    grid_colors: list[list[Optional[Color]]]  # The fixed blocks
    active_piece_positions: list[tuple[int, int]]  # Current piece positions
    active_piece_color: Color
    next_piece_positions: list[tuple[int, int]]  # Next piece preview positions
    next_piece_color: Color


@dataclass
class ScoreboardRenderData:
    score: int
    level: int
    lines_cleared: int
