class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int):
        return Point(self.x * other, self.y * other)

    def __truediv__(self, other: int):
        return Point(self.x / other, self.y / other)

    def toString(self):
        return f'{x}, {y}'


class Vector:
    def __init__(self, pointA: Point, pointB: Point):
        self.pointA = pointA
        self.pointB = pointB

    def getLenght(self):
        return ((self.pointA.x - self.pointB.x) ** 2 + \
                (self.pointA.y - self.pointB.y) ** 2) ** 0.5

    def __add__(self, other):
        return Vector(self.pointA + other.pointA, self.pointB + other.pointB)

    def __sub__(self, other):
        return Vector(self.pointA - other.pointA, self.pointB - other.pointB)

    def __mul__(self, other: int):
        return Vector(self.pointA, self.pointB * other)

    def __truediv__(self, other: int):
        return Vector(self.pointA, self.pointB / other)
