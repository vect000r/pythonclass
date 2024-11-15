import unittest
from rectangles.points import Point
import math

class TestPoints(unittest.TestCase):

    def setUp(self):
        self.zero = Point(0, 0)
        self.p1 = Point(2, 3)
        self.p2 = Point(-1, 4)
        self.p3 = Point(2, 3)  # taki sam jak p1

    def test_str(self):
        self.assertEqual(str(self.p1), "(2, 3)")
        self.assertEqual(str(self.p2), "(-1, 4)")
        self.assertEqual(str(self.zero), "(0, 0)")

    def test_repr(self):
        self.assertEqual(repr(self.p1), "Point(2, 3)")
        self.assertEqual(repr(self.zero), "Point(0, 0)")

    def test_eq(self):
        self.assertEqual(self.p1, self.p3)  # p1 == p3
        self.assertNotEqual(self.p1, self.p2)  # p1 != p2
        self.assertNotEqual(self.p1, self.zero)

    def test_ne(self):
        self.assertNotEqual(self.p1, self.p2)
        self.assertNotEqual(self.zero, self.p1)
        self.assertEqual(self.p1, self.p3)

    def test_add(self):
        self.assertEqual(self.p1 + self.p2, Point(1, 7))
        self.assertEqual(self.p1 + self.zero, self.p1)
        self.assertEqual(self.zero + self.zero, self.zero)

    def test_sub(self):
        self.assertEqual(self.p1 - self.p2, Point(3, -1))
        self.assertEqual(self.p1 - self.zero, self.p1)
        self.assertEqual(self.zero - self.zero, self.zero)

    def test_mul(self):
        # test iloczynu skalarnego
        self.assertEqual(self.p1 * self.p2, -2 + 12)  # 2*(-1) + 3*4 = 10
        self.assertEqual(self.p1 * self.zero, 0)
        self.assertEqual(self.zero * self.zero, 0)

    def test_cross(self):
        # test iloczynu wektorowego
        self.assertEqual(self.p1.cross(self.p2), 11)  # 2*4 - 3*(-1) = 11
        self.assertEqual(self.p1.cross(self.zero), 0)
        self.assertEqual(self.zero.cross(self.zero), 0)

    def test_length(self):
        self.assertEqual(self.zero.length(), 0)
        self.assertEqual(self.p1.length(), math.sqrt(13))  # sqrt(2^2 + 3^2)
        self.assertEqual(self.p2.length(), math.sqrt(17))  # sqrt((-1)^2 + 4^2)

    def test_hash(self):
        # Test czy punkty o tych samych współrzędnych mają ten sam hash
        self.assertEqual(hash(self.p1), hash(self.p3))
        # Test czy różne punkty mają różne hashe
        self.assertNotEqual(hash(self.p1), hash(self.p2))
        
        # Test czy można użyć Point jako klucza w słowniku
        point_dict = {self.p1: "point1", self.p2: "point2"}
        self.assertEqual(point_dict[self.p1], "point1")
        self.assertEqual(point_dict[self.p3], "point1")  # p3 ma te same współrzędne co p1
