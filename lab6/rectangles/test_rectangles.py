import unittest
from points import Point
from rectangles import Rectangle

class TestRectangle(unittest.TestCase):
    def test_init(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect.pt1, Point(1, 2))
        self.assertEqual(rect.pt2, Point(3, 4))

    def test_str(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(str(rect), "[(1, 2), (3, 4)]")

    def test_repr(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(repr(rect), "Rectangle((1, 2), (3, 4))")

    def test_eq(self):
        rect1 = Rectangle(1, 2, 3, 4)
        rect2 = Rectangle(1, 2, 3, 4)
        rect3 = Rectangle(4, 5, 6, 7)
        self.assertEqual(rect1, rect2)
        self.assertNotEqual(rect1, rect3)

    def test_center(self):
        rect = Rectangle(1, 2, 5, 6)
        self.assertEqual(rect.center(), "Center = (3.0, 4.0)")

    def test_area(self):
        rect = Rectangle(1, 2, 5, 6)
        self.assertEqual(rect.area(), 16)

    def test_move(self):
        rect = Rectangle(1, 2, 5, 6)
        rect.move(2, 3)
        self.assertEqual(rect.pt1, Point(3, 5))
        self.assertEqual(rect.pt2, Point(7, 9))