import pygame
from src.game_action import GameAction


class InputHandler:
    def __init__(self):
        pass

    def handle_input(self, event):
        if event.type != pygame.KEYDOWN:
            return GameAction.NoAction

        if event.key == pygame.K_LEFT:
            return GameAction.MoveLeft
        elif event.key == pygame.K_RIGHT:
            return GameAction.MoveRight
        elif event.key == pygame.K_UP:
            return GameAction.Rotate
        elif event.key == pygame.K_DOWN:
            return GameAction.HardDrop
        elif event.key == pygame.K_SPACE:
            return GameAction.Pause
        elif event.key == pygame.K_ESCAPE:
            return GameAction.Quit

        return GameAction.NoAction
