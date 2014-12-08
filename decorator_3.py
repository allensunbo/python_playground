
def around(f):
    def wrapper(*args, **kwargs):
        print('before')
        value = f(*args, **kwargs)
        print('after')
        return value

    return wrapper


@around
def foo():
    print('inside foo')
    return 100

print(foo())
