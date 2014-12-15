
def ifilter(predicate, a):
    """
        simulate ifilter method in itertools
    """
    i = 0
    while True:
        if predicate(a[i]):
            yield a[i]
            i += 1
        else:
            i += 1


p = ifilter(lambda x: x % 2 == 0, range(10))
print(next(p), end=',  ')
print(next(p), end=',  ')
print(next(p), end=',  ')
print(next(p), end=',  ')
print(next(p), end='\n')
