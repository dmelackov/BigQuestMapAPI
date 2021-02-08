import pygame


class pyButton:
    def __init__(self, x, y, text, screen, func, arr, toggle=False):
        arr.append(self)
        self.func = func
        self.x = x
        self.y = y
        self.toggle = toggle
        if self.toggle:
            self.pressed = False
        self.text = text
        self.screen = screen
        self.font = pygame.font.Font(None, 30)
        self.string = self.font.render(self.text, True, pygame.Color(255, 255, 255))
        self.intro_rect = self.string.get_rect()
        self.intro_rect.x = self.x
        self.k = 3
        self.intro_rect.top = self.y
        self.width = self.intro_rect.width
        self.height = self.intro_rect.height

    def draw(self):
        if self.toggle:
            if self.pressed:
                pygame.draw.rect(self.screen, (255, 255, 255),
                                 (self.x - self.k, self.y - self.k, self.width + 2 * self.k, self.height + 2 * self.k))
                self.string = self.font.render(self.text, True, pygame.Color(0, 0, 0))
                self.screen.blit(self.string, self.intro_rect)
            else:
                self.string = self.font.render(self.text, True, pygame.Color(255, 255, 255))
                self.screen.blit(self.string, self.intro_rect)
                pygame.draw.rect(self.screen, (255, 255, 255),
                                 (self.x - self.k, self.y - self.k, self.width + 2 * self.k, self.height + 2 * self.k),
                                 width=1)
        else:
            self.string = self.font.render(self.text, True, pygame.Color(255, 255, 255))
            self.screen.blit(self.string, self.intro_rect)
            pygame.draw.rect(self.screen, (255, 255, 255),
                             (self.x - self.k, self.y - self.k, self.width + 2 * self.k, self.height + 2 * self.k),
                             width=1)

    def checkMouse(self, mouse_pos):
        if self.toggle:
            x = mouse_pos[0]
            y = mouse_pos[1]
            if self.x - self.k <= x <= self.x + self.width + 2 * self.k and self.y - self.k <= y <= self.y \
                    + self.height + 2 * self.k:
                self.pressed = not self.pressed
                self.func(self.pressed)
            return
        else:
            x = mouse_pos[0]
            y = mouse_pos[1]
            if self.x - self.k <= x <= self.x + self.width + 2 * self.k and self.y - self.k <= y <= self.y \
                    + self.height + 2 * self.k:
                self.func()
