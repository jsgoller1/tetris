import pygame
from src.render_data import GameBoardRenderData, ScoreboardRenderData
from src.color import Color


class Renderer:
    def __init__(self, width: int, height: int):
        self.size = width, height
        pygame.display.set_caption("Tetris")
        self._display_surf: pygame.Surface = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF
        )

        # Define regions for different components
        self.board_region = pygame.Rect(50, 10, 200, 440)  # Main game board
        self.board_outline_region = pygame.Rect(
            50, 50, 200, 400
        )  # Outline region doesn't include hidden part
        self.next_piece_region = pygame.Rect(300, 50, 100, 100)  # Next piece preview
        self.scoreboard_region = pygame.Rect(300, 200, 150, 140)  # Scoreboard

        # Initialize font for text rendering
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)

    def _draw_game_board(self, game_board: GameBoardRenderData):
        # Draw the grid
        block_size = 20
        for y, row in enumerate(game_board.grid_colors):
            for x, color in enumerate(row):
                if color:
                    pygame.draw.rect(
                        self._display_surf,
                        color.value,
                        (
                            self.board_region.x + x * block_size,
                            self.board_region.y + y * block_size,
                            block_size - 1,
                            block_size - 1,
                        ),
                    )

        # Draw the active piece
        for x, y in game_board.active_piece_positions:
            # Skip the first two hidden rows for the active piece,
            # since they are not visible to the player
            if y < 2:
                continue
            pygame.draw.rect(
                self._display_surf,
                game_board.active_piece_color.value,
                (
                    self.board_region.x + x * block_size,
                    self.board_region.y + y * block_size,
                    block_size - 1,
                    block_size - 1,
                ),
            )

        # Draw the next piece preview
        # Center the next piece in the preview region
        min_x = min(x for x, y in game_board.next_piece_positions)
        max_x = max(x for x, y in game_board.next_piece_positions)
        min_y = min(y for x, y in game_board.next_piece_positions)
        max_y = max(y for x, y in game_board.next_piece_positions)

        piece_width = (max_x - min_x + 1) * block_size
        piece_height = (max_y - min_y + 1) * block_size

        x_offset = (self.next_piece_region.width - piece_width) // 2
        y_offset = (self.next_piece_region.height - piece_height) // 2

        for x, y in game_board.next_piece_positions:
            pygame.draw.rect(
                self._display_surf,
                game_board.next_piece_color.value,
                (
                    self.next_piece_region.x + x_offset + (x - min_x) * block_size,
                    self.next_piece_region.y + y_offset + (y - min_y) * block_size,
                    block_size - 1,
                    block_size - 1,
                ),
            )

    def _draw_scoreboard(self, scoreboard: ScoreboardRenderData):
        # Draw score
        score_text = self.font.render(
            f"Score: {scoreboard.score}", True, (255, 255, 255)
        )
        self._display_surf.blit(
            score_text, (self.scoreboard_region.x + 25, self.scoreboard_region.y + 10)
        )

        # Draw level
        level_text = self.font.render(
            f"Level: {scoreboard.level}", True, (255, 255, 255)
        )
        self._display_surf.blit(
            level_text, (self.scoreboard_region.x + 25, self.scoreboard_region.y + 50)
        )

        # Draw lines cleared
        lines_text = self.font.render(
            f"Lines: {scoreboard.lines_cleared}", True, (255, 255, 255)
        )
        self._display_surf.blit(
            lines_text, (self.scoreboard_region.x + 25, self.scoreboard_region.y + 90)
        )

    def draw(self, game_board: GameBoardRenderData, scoreboard: ScoreboardRenderData):
        # Fill the background with black
        self._display_surf.fill((0, 0, 0))

        # Draw game components
        self._draw_game_board(game_board)
        self._draw_scoreboard(scoreboard)

        # Draw borders around regions
        pygame.draw.rect(
            self._display_surf, (128, 128, 128), self.board_outline_region, 2
        )
        pygame.draw.rect(self._display_surf, (128, 128, 128), self.next_piece_region, 2)
        pygame.draw.rect(self._display_surf, (128, 128, 128), self.scoreboard_region, 2)

        # Update the display
        pygame.display.flip()

    def on_loop(
        self, game_board: GameBoardRenderData, scoreboard: ScoreboardRenderData
    ):
        self.draw(game_board, scoreboard)
