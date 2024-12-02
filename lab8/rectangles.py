from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]"

    def __repr__(self):
        return f"Rectangle(({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y}))"

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):
        return not self == other

    @classmethod
    def from_points(cls, points):
        """Tworzy prostokąt z dwóch punktów."""
        pt1, pt2 = points
        return cls(pt1.x, pt1.y, pt2.x, pt2.y)

    @property
    def center(self):
        """Zwraca środek prostokąta."""
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    @property
    def area(self):
        """Pole powierzchni prostokąta."""
        return abs(self.pt2.x - self.pt1.x) * abs(self.pt2.y - self.pt1.y)

    @property
    def width(self):
        """Szerokość prostokąta."""
        return abs(self.pt2.x - self.pt1.x)

    @property
    def height(self):
        """Wysokość prostokąta."""
        return abs(self.pt2.y - self.pt1.y)

    @property
    def top(self):
        return max(self.pt1.y, self.pt2.y)

    @property
    def bottom(self):
        return min(self.pt1.y, self.pt2.y)

    @property
    def left(self):
        return min(self.pt1.x, self.pt2.x)

    @property
    def right(self):
        return max(self.pt1.x, self.pt2.x)

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)

    def move(self, x, y):
        """Przesunięcie prostokąta o (x, y)."""
        self.pt1.x += x
        self.pt2.x += x
        self.pt1.y += y
        self.pt2.y += y
