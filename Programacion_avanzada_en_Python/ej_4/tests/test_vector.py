from geom2d import Vector
import pytest
import math

@pytest.mark.parametrize(
    "a,expected", [
        (Vector(2, 3), math.sqrt(13))
    ]
)
def test_vector_mod(a, expected):
    assert a.mod == expected
