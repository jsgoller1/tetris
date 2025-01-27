import pygame
from renderer import Renderer
from input_handler import InputHandler
from game_board import GameBoard
from game_action import GameAction


class Tetris:
    def __init__(self, width=640, height=400):
        pygame.init()
        self._running = True
        self._renderer = Renderer(width, height)
        self._input_handler = InputHandler()
        self._game_board = GameBoard()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_render(self):
        self._renderer.draw()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    tetris = Tetris()
    tetris.on_execute()
