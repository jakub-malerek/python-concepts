def decorator_func(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper  


def func(a,b):
    print("inner func",a,b)


def argument_decorator_func(func):
    def wrapper(*args,**kwargs):
        print("before")
        result = func(*args,**kwargs)
        print("after")
        return result
    return wrapper

func = argument_decorator_func(func)
func(10,20)

import time


def time_threshold(threshold):
    def decorator(func):
        def wrapper():
            start = time.time()
            result = func()
            end = time.time()
            if (end-start) > threshold:
                 print(f"{func.__name__} took {(end-start)} seconds to execute, which exceeds the threshold.")
        return wrapper
    return decorator




    



@time_threshold(threshold=0.5)
def long_running_function():
    # Simulate a time-consuming operation
    time.sleep(1)  # Sleep for 1 second
    print("Function execution completed.")

long_running_function()

