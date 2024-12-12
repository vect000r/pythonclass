import tkinter as tk
import random

class NumberGenerator:
    def __init__(self, num=5):
        self.opt1, self.opt2, self.opt3 = random.sample(range(self.num), 3)
    def result(self):
        pass
