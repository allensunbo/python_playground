import types


def count(a):
    """
        simulate count method in itertools
    """
    if not isinstance(a, (int, float, complex)):
        raise TypeError('a number is required')

    while True:
        yield a
        a += 1    


p = count(10)
print(next(p), end=',  ')
print(next(p), end=',  ')
print(next(p), end=',  ')
print(next(p), end=',  ')
print(next(p), end=',  ')
print(next(p), end=',  ')
print(next(p), end=',  ')
print(next(p), end=',  ')
print(next(p), end=',  ')
print(next(p), end=',  ')
print(next(p), end=',  ')
print(next(p), end=',  ')
print(next(p), end=',  ')
print(next(p), end=',  ')
print(next(p), end='\n')
