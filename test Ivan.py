import pygame
from app.objects.pyGameButton import pyButton
from app.objects.pySwitch import pySwitch
from app.objects.inputWindow import inputWindow
from app.objects.pyMap import pyMap
from app.objects.map import MapClassObject, Layer, Marker, MarkerType
from app.objects.vectorUtils import Vector
from app.objects.api import ApiClassObject

MapClassObject.setPosition(Vector(0, 0))
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
search_input = inputWindow(10, 40, 350, 25, screen, widgets, inputs, 'Введите объект для поиска', True)
search_button = pyButton(10, 80, 'Искать', screen, widgets, buttons, 100, 50, toggle=False)
dropButton = pyButton(10, 140, 'Сброс координат', screen, widgets, buttons, 200, 50, toggle=False)

address_output = inputWindow(299, 700, 600, 25, screen, widgets, inputs, 'Здесь будет адрес', False)
index_switch = pyButton(10, 700, 'Отображение индекса', screen, widgets, buttons, 260, 30, toggle=True)

up.setCheckKey(pygame.K_UP)
down.setCheckKey(pygame.K_DOWN)
left.setCheckKey(pygame.K_LEFT)
right.setCheckKey(pygame.K_RIGHT)
plus_size.setCheckKey(pygame.K_PAGEUP)
minus_size.setCheckKey(pygame.K_PAGEDOWN)


def resetMarkers():
    MapClassObject.markers = []
    MapClassObject.update()
    address_output.setText("")


dropButton.setEventHandler(resetMarkers)

scheme.setEventHandler(lambda x: MapClassObject.setLayer((Layer.map, Layer.sat, Layer.hyb)[x]))


def unitPositionSet(vect):
    positionDeltaX = 360 / (2 ** MapClassObject.size)
    positionDeltaY = 180 / (2 ** MapClassObject.size)
    return Vector(vect.x * positionDeltaX, vect.y * positionDeltaY)


def search():
    MapObject = ApiClassObject.findAddressGeocoder(search_input.getText())
    MapClassObject.setAddress(MapObject)
    MapClassObject.setPosition(MapObject.getPostion())
    MapClassObject.addMarker(Marker(MapObject.getPostion(), MarkerType.blueRound))
    MapClassObject.update()
    address_output.setText(
        MapClassObject.focusedAddress.getAddress() + (
            (" Индекс: " + MapClassObject.focusedAddress.getIndex()) if index_switch.pressed else ""))


def indexSwitch(switch):
    if MapClassObject.focusedAddress is not None:
        print(index_switch.pressed)
        address_output.setText(
            MapClassObject.focusedAddress.getAddress() + (
                (" Индекс: " + MapClassObject.focusedAddress.getIndex()) if index_switch.pressed else ""))


up.setEventHandler(lambda: MapClassObject.addPosition(unitPositionSet(Vector(0, 1))))
down.setEventHandler(lambda: MapClassObject.addPosition(unitPositionSet(Vector(0, -1))))
left.setEventHandler(lambda: MapClassObject.addPosition(unitPositionSet(Vector(-1, 0))))
right.setEventHandler(lambda: MapClassObject.addPosition(unitPositionSet(Vector(1, 0))))

plus_size.setEventHandler(lambda: MapClassObject.addSize(1))
minus_size.setEventHandler(lambda: MapClassObject.addSize(-1))

index_switch.setEventHandler(indexSwitch)
search_button.setEventHandler(search)

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
