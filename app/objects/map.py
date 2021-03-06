from app.objects.vectorUtils import Vector
from app.objects.api import GeocoderMapObject, ApiClassObject


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

    def toString(self):
        return self.pos.toString() + "," + self.markerType


class Map:
    def __init__(self):
        self.position = Vector(0, 0)
        self.size = 1
        self.layer = "map"
        self.focusedAddress = None
        self.image = None
        self.markers = []
        self.update()

    def update(self):
        self.image = ApiClassObject.loadMap(self)

    def addPosition(self, add: Vector):
        if self.validateCoord(self.position + add):
            self.position = self.position + add
            self.update()

    def setPosition(self, v: Vector):
        if self.validateCoord(v):
            self.position = v

    def addSize(self, addSize: int):
        if 0 <= (self.size + addSize) <= 17:
            self.size = self.size + addSize
            self.update()

    def setSize(self, size: int):
        if 0 <= size <= 17:
            self.size = size

    def validateCoord(self, val: Vector):
        return abs(val.y) <= 85 and abs(val.x) < 180

    def addMarker(self, marker: Marker):
        self.markers.append(marker)

    def setLayer(self, layer):
        self.layer = layer
        self.update()

    def resetAddress(self):
        self.focusedAddress = None
        self.update()

    def setAddress(self, address: GeocoderMapObject):
        self.focusedAddress = address


MapClassObject = Map()
