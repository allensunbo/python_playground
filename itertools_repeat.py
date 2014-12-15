
def repeat(a, n):
    """
        simulate repeat method in itertools
    """
    i = 0
    while True:
        if i < n:
            yield a
            i += 1
        else:
            break
            # raise StopIteration

p = repeat(10, 3)
print(next(p), end=',  ')
print(next(p), end=',  ')
print(next(p), end=',  ')
print(next(p), end='\n')
