"""
    Write a function unique to find all the unique elements of a list.
    >>> unique([1, 2, 1, 3, 2, 5])
    [1, 2, 3, 5]
"""


def my_unique(a, result=[]):
    i = 0
    while i < len(a):
        if a[i] in result:
            i = i + 1
            continue
        else:
            result.append(a[i])
            i = i + 1

    return result           


def main():
    b = list(my_unique([1, 2, 1, 3, 2, 5]))
    print(b)

if __name__ == '__main__':
    main()
