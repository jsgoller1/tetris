import pygame
from src.renderer import Renderer
from src.input_handler import InputHandler
from src.game_board import GameBoard
from src.game_action import GameAction
from src.music_player import MusicPlayer
from src.score_keeper import ScoreKeeper


class Tetris:
    def __init__(self, width=550, height=500):
        pygame.init()
        self._running = True
        self._renderer = Renderer(width, height)
        self._input_handler = InputHandler()
        self._game_board = GameBoard()
        self._score_keeper = ScoreKeeper()
        self._music_player = MusicPlayer()
        self._last_update = pygame.time.get_ticks()
        self._update_delay = 800  # Delay between updates in milliseconds

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        action = self._input_handler.handle_input(event)
        if action == GameAction.Quit:
            self._running = False
        elif action == GameAction.Pause:
            if self._music_player.is_paused:
                self._music_player.unpause()
            else:
                self._music_player.pause()
        elif action == GameAction.MoveLeft:
            self._game_board.active_tile_move_left()
        elif action == GameAction.MoveRight:
            self._game_board.active_tile_move_right()
        elif action == GameAction.Rotate:
            self._game_board.active_tile_rotate()
        elif action == GameAction.HardDrop:
            self._game_board.active_tile_hard_drop()

    def on_loop(self):
        if self._game_board.is_game_over():
            self._running = False
            return

        current_time = pygame.time.get_ticks()
        if current_time - self._last_update >= self._update_delay:
            # Update game board and get number of cleared lines
            rows_cleared = self._game_board.on_loop()

            # Update score if rows were cleared
            if rows_cleared > 0:
                self._score_keeper.add_cleared_lines(rows_cleared)

            self._last_update = current_time

            # Update game speed based on level
            self._update_delay = max(100, 800 - (self._score_keeper.level - 1) * 50)

        # Always render, even if game state hasn't updated
        self._renderer.on_loop(
            self._game_board.get_render_data(),
            self._score_keeper.get_render_data(),
        )

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
        self.on_cleanup()
