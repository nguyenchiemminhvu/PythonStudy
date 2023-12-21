from datetime import datetime
import time
from functools import wraps
import random

def sample_decorator(func):
    def wrapper():
        print(f"before {func.__name__}")
        func()
        print(f"after {func.__name__}")
    
    return wrapper

def decor_silent_night(func):
    def wrapper():
        if (datetime.now().hour < 7 and datetime.now().hour < 22):
            print("Keep silent during the night")
        else:
            print("Do it in day time")
            func()
    return wrapper

def do_twice(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

def do_times(num_times = 1):
    def do_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(0, num_times):
                func(*args, **kwargs)
        return wrapper
    return do_repeat

def round_float(func):
    @wraps(func)
    def wrapper():
        value = func()
        print("original value:", value)
        return round(value)
    return wrapper

def check_performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print("{} finished in {} seconds".format(func.__name__, end - start))
    return wrapper

def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print("Call {} {} times".format(func.__name__, wrapper.count))
        func(*args, **kwargs)
    wrapper.count = 0
    return wrapper

def sample_func():
    print("sample function is called")

@sample_decorator
def shorten_decor():
    print("sample function is called")

@do_twice
@decor_silent_night
def say_out_loud():
    print("Say out loud!!!")

@do_times(3)
def say_my_name(name:str):
    print(name)

@round_float
def get_random_value():
    return random.random()

@check_performance
def an_algorithm():
    for i in range(0, 1000000):
        pass

@count_calls
def call_multiple_times():
    print(call_multiple_times.__name__)

if __name__ == "__main__":
    sample_func = sample_decorator(sample_func)
    sample_func()
    shorten_decor()
    say_out_loud()
    say_my_name("Vu")
    print(say_my_name.__name__)
    print(get_random_value())
    an_algorithm()
    for _ in range(0, 3):
        call_multiple_times()