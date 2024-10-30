import time
import functools

# Dekorator mierzący czas wykonania innych funkcji 
# Używam go między innymi w zadaniu 4.5 w celu porównania czasów wykonania podejścia iteracyjnego i rekurencyjnego


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        
        execution_time = end_time - start_time
        print(f"{func.__name__} took {execution_time:.6f} seconds to execute")
        
        return result
    return wrapper