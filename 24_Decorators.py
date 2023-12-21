from datetime import datetime
from functools import wraps

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

def sample_func():
    print("sample function is called")

@sample_decorator
def shorten_decor():
    print("sample function is called")

@do_twice
@decor_silent_night
def say_out_loud():
    print("Say out loud!!!")

@do_twice
def say_my_name(name:str):
    print(name)

if __name__ == "__main__":
    sample_func = sample_decorator(sample_func)
    sample_func()
    shorten_decor()
    say_out_loud()
    say_my_name("Vu")
    
    print(say_my_name.__name__)