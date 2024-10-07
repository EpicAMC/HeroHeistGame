'''
BoardView

BoardView is responsible for drawing the board surface to the screen.
'''

import pygame
from model.board import Board
from math import sin, cos, pi, sqrt

class BoardView:
    TILE_COLOR = (40, 175, 20)
    TILE_BORDER_COLOR = (0, 0, 0)
    TILE_BORDER_WIDTH = 3

    def __init__(self, game_width, game_height):
        self.surface = pygame.Surface((game_width / 3 * 2, game_height), pygame.SRCALPHA, 32)

    def draw(self, root: pygame.Surface):
        root.blit(self.surface, (0, 0))
    
    def update(self, board: Board):
        # Clear the surface
        self.surface.fill((0, 0, 0, 0))  # Transparent background

        # Calculate the maximum radius that will fit within the surface with 5% margin
        max_height = self.surface.get_height() * 0.9
        
        # Calculate the radius based on the board size and available space
        radius = max_height / (2 * board.radius * 2)
        
        # Calculate the center of the surface
        center_x = self.surface.get_width() / 2
        center_y = self.surface.get_height() / 2
        
        # Calculate the horizontal and vertical spacing between hexagon centers
        h_spacing = radius * 3 / 2
        v_spacing = radius * sqrt(3)
        
        # Draw each hexagon in the board
        for (q, r), tile in board.tiles.items():
            # Calculate the position of the hexagon
            x = center_x + h_spacing * q
            y = center_y + v_spacing * r / 2
            
            # Draw the hexagon
            self.draw_hexagon(radius, (x, y))

    def draw_hexagon(self, radius, position):
        # Draws a hexagon on the surface centered at position with radius
        n, r = 6, radius
        x, y = position
        pygame.draw.polygon(
            self.surface,
            self.TILE_COLOR,
            [(x + r * cos(2 * pi * i / n), y + r * sin(2 * pi * i / n)) for i in range(n)],
            0
        )
        pygame.draw.polygon(
            self.surface,
            self.TILE_BORDER_COLOR,
            [(x + r * cos(2 * pi * i / n), y + r * sin(2 * pi * i / n)) for i in range(n)],
            self.TILE_BORDER_WIDTH
        )

