
def dropwhile(predicate, a):
    """
        simulate dropwhile method in itertools
    """
    i = 0
    dropped = False
    while True:
        if predicate(a[i]) and not dropped:
            i += 1
            continue
        else:
            dropped = True
            yield a[i]
            i += 1


p = dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1])
print(next(p), end=',  ')
print(next(p), end=',  ')
print(next(p), end='\n')
