import timeit

PRECISION = 100

def average(arr):
    return sum(arr) / len(arr)

def timeThis(func):
    def wrapper(*args, **kwargs):
        start = timeit.default_timer()

        for _ in range(PRECISION):
            value =func(*args, **kwargs)
            
        total_time = (timeit.default_timer() - start) / PRECISION

        print(f'[+] Function {func.__name__} executed in { total_time }')
        return value, total_time, func.__name__

    return wrapper
    