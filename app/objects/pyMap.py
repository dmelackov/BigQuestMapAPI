import pygame
from app.objects.map import MapClassObject, Marker, MarkerType
from app.objects.vectorUtils import Vector
import math


class pyMap:
    def __init__(self, x, y, screen, widgets):
        widgets.append(self)
        self.x = x
        self.y = y
        self.screen = screen
        self.width = 600
        self.height = 450

    def draw(self):
        self.screen.blit(MapClassObject.image, (self.x, self.y))

    def checkMouse(self, event):
        absX, absY = event.pos
        relX = absX - self.x
        relY = absY - self.y
        if relX >= self.width or relX < 0:
            return
        if relY >= self.height or relY < 0:
            return
        relCoords = Vector(relX - self.width // 2, -(relY - self.height // 2))
        global Ycoef

        pixelAbs = Vector(merc_x(MapClassObject.position.x, MapClassObject.size),
                          merc_y(MapClassObject.position.y, MapClassObject.size))

        pixelAbs += relCoords

        lat, long = intoLatAndLong(pixelAbs.x, pixelAbs.y, MapClassObject.size)
        gradAbs = Vector(long, lat)
        MapClassObject.addMarker(Marker(gradAbs, MarkerType.flag))
        MapClassObject.update()


# Кто тронет хоть одну константу - тот пидорас
Xcoef = 0.711827042
Ycoef = 0.711827042


def merc_x(lon, z):
    r_major = 6378137.000
    return r_major * math.radians(lon) * (Xcoef / 111319.49079327357 * 2 ** z)


def merc_y(lat, z):
    if lat > 89.5: lat = 89.5
    if lat < -89.5: lat = -89.5
    r_major = 6378137.000
    r_minor = 6378137.000
    temp = r_minor / r_major
    eccent = math.sqrt(1 - temp ** 2)
    phi = math.radians(lat)
    sinphi = math.sin(phi)
    con = eccent * sinphi
    com = eccent / 2
    con = ((1.0 - con) / (1.0 + con)) ** com
    ts = math.tan((math.pi / 2 - phi) / 2) / con
    y = 0 - r_major * math.log(ts)
    return y * (Ycoef / 111319.49079327357 * 2 ** z)


def intoLatAndLong(Xin, Yin, z):
    Y = Yin / (Ycoef / 111319.49079327357 * 2 ** z)
    X = Xin / (Xcoef / 111319.49079327357 * 2 ** z)
    a = 6378137
    b = 6378137
    f = (a - b) / a
    e = math.sqrt(2 * f - f ** 2)
    pih = math.pi / 2
    ts = math.exp(-Y / a)
    phi = pih - 2 * math.atan(ts)
    con = e * math.sin(phi)
    dphi = pih - 2 * math.atan(ts * ((1 - con) / (1 + con)) ** e) - phi
    phi = phi + dphi
    rLong = X / a
    rLat = phi
    Long = rLong * 180 / math.pi
    Lat = rLat * 180 / math.pi
    return Lat, Long
