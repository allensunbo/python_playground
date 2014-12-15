"""
    Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...].
    >>> cumulative_sum([1, 2, 3, 4])
    [1, 3, 6, 10]
"""


def cumulative_sum(a):
    prev = 0
    i = 0
    while i < len(a):
        p = prev + a[i]
        yield p
        i = i + 1
        prev = p


def main():
    b = list(cumulative_sum([1, 2, 3, 4]))
    print(b)

if __name__ == '__main__':
    main()
