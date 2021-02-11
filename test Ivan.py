import pygame
from app.objects.pyGameButton import pyButton
from app.objects.pySwitch import pySwitch
from app.objects.inputWindow import inputWindow
from app.objects.pyMap import pyMap
from app.objects.map import MapClassObject
from app.objects.vectorUtils import Vector

MapClassObject.setSize(Vector(20, 20))
MapClassObject.setPosition(Vector(55.755151, 37.612891))
MapClassObject.update()
pygame.init()
screen = pygame.display.set_mode((1200, 800))
widgets = []
buttons = []
inputs = []
font = pygame.font.SysFont('calibri', 26)

up = pyButton(300, 125, '↑', screen, widgets, buttons, 600, 50, toggle=False)
down = pyButton(300, 625, '↓', screen, widgets, buttons, 600, 50, toggle=False)
left = pyButton(900, 174, '→', screen, widgets, buttons, 50, 450, toggle=False)
map = pyMap(300, 175, screen, widgets)

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
                widget.checkMouse(event)
        if event.type == pygame.KEYDOWN:
            for el in inputs:
                el.keyboardButtonPressed(event)
    [x.mouseonButton(pygame.mouse.get_pos()) for x in buttons]
    [x.draw() for x in widgets]
    pygame.display.flip()
    clock.tick(60)
