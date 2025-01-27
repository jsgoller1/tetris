from dataclasses import dataclass
from typing import Optional
from src.color import Color


@dataclass
class RenderData:
    grid_colors: list[list[Optional[Color]]]  # The fixed blocks
    active_piece_positions: list[tuple[int, int]]  # Current piece positions
    active_piece_color: Color
