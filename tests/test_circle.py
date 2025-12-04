

from geometric_lib.circle import area, perimeter
import math

def test_area():
    assert area(1) == math.pi
    assert area(3) == math.pi * 9

def test_perimeter():
    assert perimeter(1) == 2 * math.pi
    assert perimeter(5) == 10 * math.pi