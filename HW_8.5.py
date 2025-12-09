# 8.5 Декоратор кэширования результатов

import time

def cache_results(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key in cache:
            return cache[key]
        else:
            result = func(*args, **kwargs)
            cache[key] = result
            return result
    return wrapper


@cache_results
def expensive_calculation(n):
    print(f"Calculate for {n}")
    time.sleep(1)
    return n * n

print(expensive_calculation(5))
print(expensive_calculation(5))
print(expensive_calculation(5))
print(expensive_calculation(6))
print(expensive_calculation(5))