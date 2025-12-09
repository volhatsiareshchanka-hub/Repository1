# 8.3	Декоратор замера времени выполнения

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"{func.__name__} finished in {duration:.2f} sec.")
        return result
    return wrapper


@timer
def slow_test():
    time.sleep(1)
    return "OK"

print(slow_test())

















