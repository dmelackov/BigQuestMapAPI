from app.objects.map import MapClassObject
from app.objects.vectorUtils import Vector
import pygame
import math

MapClassObject.setSize(Vector(20, 20))
MapClassObject.setPosition(Vector(0, 0))
MapClassObject.update()

pygame.init()
screen = pygame.display.set_mode((600, 450))

clock = pygame.time.Clock()
MYEVENTTYPE = pygame.USEREVENT + 1
pygame.time.set_timer(MYEVENTTYPE, 500)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == MYEVENTTYPE:
            MapClassObject.addSize(Vector(0.5, 0.5))
            print(MapClassObject.size.toString())
    screen.blit(MapClassObject.image, (0, 0))
    pygame.display.flip()
pygame.quit()
