# 8.4 Декоратор ожидания с таймаутом

import time

def wait_with_retry_until(timeout=10, interval=0.5):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            attempt = 1
            while True:
                result = func(*args, **kwargs)
                if result:
                    print(f"Attempt {attempt}: successful")
                    print("Element found")
                    return result
                else:
                    print(f"Attempt {attempt}:unsuccessful")
                    if time.time() - start_time >= timeout:
                            print("Timeout reached.Element not found.")
                            return False
                    attempt += 1
                    time.sleep(interval)
        return wrapper
    return decorator

@wait_with_retry_until(timeout=3, interval=0.5)
def element_visible():
    return time.time() % 3 > 2

element_visible()


