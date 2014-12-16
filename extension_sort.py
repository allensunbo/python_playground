"""
    Write a function extsort to sort a list of files based on extension.
    >>> extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
    ['a.c', 'x.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt']
"""


def extension_sort(a):
    return sorted(a, key=lambda s: s.split('.')[-1])


def main():
    p = extension_sort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
    print(p)

if __name__ == '__main__':
    main()
