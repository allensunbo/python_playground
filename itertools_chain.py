
def chain(*args):
    """
        simulate chain method in itertools
    """
    for arg in args:
        for a in arg:
            yield a

p = chain('abc', 'def')
print(next(p), end=',  ')
print(next(p), end=',  ')
print(next(p), end=',  ')
print(next(p), end=',  ')
print(next(p), end=',  ')
print(next(p), end='\n')
