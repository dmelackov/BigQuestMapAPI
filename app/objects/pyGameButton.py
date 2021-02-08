import pygame


class pyButton:
    def __init__(self, x, y, text, screen):
        self.x = x
        self.y = y
        self.text = text
        self.screen = screen
        self.font = pygame.font.Font(None, 30)

    def draw(self):
        string = self.font.render(self.text, 1, pygame.Color(255, 255, 255))
        intro_rect = string.get_rect()
        intro_rect.x = self.x
        intro_rect.top = self.x
