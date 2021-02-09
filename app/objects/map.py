from app.objects.vectorUtils import Vector
from app.objects.api import GeocoderMapObject


class MarkerType:
    flag = "flag"
    blue = "org"
    blueComma = "comma"
    blueRound = "round"
    home = "home"
    work = "work"
    yandex = "ya_ru"
    blackButton = "vkbkm"
    grayButton = "vkgrm"


class Layer:
    map = "map"
    sat = "sat"
    hyb = "sat,skl"


class Marker:
    def __init__(self, pos: Vector, markerType: str = MarkerType.flag):
        self.pos = pos
        self.markerType = markerType


class Map:
    def __init__(self):
        self.position = Vector(0, 0)
        self.size = Vector(0, 0)
        self.layer = "map"
        self.focusedAddress = None
        self.image = None
        self.markers = []
        self.update()

    def update(self):
        pass

    def addPosition(self, add: Vector):
        if self.validateCoord(self.position + add):
            self.position = self.position + add
            self.update()

    def multipleSize(self, coef: int):
        if self.validateCoord(self.size * coef):
            self.size = self.size * coef
            self.update()

    def validateCoord(self, val: Vector):
        return abs(val.y) <= 90

    def addMarker(self, marker: Marker):
        self.markers.append(marker)
        self.update()

    def setLayer(self, layer):
        self.layer = layer
        self.update()

    def resetAddress(self):
        self.focusedAddress = None
        self.update()

    def setAddress(self, address: GeocoderMapObject):
        self.focusedAddress = address
