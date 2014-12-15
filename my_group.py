"""
     Write a function group(list, size) that take a list and splits into smaller lists of given size.
     >>> group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
     [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
     >>> group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
     [[1, 2, 3, 4], [5, 6, 7, 8], [9]]
"""


def my_group(a, n, result=None):
    if result is None:
        result = []
    i = 0
    t = []
    while i < len(a):
        if (i + 1) % n == 0:
            t.append(a[i])
            result.append(t)
            t = []
        else:
            t.append(a[i])

        i = i + 1

        # alignment remaining elements
    if len(t) > 0:
        result.append(t)

    return result


def main():
    b = list(my_group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
    print(b)
    b = list(my_group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
    print(b)

if __name__ == '__main__':
    main()
