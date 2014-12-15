"""
    chain – chains multiple iterators together.
"""


def chain(*args):
    for it in args:
        while True:
            try:
                item = next(it)
                yield item
            except StopIteration as e:
                print(e)
                break


def main():
    it1 = iter([1, 2, 3])
    it2 = iter([4, 5, 6])
    p = chain(it1, it2)
    for s in p:
        print(s)


if __name__ == '__main__':
    main()
