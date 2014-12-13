
def izip(a, b):
    """
        simulate izip method in itertools
    """
    p = len(a)
    q = len(b)
    m = p if p < q else q
    i = 0
    while True:
        if i < m:
            yield a[i] + b[i]
            i += 1
        else:
            i += 1
            break


p = izip('ABCD', 'xy')
print(next(p), end=',  ')
print(next(p), end=',  ')
print(next(p), end='\n')
