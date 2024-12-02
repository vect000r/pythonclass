from points import Point
import math

class Circle:
    """Klasa reprezentująca okrąg na płaszczyźnie"""
    def __init__(self, x, y, r):
        if r < 0:
            raise ValueError("promień nie może byc ujemny")
        
        self.pt = Point(x, y)
        self.r = r

    def __repr__(self):
        return f"Circle({self.x}, {self.y}, {self.r})"
    
    def __eq__(self, other):
        return self.r == other.r and self.pt == other.pt
    
    def __ne__(self, other):
        return not self == other

    def area(self):
        return math.pi * (self.r ** 2)
    
    def move(self, x, y):
        self.pt.x += x
        self.pt.y += y

    def cover(self, other):
        d = math.sqrt((self.pt.x - other.pt.x) ** 2 + (self.pt.y - other.pt.y) ** 2)

        # Przypadek 1: jeden okrąg zawiera się w drugim
        if d <= abs(self.r - other.r):
            if self.r > other.r:
                return Circle(self.pt.x, self.pt.y, self.r)
            else:
                return Circle(other.pt.x, other.pt.y, other.r)

        # Przypadek 2: okręgi częściowo się pokrywają lub są rozdzielne
        else:
            # Obliczamy środek okręgu pokrywającego
            weight_self = self.r / (self.r + other.r)
            weight_other = other.r / (self.r + other.r)
            center_x = weight_self * self.pt.x + weight_other * other.pt.x
            center_y = weight_self * self.pt.y + weight_other * other.pt.y

            # Obliczamy promień okręgu pokrywającego
            new_radius = (d + self.r + other.r) / 2

            return Circle(center_x, center_y, new_radius)
