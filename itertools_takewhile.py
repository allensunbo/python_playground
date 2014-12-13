
def takewhile(predicate, a):
    """
        simulate takewhile method in itertools
    """
    i = 0
    terminated = False
    while True:
        if predicate(a[i]) and not terminated:
            yield a[i]
            i += 1
        else:
            raise StopIteration('No more elements')


p = takewhile(lambda x: x < 5, [1, 4, 6, 4, 1])
print(next(p), end=',  ')
print(next(p), end=',  ')
print(next(p), end='\n')
