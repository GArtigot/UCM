from geom2d import Point
import pytest
import math

@pytest.mark.parametrize(
    "a, b, expected", [
        (Point(2, 3), Point(6,8), math.sqrt(41))
    ]
)
def test_point_distance(a, b, expected):
    assert Point.distance(a, b) == expected