# 8.1 Декоратор повторного запуска теста

import time

def retry(times=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                result = func(*args, **kwargs)
                if result == "PASSED":
                    return result
                else:
                    print(f"Unsuccessful! Attempt number: {attempt}")
            print("No more attempts left")
            return "FAILURE"
        return wrapper
    return decorator


@retry(times=2)
def flaky_test():
    if time.time() % 2 < 1:
        return "FAILURE"
    return "PASSED"


print(flaky_test())