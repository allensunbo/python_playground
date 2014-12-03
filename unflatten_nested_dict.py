
tmp = []

def unflatten_nested_dict(a, result=None):
    """
    Write a function unflatten_dict to do reverse of flatten_dict. for example:
    >>> unflatten_nested_dict({'a': 1, 'b.x': 2, 'b.y.z': 3, 'c': 4})
    {'a': 1, 'b': {'x': 2, 'y': {'z':3}}, 'c': 4}

    """
    if result is None:
        result = {}

        for x in a:
            keys = x.split('.')
            value = a[x]
            r = {}
            i = 0
            for key in reversed(keys):
                if i == 0:
                    r[key] = value
                else:
                    r = {key: r}
                i += 1
            # print(r)   
            tmp.append(r) 
            # result[keys[0]] = r[keys[0]]
    return result

# tricky part is how to merge 'r'
# TODO
def merge(a):
    print(a)

print(unflatten_nested_dict({'a': 1, 'b.x': 2, 'b.y.z': 3, 'c': 4}))

print(tmp)
