"""
    Write a function tree_reverse to reverse elements of a nested-list recursively.
    >>> tree_reverse([[1, 2], [3, [4, 5]], 6])
    [6, [[5, 4], 3], [2, 1]]
"""


def tree_reverse(a, result=None):
    if result is None:
        result = []

    a.reverse()
    for e in a:
        if isinstance(e, list):
            newResult = []
            tree_reverse(e, newResult)
            result.append(newResult)
        else:
            result.append(e)

    return result


def main():
    r = tree_reverse([[1, 2], [3, [4, 5]], 6])
    print(r)


if __name__ == '__main__':
    main()
