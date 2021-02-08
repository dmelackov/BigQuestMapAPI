import pygame


class pyButton:
    def __init__(self, x, y, text, screen):
        self.x = x
        self.y = y
        self.text = text
        self.screen = screen
        self.font = pygame.font.Font(None, 30)
        self.string = self.font.render(self.text, True, pygame.Color(255, 255, 255))
        self.intro_rect = self.string.get_rect()
        self.intro_rect.x = self.x
        self.intro_rect.top = self.y
        self.width = self.intro_rect.width
        self.height = self.intro_rect.height

    def draw(self):
        self.screen.blit(self.string, self.intro_rect)
