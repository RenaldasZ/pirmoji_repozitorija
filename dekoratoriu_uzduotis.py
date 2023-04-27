import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} took {end - start} seconds to execute')
        return result
    return wrapper

@time_it
def my_function(x):
    # do some stuff here
    x = 5
    x * 2
    return x

print()