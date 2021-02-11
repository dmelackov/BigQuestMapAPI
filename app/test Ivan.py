import pygame
from objects.pyGameButton import pyButton
from objects.pySwitch import pySwitch
from objects.inputWindow import inputWindow

pygame.init()
screen = pygame.display.set_mode((1200, 800))
widgets = []
buttons = []
inputs = []
font = pygame.font.SysFont('calibri', 26)

up = pyButton(300, 176, '↑', screen, widgets, buttons, 600, 50, toggle=False)
down = pyButton(300, 625, '↓', screen, widgets, buttons, 600, 50, toggle=False)
left = pyButton(900, 101, '→', screen, widgets, buttons, 50, 400, toggle=False)

pygame.display.flip()
clock = pygame.time.Clock()
while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            for widget in widgets:
                widget.checkMouse(event.pos)
        if event.type == pygame.KEYDOWN:
            for el in inputs:
                el.keyboardButtonPressed(event)
    [x.mouseonButton(pygame.mouse.get_pos()) for x in buttons]
    [x.draw() for x in widgets]
    pygame.draw.rect(screen, (255, 255, 255),
                     (300, 175, 600, 450), width=1)
    string = font.render('Место для карты', True, pygame.Color(255, 255, 255))
    screen.blit(string, (500, 380, 200, 50))
    pygame.display.flip()
    clock.tick(60)
