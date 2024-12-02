import unittest
from circles import Circle  
import math

class TestCircle(unittest.TestCase):

    def test_init(self):
        """Test inicjalizacji"""
        c = Circle(1, 2, 3)
        self.assertEqual(c.pt.x, 1)
        self.assertEqual(c.pt.y, 2)
        self.assertEqual(c.r, 3)
        with self.assertRaises(ValueError):
            Circle(0, 0, -1)  # Ujemny promień powinien spowodować błąd

    def test_area(self):
        """Test obliczania pola powierzchni"""
        c = Circle(0, 0, 3)
        self.assertAlmostEqual(c.area(), math.pi * 9, places=5)

    def test_move(self):
        """Test przesuwania okręgu"""
        c = Circle(1, 1, 2)
        c.move(3, 4)
        self.assertEqual(c.pt.x, 4)
        self.assertEqual(c.pt.y, 5)

    def test_equality(self):
        """Test równości i nierówności"""
        c1 = Circle(0, 0, 3)
        c2 = Circle(0, 0, 3)
        c3 = Circle(1, 1, 3)
        self.assertTrue(c1 == c2)
        self.assertFalse(c1 == c3)

    def test_cover_containment(self):
        """Test pokrywania gdy okręgi zawierają się w sobie"""
        c1 = Circle(0, 0, 5)
        c2 = Circle(1, 1, 2)
        result = c1.cover(c2)
        self.assertEqual(result.pt, c1.pt)
        self.assertEqual(result.r, c1.r)

    def test_cover_partial_overlap(self):
        """Test pokrywania gdy okręgi się przecinają"""
        c1 = Circle(0, 0, 3)
        c2 = Circle(4, 0, 2)
        result = c1.cover(c2)
        self.assertAlmostEqual(result.pt.x, 1.6, places=5)
        self.assertAlmostEqual(result.pt.y, 0.0, places=5)
        self.assertAlmostEqual(result.r, 4.5, places=5)

    def test_cover_separate(self):
        """Test pokrywania dla oddzielnych okręgów"""
        c1 = Circle(0, 0, 1)
        c2 = Circle(6, 0, 1)
        result = c1.cover(c2)
        self.assertAlmostEqual(result.pt.x, 3.0, places=5)
        self.assertAlmostEqual(result.pt.y, 0.0, places=5)
        self.assertAlmostEqual(result.r, 4.0, places=5)