import pygame


class Renderer:
    def __init__(self, width: int, height: int):
        self.size = width, height
        self._display_surf: pygame.Surface = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF
        )

    def draw(self):
        # Fill the background with a color (e.g., black)
        self._display_surf.fill((0, 0, 0))

        # Example: Draw a red rectangle
        pygame.draw.rect(self._display_surf, (255, 0, 0), (100, 100, 50, 50))

        # Example: Draw a white circle
        pygame.draw.circle(self._display_surf, (255, 255, 255), (200, 200), 30)

        # IMPORTANT: Update the display to show the changes
        pygame.display.flip()
