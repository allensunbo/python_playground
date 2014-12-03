def flatten_nested_dict(a, result=None):
    """
            flatten a nested dict, for example:
            >>> flatten_nested_dict({'a': 1, 'b': {'x': 2, 'y': {'z':3}}, 'c': 4})
            {'a': 1, 'b.x': 2, 'b.y.z': 3, 'c': 4}
    """
    if result is None:
        result = {}

    for x in a:
        if isinstance(a[x], dict):
            new_dict = {}
            for y in a[x]:
                new_dict[x + '.' + y] = a[x][y]
            flatten_nested_dict(new_dict, result)
        else:
            result[x] = a[x]
    return result


print(flatten_nested_dict({'a': 1, 'b': {'x': 2, 'y': {'z': 3}, 'p':{'q':2, 'r':{'s':3}}}, 'c': 4}))

