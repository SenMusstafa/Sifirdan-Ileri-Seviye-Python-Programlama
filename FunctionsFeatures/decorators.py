import math
import time

def calculate_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        time.sleep(1)
        func(*args, **kwargs)
        finish = time.time()
        print("Function " + func.__name__ + " took " + str(finish - start) + " seconds")
    return inner

@calculate_time
def exponentiation(a, b):
    print(math.pow(a, b))

@calculate_time
def factorial_function(num):
    print(math.factorial(num))

exponentiation(5, 3)
factorial_function(5)
