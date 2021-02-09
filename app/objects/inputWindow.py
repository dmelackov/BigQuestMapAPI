import pygame


class inputWindow:
    def __init__(self, x, y, width, height, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = ''
        self.k = 3
        self.i = 0
        self.active = False
        self.screen = screen
        self.fbuttons = [f'f{x}' for x in range(1, 13)]
        a = 1
        font = pygame.font.Font(None, a)
        string = font.render('Test string', True, pygame.Color(255, 255, 255))
        rect = string.get_rect()
        while rect.height < self.height:
            a += 1
            font = pygame.font.SysFont('calibri', a)
            string = font.render('Test string', True, pygame.Color(255, 255, 255))
            rect = string.get_rect()
        a -= 1
        self.font = pygame.font.SysFont('calibri', a)
        string = font.render('D', True, pygame.Color(255, 255, 255))
        self.one_sym = string.get_rect().width
        while self.width % self.one_sym:
            self.width += 1

    def getText(self):
        return self.text

    def checkActivated(self, mouse_pos):
        x, y = mouse_pos
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            self.active = not self.active
        else:
            self.active = False

    def keyboardButtonPressed(self, event):
        button = event.unicode
        if self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif button:
                self.text += button

    def draw(self):
        x = self.x
        y = self.y

        if self.active:
            pygame.draw.rect(self.screen, (255, 255, 255),
                             (self.x - self.k, self.y - self.k, self.width + self.k * 2,
                              self.height + 2 * self.k))
            for sym in self.text[-self.width // self.one_sym - 4:]:
                x += self.render(sym, (x, y))
                if x > self.width:
                    self.i += 1
        else:
            pygame.draw.rect(self.screen, (255, 255, 255),
                             (self.x - self.k, self.y - self.k, self.width + self.k * 2,
                              self.height + 2 * self.k), width=1)
            for sym in self.text[-self.width // self.one_sym - 4:]:
                x += self.render(sym, (x, y), (255, 255, 255))

    def render(self, sym, coords, color=(0, 0, 0)):
        string = self.font.render(sym, True, pygame.Color(color))
        rect = string.get_rect()
        rect.x = coords[0]
        rect.y = coords[1]
        self.screen.blit(string, rect)
        return rect.width
