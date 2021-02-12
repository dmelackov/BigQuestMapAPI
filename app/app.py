from app.objects.map import MapClassObject
from app.objects.vectorUtils import Vector
from app.objects.mainWindow import MainWindowClassObject


def main():
    MapClassObject.setPosition(Vector(0, 0))
    MapClassObject.update()
    while True:
        MainWindowClassObject.tick()
