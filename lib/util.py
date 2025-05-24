import math
import time
import numpy as np


def timing(func):

    def timing_wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"function: {func.__name__}, timing: {end_time - start_time:.4f} s")
        return result

    return timing_wrapper


if __name__ == "__main__":
    print(f"  5! = {math.factorial(5)}")

    @timing
    def test_func():
        time.sleep(0.5)

    test_func()
