import pygame
from src.render_data import RenderData
from src.color import Color


class Renderer:
    def __init__(self, width: int, height: int):
        self.size = width, height
        pygame.display.set_caption("Tetris")
        self._display_surf: pygame.Surface = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF
        )

    def draw(self, render_data: RenderData):
        # Fill the background with a color (e.g., black)
        self._display_surf.fill((0, 0, 0))

        # Draw the grid
        for y, row in enumerate(render_data.grid_colors):
            for x, color in enumerate(row):
                if color:
                    pygame.draw.rect(
                        self._display_surf, color.value, (x * 10, y * 10, 10, 10)
                    )

        # Draw the active piece
        for x, y in render_data.active_piece_positions:
            pygame.draw.rect(
                self._display_surf,
                render_data.active_piece_color.value,
                (x * 10, y * 10, 10, 10),
            )

        # IMPORTANT: Update the display to show the changes
        pygame.display.flip()

    def on_loop(self, render_data: RenderData):
        self.draw(render_data)
