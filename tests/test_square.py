

from geometric_lib.square import area, perimeter

def test_area():
    assert area(5) == 25
    assert area(0) == 0
    assert area(2.5) == 6.25

def test_perimeter():
    assert perimeter(5) == 20
    assert perimeter(0) == 0
    assert perimeter(3) == 12