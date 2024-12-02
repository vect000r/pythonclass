import itertools
import random

iter1 = itertools.cycle((0, 1))
iter2 = (random.choice(("N", "E", "S", "W")) for _ in iter(int, 1))
iter3 = itertools.cycle(range(7))

for i in range(10):
    print(next(iter1))

for i in range(10):
    print(next(iter2))

for i in range(7):
    print(next(iter3))