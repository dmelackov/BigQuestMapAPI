import pygame
from app.objects.map import MapClassObject


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

    def checkMouse(self, mouse_pos):
        absX, absY = mouse_pos[0], mouse_pos[1]
        relX = absX - self.x
        relY = absY - self.y
        if relX >= self.width or relX < 0:
            return
        if relY >= self.height or relY < 0:
            return
        print("MapRel:", relX, relY)
