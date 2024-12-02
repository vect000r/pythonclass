import pytest
from rectangles import Rectangle
from points import Point

def test_rectangle_creation():
    rect = Rectangle(0, 0, 4, 3)
    assert rect.pt1 == Point(0, 0)
    assert rect.pt2 == Point(4, 3)

def test_from_points():
    rect = Rectangle.from_points((Point(1, 1), Point(4, 5)))
    assert rect.pt1 == Point(1, 1)
    assert rect.pt2 == Point(4, 5)

def test_area():
    rect = Rectangle(0, 0, 4, 3)
    assert rect.area == 12

def test_center():
    rect = Rectangle(0, 0, 4, 4)
    assert rect.center == Point(2, 2)

def test_width_and_height():
    rect = Rectangle(0, 0, 5, 7)
    assert rect.width == 5
    assert rect.height == 7

def test_virtual_attributes():
    rect = Rectangle(1, 1, 4, 5)
    assert rect.top == 5
    assert rect.bottom == 1
    assert rect.left == 1
    assert rect.right == 4
    assert rect.topleft == Point(1, 5)
    assert rect.bottomleft == Point(1, 1)
    assert rect.topright == Point(4, 5)
    assert rect.bottomright == Point(4, 1)

def test_move():
    rect = Rectangle(0, 0, 4, 3)
    rect.move(1, 2)
    assert rect.pt1 == Point(1, 2)
    assert rect.pt2 == Point(5, 5)
