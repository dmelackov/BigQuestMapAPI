import pygame


class pyButton:
    def __init__(self, x, y, text, screen, arr, buttons, toggle=False):
        self.handler = None
        self.mouse = 0
        arr.append(self)
        buttons.append(self)
        self.x = x
        self.mode = 0
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
        self.timer = 100000
        self.anim = 0

    def setEventHandler(self, handler):
        self.handler = handler

    def timerCheck(self):
        if self.timer < 15:
            self.timer += 1
            self.anim = 1
            return
        self.anim = 0
        return

    def draw(self):
        self.timerCheck()
        if self.anim == 1:
            pygame.draw.rect(self.screen, (45, 45, 45),
                             (self.x - self.k, self.y - self.k, self.width + 2 * self.k, self.height + 2 * self.k))
            self.string = self.font.render(self.text, True, pygame.Color(0, 0, 0))
            self.screen.blit(self.string, self.intro_rect)
        elif self.toggle and self.mode and self.mouse:
            pygame.draw.rect(self.screen, (120, 120, 120),
                             (self.x - self.k, self.y - self.k, self.width + 2 * self.k, self.height + 2 * self.k))
            self.string = self.font.render(self.text, True, pygame.Color(0, 0, 0))
            self.screen.blit(self.string, self.intro_rect)
        elif self.mouse == 1:
            self.string = self.font.render(self.text, True, pygame.Color(120, 120, 120))
            self.screen.blit(self.string, self.intro_rect)
            pygame.draw.rect(self.screen, (120, 120, 120),
                             (self.x - self.k, self.y - self.k, self.width + 2 * self.k, self.height + 2 * self.k),
                             width=1)
        elif self.mode == 1:
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

    def checkMouse(self, mouse_pos):
        if self.toggle:
            x = mouse_pos[0]
            y = mouse_pos[1]
            if self.x - self.k <= x <= self.x + self.width + 2 * self.k and self.y - self.k <= y <= self.y \
                    + self.height + 2 * self.k:
                self.mode = (self.mode + 1) % 2
                self.timer = 0
                if self.handler:
                    self.handler(self.pressed)
            return
        else:
            x = mouse_pos[0]
            y = mouse_pos[1]
            if self.x - self.k <= x <= self.x + self.width + 2 * self.k and self.y - self.k <= y <= self.y \
                    + self.height + 2 * self.k:
                self.timer = 0
                if self.handler:
                    self.handler()

    def mouseonButton(self, mouse_pos):
        x = mouse_pos[0]
        y = mouse_pos[1]
        if self.x - self.k <= x <= self.x + self.width + 2 * self.k and self.y - self.k <= y <= self.y \
                + self.height + 2 * self.k:
            self.mouse = 1
        else:
            self.mouse = 0
