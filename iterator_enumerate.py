"""
    The built-in function my_enumerate takes an iteratable and returns an iterator over pairs (index, value) for each value in the source.
    >>> list(my_enumerate(["a", "b", "c"])
    [(0, "a"), (1, "b"), (2, "c")]
    >>> for i, c in my_enumerate(["a", "b", "c"]):
    ...     print i, c
    ...
    0 a
    1 b
    2 c
"""


def my_enumerate(a):
    i = 0
    while i < len(a):
        yield (i, a[i])
        i = i + 1


def main():
    b = my_enumerate(["a", "b", "c"])
    for i, c in b:
        print(i, c)


if __name__ == '__main__':
    main()
