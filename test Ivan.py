import pygame
from app.objects.pyGameButton import pyButton
from app.objects.pySwitch import pySwitch
from app.objects.inputWindow import inputWindow
from app.objects.pyMap import pyMap
from app.objects.map import MapClassObject, Layer
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

up = pyButton(299, 128, '↑', screen, widgets, buttons, 605, 50, toggle=False)
down = pyButton(299, 625, '↓', screen, widgets, buttons, 605, 50, toggle=False)
right = pyButton(900, 174, '→', screen, widgets, buttons, 50, 455, toggle=False)
left = pyButton(253, 174, '←', screen, widgets, buttons, 50, 455, toggle=False)
plus_size = pyButton(1000, 174, '+', screen, widgets, buttons, 50, 50, toggle=False)
minus_size = pyButton(1000, 224, '-', screen, widgets, buttons, 50, 50, toggle=False)
map = pyMap(300, 175, screen, widgets)
scheme = pySwitch(1000, 300, screen, ('Карта', 'Спутник', 'Гибрид'), widgets)
search_input = inputWindow(10, 40, 350, 25, screen, widgets, inputs, 'Введите объект для поиска')
search_button = pyButton(10, 80, 'Искать', screen, widgets, buttons, 100, 50, toggle=False)

up.setCheckKey(pygame.K_UP)
down.setCheckKey(pygame.K_DOWN)
left.setCheckKey(pygame.K_LEFT)
right.setCheckKey(pygame.K_RIGHT)
plus_size.setCheckKey(pygame.K_PAGEUP)
minus_size.setCheckKey(pygame.K_PAGEDOWN)

scheme.setEventHandler(lambda x: MapClassObject.setLayer((Layer.map, Layer.sat, Layer.hyb)[x]))

up.setEventHandler(lambda: MapClassObject.addPosition(Vector(0, 1)))
down.setEventHandler(lambda: MapClassObject.addPosition(Vector(0, -1)))
left.setEventHandler(lambda: MapClassObject.addPosition(Vector(-1, 0)))
right.setEventHandler(lambda: MapClassObject.addPosition(Vector(1, 0)))

plus_size.setEventHandler(lambda: MapClassObject.addSize(Vector(-4 / 4, -3 / 4)))
minus_size.setEventHandler(lambda: MapClassObject.addSize(Vector(4 / 4, 3 / 4)))

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
            for el in buttons:
                el.checkKeyboard(event)
    [x.mouseonButton(pygame.mouse.get_pos()) for x in buttons]
    [x.draw() for x in widgets]
    pygame.display.flip()
    clock.tick(60)
