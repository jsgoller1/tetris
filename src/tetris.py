import pygame
from src.renderer import Renderer
from src.input_handler import InputHandler
from src.game_board import GameBoard
from src.game_action import GameAction
from src.music_player import MusicPlayer


class Tetris:
    def __init__(self, width=1024, height=768):
        pygame.init()
        self._running = True
        self._renderer = Renderer(width, height)
        self._input_handler = InputHandler()
        self._game_board = GameBoard()
        self._music_player = MusicPlayer()
        self._last_update = pygame.time.get_ticks()
        self._update_delay = 800  # Delay between updates in milliseconds

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        current_time = pygame.time.get_ticks()
        if current_time - self._last_update >= self._update_delay:
            self._game_board.on_loop()
            self._last_update = current_time

        # Always render, even if game state hasn't updated
        self._renderer.on_loop(self._game_board.get_render_data())

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
        self.on_cleanup()
