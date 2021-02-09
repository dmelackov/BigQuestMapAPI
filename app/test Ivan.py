import pygame
from objects.pyGameButton import pyButton
from objects.pySwitch import pySwitch
from objects.inputWindow import inputWindow


pygame.init()
screen = pygame.display.set_mode((600, 450))
widgets = []
buttons = []
inputs = []
d = inputWindow(10, 150, 350, 30, screen, widgets, inputs)
c = pySwitch(200, 50, screen, ('First', 'Second', 'Third'), widgets ,False)
a = pyButton(10, 10, 'Это тестовая кнопка', screen,widgets, buttons, True)
b = pyButton(200, 400, 'Это тестовая кнопка 2', screen,buttons, widgets)
pygame.display.flip()
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
    pygame.display.flip()
