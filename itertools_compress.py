
def compress(a, b):
    """
        simulate compress method in itertools
    """
    p = len(a)
    q = len(b)
    if not p == q:
        raise ValueError('illegal argument')
    else:
        for i in range(0, p):
            if b[i] == 1:
                yield a[i]
            else:
                continue


p = compress('ABCDEF', [1, 0, 1, 0, 1, 1])
print(next(p), end=',  ')
print(next(p), end=',  ')
print(next(p), end=',  ')
print(next(p), end=',  ')
print(next(p), end=',  ')
print(next(p), end='\n')
