import pygame


class pySwitch:
    def __init__(self, x, y, screen, variants, orientation=False):
        self.x = x
        self.y = y
        self.handler = None
        self.orientation = orientation
        self.screen = screen
        self.variants = variants
        self.font = pygame.font.Font(None, 30)
        self.coords = []
        self.bools = [False] * len(variants)
        self.k = 3
        self.max_width = 0
        for i in range(len(self.variants)):
            string = self.font.render(self.variants[i], True, pygame.Color(255, 255, 255))
            intro_rect = string.get_rect()
            intro_rect.x = self.x
            intro_rect.y = self.y
            self.max_width = max(self.max_width, intro_rect.width)
            if orientation:
                self.x += intro_rect.width + self.k * 2
            else:
                self.y += intro_rect.height + self.k * 2
            self.coords.append(intro_rect)
        for i in range(len(self.variants)):
            self.coords[i].width = self.max_width
        print(self.coords)

    def setEventHandler(self, handler):
        self.handler = handler

    def draw(self):
        for i in range(len(self.variants)):
            x, y, width, height = self.coords[i]
            if self.bools[i]:
                pygame.draw.rect(self.screen, (255, 255, 255),
                                 (x - self.k, y - self.k, width + self.k * 2,
                                  height + 2 * self.k))
                string = self.font.render(self.variants[i], True, pygame.Color(0, 0, 0))
                self.screen.blit(string, self.coords[i])
            else:
                pygame.draw.rect(self.screen, (255, 255, 255),
                                 (x - self.k, y - self.k, width + self.k * 2,
                                  height + 2 * self.k), width=1)
                string = self.font.render(self.variants[i], True, pygame.Color(255, 255, 255))
                self.screen.blit(string, self.coords[i])

    def mouseCheck(self, mouse_pos):
        x, y = mouse_pos
        for i in range(len(self.variants)):
            if self.coords[i].x - self.k <= x <= self.coords[i].x + self.coords[i].width + 2 * self.k and self.coords[i].y - self.k <= y <= self.coords[i].y \
                    + self.coords[i].height + 2 * self.k:
                self.bools = [False] * len(self.variants)
                self.bools[i] = True
