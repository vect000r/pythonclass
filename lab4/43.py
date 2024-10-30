def factorial(n:int) -> int:
    fact = 1
    for i in range(1,n + 1):
        fact = fact*i
    return fact

assert factorial(5) == 120