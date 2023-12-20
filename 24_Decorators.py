def sample_decorator(func):
    def wrapper():
        print(f"before {func.__name__}")
        func()
        print(f"after {func.__name__}")
    
    return wrapper

def sample_func():
    print("sample function is called")

if __name__ == "__main__":
    sample_func = sample_decorator(sample_func)
    sample_func()