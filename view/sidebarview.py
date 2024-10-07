import pygame

class SidebarView:
    SIDEBAR_COLOR = (120, 120, 120)

    def __init__(self, game_width, game_height):
        self.surface = pygame.Surface((game_width / 3, game_height), pygame.SRCALPHA, 32)
        self.surface.fill(self.SIDEBAR_COLOR)

    def draw(self, root: pygame.Surface):
        root.blit(self.surface, (root.get_width() - self.surface.get_width(), 0))
