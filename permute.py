"""
    Write a function permute to compute all possible permutations of elements of a given list.
    >>> permute([1, 2, 3])
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
"""


def permute(a, result=None):
    if result is None:
        result = []

    if len(a) == 1:
        return [a[0]]

    for p in range(len(a)):
        prev = a[0:p]
        after = a[p + 1:]
        other = prev + after
        r = permute(other)
        for s in r:
            q = []
            q.append(a[p])
            if isinstance(s, int):
                q.append(s)
            else:
                for t in s:
                    q.append(t)
            result.append(q)

    return result


def main():
    r = permute([1, 2, 3, 4])
    print('total permutations = ', len(r))
    print(r)


if __name__ == '__main__':
    main()
