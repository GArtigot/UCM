from .vector import Vector
from typing import Self


class Point(Vector):
    def __init__(self, x: float = 1.0, y: float = 1.0):
        Vector.__init__(self, x, y)

    def __repr_(self) -> str:
        return f'P({self.x}, {self.y})'

    def __hash__(self):
        return hash((self.x, self.y))

    def __sub__(self, other: Self):
        return Vector(self.x - other.x, self.y - other.y)

    def distance(self, other: Self) -> float:
        difference = self - other
        return difference.mod