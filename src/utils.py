# utils for gitdemo

def benchmark(func):
    ''' Standard benchmarking decorator. '''

    from time import clock

    def wrapper(*args, **kwargs):
        t = clock()
        res = func(*args, **kwargs)
        print("Method name: ", func.__name__, "time to execute: ", clock()-t, "s")
        return res

    return wrapper
