import pygame


class inputWindow:
    def __init__(self, x, y, width, height, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = ''
        self.k = 3
        self.active = False
        self.screen = screen
        self.fbuttons = [f'f{x}' for x in range(1, 13)]
        a = 1
        font = pygame.font.Font(None, a)
        string = font.render('Test string', True, pygame.Color(255, 255, 255))
        rect = string.get_rect()
        while rect.height < self.height:
            a += 1
            font = pygame.font.Font(None, a)
            string = font.render('Test string', True, pygame.Color(255, 255, 255))
            rect = string.get_rect()
        a -= 1
        string = font.render('s', True, pygame.Color(255, 255, 255))
        self.one_sym = string.get_rect().width
        self.font = pygame.font.Font(None, a)

    def getText(self):
        return self.text

    def checkActivated(self, mouse_pos):
        x, y = mouse_pos
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            self.active = not self.active
        else:
            self.active = False

    def keyboardButtonPressed(self, button):
        if self.active:
            if button == 'backspace':
                self.text = self.text[:-1]
            elif button == 'space':
                self.text += ' '
            elif 'ctrl' in button or \
                    'alt' in button or \
                    'return' in button or\
                    'delete' in button or\
                    'print screen' in button or\
                    'insert' in button or\
                    'enter' in button or\
                    'left' in button or\
                    'up' in button or\
                    'down' in button or\
                    'right' in button or\
                    'tab' in button or\
                    'caps lock' in button or\
                    'escape' in button or\
                    'break' in button or\
                    button in self.fbuttons:
                pass
            else:
                self.text += button

    def draw(self):
        text = self.text
        if len(self.text) > self.width // self.one_sym:
            text = self.text[-self.width // self.one_sym + 1:]
        if self.active:
            pygame.draw.rect(self.screen, (255, 255, 255),
                             (self.x - self.k, self.y - self.k, self.width + self.k * 2,
                              self.height + 2 * self.k))
            string = self.font.render(text, True, pygame.Color(0, 0, 0))
            rect = string.get_rect()
            rect.x = self.x
            rect.y = self.y
            self.screen.blit(string, rect)
        else:
            pygame.draw.rect(self.screen, (255, 255, 255),
                             (self.x - self.k, self.y - self.k, self.width + self.k * 2,
                              self.height + 2 * self.k), width=1)
            string = self.font.render(text, True, pygame.Color(255, 255, 255))
            rect = string.get_rect()
            rect.x = self.x
            rect.y = self.y
            self.screen.blit(string, rect)
