def cycle(a):
    """
        simulate cycle method in itertools
    """
    max = len(a)
    i = 0
    while True:
        if i < max:
            yield a[i]
            i = i + 1
        else:
            # yield a[0]
            i = 0

p = cycle('tes')
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
