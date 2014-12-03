def treemap(f, a, result=None):
    """
    Write a function treemap to map a function over nested list. for example:
        >>> treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
            [1, 4, [9, 16, [25]]]
    """
    if result is None:
        result = []

    for x in a:
        r = []
        if isinstance(x, list):
            treemap(f, x, r)
        else:
            r = f(x)
        result.append(r)    
    return result

print(treemap(lambda x: x * x, [1, 2, [3, 4, [5]]]))
