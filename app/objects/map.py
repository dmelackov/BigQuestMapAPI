from app.objects.vectorUtils import Point


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
    def __init__(self, pos: Point, markerType: str = MarkerType.flag):
        self.pos = pos
        self.markerType = markerType


class Map:
    def __init__(self):
        self.position = Point(0, 0)
        self.size = Point(0, 0)
        self.layer = "map"
        self.focusedAddress = ""
        self.index = ""
        self.markers = []
        self.update()

    def update(self):
        pass

    def addPosition(self, add: Point):
        if self.validateCoord(self.position + add):
            self.position = self.position + add
            self.update()

    def multSize(self, coef: int):
        if self.validateCoord(self.size * coef):
            self.size = self.size * coef
            self.update()

    def validateCoord(self, val: Point):
        return abs(val.y) <= 90

    def addMarker(self, marker: Marker):
        self.markers.append(marker)
        self.update()

    def setLayer(self, layer):
        self.layer = layer
        self.update()
