def announce(func):
    def wrapper():
        print("Function started")
        result = func()
        print("Function finished")
        return result
    return wrapper

@announce
def greet():
    print("Hello, programmer!")

greet()
