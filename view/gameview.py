import pygame
from view.boardview import BoardView
from view.sidebarview import SidebarView
from model.board import Board

class GameView:
    BG_COLOR = (0, 150, 230)

    def __init__(self, root: pygame.Surface):
        self.root = root
        self.board_view = BoardView(root.get_width(), root.get_height())
        self.sidebar_view = SidebarView(root.get_width(), root.get_height())

    def draw(self):
        self.root.fill(self.BG_COLOR)
        self.board_view.draw(self.root)
        self.sidebar_view.draw(self.root)

    def updateBoard(self, board: Board):
        self.board_view.update(board)

