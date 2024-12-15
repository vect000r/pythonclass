import random

class NumberGenerator:
    def __init__(self, num=5):
        self.num = num

    def result(self):
        """Zwraca 3 losowe liczby z przedziału od 1 do 5"""
        return [random.randint(1, self.num) for _ in range(3)]
