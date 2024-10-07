import pygame
from model.board import Board
from view.gameview import GameView

class Game:
    GAME_WIDTH = 1728
    GAME_HEIGHT = 972

    def __init__(self):
        self.board = Board(5)
        self.view = None

    def run(self):
        pygame.init()
        self.view = GameView(pygame.display.set_mode((self.GAME_WIDTH, self.GAME_HEIGHT)))

        # Draw initial board
        self.view.updateBoard(self.board)

        self.view.draw()
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    
                    