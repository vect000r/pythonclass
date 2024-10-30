import performance_decorator

@performance_decorator.timer
def odwracanie_iter(L: list, left: int, right: int):
    while (left < right):
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

@performance_decorator.timer
def odwracanie_rek(L: list, left: int, right: int):
    if left < right:
        L[left], L[right] = L[right], L[left]
        odwracanie_rek(L, left + 1, right - 1)



L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
L2 = [10, 11, 12, 13, 14, 15, 16, 17, 18]


odwracanie_iter(L1, 2, 6)
print(L1)
odwracanie_rek(L2, 2, 6)
print(L2)