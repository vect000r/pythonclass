def fibonacci(n:int) -> int:
    a = 0
    b = 1
    for i in range(n):
        print(str(b) + " ")
        b += a
        a = b - a

fibonacci(10)