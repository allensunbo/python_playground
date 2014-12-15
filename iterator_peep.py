"""
     Write a function peep, that takes an iterator as argument and returns the first element and an equivalant iterator.
"""


def peep(it):
    yield next(it)
    yield it


def main():
    it = iter(range(5))
    x, it1 = peep(it)
    print(x, ', ', [x for x in it1])


if __name__ == '__main__':
    main()
