def memoize(function):
    cache = {}

    def wrapper(number):
        if number not in cache:
            cache[number] = function(number)
        return cache[number]

    return wrapper


@memoize
def square(number):
    print("Calculating...")
    return number * number


print(square(5))
print(square(5))
