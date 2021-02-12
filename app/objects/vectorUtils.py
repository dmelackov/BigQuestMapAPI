class Vector:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int):
        return Vector(self.x * other, self.y * other)

    def __truediv__(self, other: int):
        return Vector(self.x / other, self.y / other)

    def toString(self):
        return f'{round(self.x, 10)},{round(self.y, 10)}'
