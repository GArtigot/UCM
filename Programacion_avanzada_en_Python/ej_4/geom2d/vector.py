import math
from typing import Self


class Vector(object):
    def __init__(self, x: float = 1.0, y: float = 1.0):
        self._x: float = x
        self._y: float = y

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @x.setter
    def x(self, x) -> None:
        self._x = x

    @y.setter
    def y(self, y) -> None:
        self._y = y

    def __str__(self) -> str:
        return f'({self.x:.4f}, {self.y:.4f})'

    def __repr__(self) -> str:
        return f'V({self.x:.4f}, {self.y:.4f})'

    @property
    def mod(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, other: Self) -> bool:
        return self.x == other.x and self.y == other.y

    def __le__(self, other: Self) -> bool:
        return self.mod <= other.mod

    def __hash__(self):
        return hash((self.x, self.y, self.mod))

    def __add__(self, other: Self):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Self):
        return Vector(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __rmul__(self, other: float):
        return Vector(self.x * other, self.y * other)

    def __mul__(self, other: Self):
        return self.x * other.x + self.y * other.y