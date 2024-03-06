def decorator_func(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper  

@decorator_func
def func():
    print("inner func")


func()

