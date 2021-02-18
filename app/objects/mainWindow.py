import pygame
from app.objects.pyGameButton import pyButton
from app.objects.pySwitch import pySwitch
from app.objects.inputWindow import inputWindow
from app.objects.pyMap import pyMap
from app.objects.map import MapClassObject, Layer, Marker, MarkerType
from app.objects.vectorUtils import Vector
from app.objects.api import ApiClassObject


def unitPositionSet(vect):
    positionDeltaX = 360 / (2 ** MapClassObject.size)
    positionDeltaY = 180 / (2 ** MapClassObject.size)
    return Vector(vect.x * positionDeltaX, vect.y * positionDeltaY)


class MainWindow:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.widgets = []
        self.buttons = []
        self.inputs = []
        self.font = pygame.font.SysFont('calibri', 26)
        self.createElements()
        self.setCheckKeys()
        self.setEvents()
        self.clock = pygame.time.Clock()

    def createElements(self):
        self.up = pyButton(299, 128, '↑', self.screen, self.widgets, self.buttons, 605, 50, toggle=False)
        self.down = pyButton(299, 625, '↓', self.screen, self.widgets, self.buttons, 605, 50, toggle=False)
        self.right = pyButton(900, 174, '→', self.screen, self.widgets, self.buttons, 50, 455, toggle=False)
        self.left = pyButton(253, 174, '←', self.screen, self.widgets, self.buttons, 50, 455, toggle=False)

        self.plus_size = pyButton(1000, 174, '+', self.screen, self.widgets, self.buttons, 50, 50, toggle=False)
        self.minus_size = pyButton(1000, 224, '-', self.screen, self.widgets, self.buttons, 50, 50, toggle=False)

        self.map = pyMap(300, 175, self.screen, self.widgets)

        self.scheme = pySwitch(1000, 300, self.screen, ('Карта', 'Спутник', 'Гибрид'), self.widgets)

        self.search_input = inputWindow(10, 40, 350, 25, self.screen, self.widgets, self.inputs, '', True)
        self.search_button = pyButton(10, 80, 'Искать', self.screen, self.widgets, self.buttons, 100, 50, toggle=False)
        self.dropButton = pyButton(10, 140, 'Сброс координат', self.screen, self.widgets, self.buttons, 200, 50,
                                   toggle=False)

        self.address_output = inputWindow(299, 700, 800, 25, self.screen, self.widgets, self.inputs,
                                          'Здесь будет адрес', False)
        self.organisation_output = inputWindow(299, 735, 800, 25, self.screen, self.widgets, self.inputs,
                                               'Здесь будет название организации', False)
        self.index_switch = pyButton(10, 700, 'Отображение индекса', self.screen, self.widgets, self.buttons, 260, 30,
                                     toggle=True)

    def setCheckKeys(self):
        self.up.setCheckKey(pygame.K_UP)
        self.down.setCheckKey(pygame.K_DOWN)
        self.left.setCheckKey(pygame.K_LEFT)
        self.right.setCheckKey(pygame.K_RIGHT)
        self.plus_size.setCheckKey(pygame.K_PAGEUP)
        self.minus_size.setCheckKey(pygame.K_PAGEDOWN)

    def setEvents(self):
        self.dropButton.setEventHandler(self.resetMarkers)

        self.scheme.setEventHandler(lambda x: MapClassObject.setLayer((Layer.map, Layer.sat, Layer.hyb)[x]))

        self.up.setEventHandler(lambda: MapClassObject.addPosition(unitPositionSet(Vector(0, 1))))
        self.down.setEventHandler(lambda: MapClassObject.addPosition(unitPositionSet(Vector(0, -1))))
        self.left.setEventHandler(lambda: MapClassObject.addPosition(unitPositionSet(Vector(-1, 0))))
        self.right.setEventHandler(lambda: MapClassObject.addPosition(unitPositionSet(Vector(1, 0))))

        self.plus_size.setEventHandler(lambda: MapClassObject.addSize(1))
        self.minus_size.setEventHandler(lambda: MapClassObject.addSize(-1))

        self.index_switch.setEventHandler(self.indexSwitch)
        self.search_button.setEventHandler(self.search)

        self.map.setEventHandler(self.mouseClickSearch)

    def tick(self):
        self.screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                for widget in self.widgets:
                    widget.checkMouse(event)
            if event.type == pygame.KEYDOWN:
                for el in self.inputs:
                    el.keyboardButtonPressed(event)
                for el in self.buttons:
                    el.checkKeyboard(event)
        [x.mouseonButton(pygame.mouse.get_pos()) for x in self.buttons]
        [x.draw() for x in self.widgets]
        pygame.display.flip()
        self.clock.tick(60)

    def search(self):
        if self.search_input.getText().strip() == '':
            return
        MapObject = ApiClassObject.findAddressGeocoder(self.search_input.getText())
        self.resetMarkers()
        MapClassObject.setAddress(MapObject)
        MapClassObject.setPosition(MapObject.getPostion())
        MapClassObject.addMarker(Marker(MapObject.getPostion(), MarkerType.blueComma))
        MapClassObject.setSize(MapObject.getSize())
        MapClassObject.update()
        self.address_output.setText(
            MapClassObject.focusedAddress.getAddress() + (
                (" Индекс: " + MapClassObject.focusedAddress.getIndex()) if self.index_switch.pressed else ""))

    def indexSwitch(self, switch):
        if MapClassObject.focusedAddress is not None:
            self.address_output.setText(
                MapClassObject.focusedAddress.getAddress() + (
                    (" Индекс: " + MapClassObject.focusedAddress.getIndex()) if self.index_switch.pressed else ""))

    def resetMarkers(self):
        MapClassObject.markers = []
        MapClassObject.update()
        self.address_output.setText("")
        self.search_input.setText("")
        self.organisation_output.setText("")

    def mouseClickSearch(self, coords, event):
        if event.button == pygame.BUTTON_LEFT:
            self.resetMarkers()
            MapObject = ApiClassObject.findAddressGeocoder(coords.toString())
            MapClassObject.setAddress(MapObject)
            MapClassObject.addMarker(Marker(MapObject.getPostion(), MarkerType.blueComma))
            MapClassObject.update()
            self.address_output.setText(
                MapClassObject.focusedAddress.getAddress() + (
                    (" Индекс: " + MapClassObject.focusedAddress.getIndex()) if self.index_switch.pressed else ""))
        if event.button == pygame.BUTTON_RIGHT:
            self.resetMarkers()
            MapObject = ApiClassObject.requestOrganization("магазин", params={"ll": coords.toString()})
            if MapObject.getPostion() is None:
                return
            MapClassObject.setAddress(MapObject)
            self.address_output.setText(
                MapClassObject.focusedAddress.getAddress() + (
                    (" Индекс: " + MapClassObject.focusedAddress.getIndex()) if self.index_switch.pressed else ""))
            self.organisation_output.setText(MapClassObject.focusedAddress.getName())
            MapClassObject.addMarker(Marker(MapObject.getPostion(), MarkerType.flag))
            MapClassObject.update()


MainWindowClassObject = MainWindow()
