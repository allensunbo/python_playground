"""
    izip – iterable version of zip
"""


def izip(a, b):
    ita = iter(a)
    itb = iter(b)
    exit = False
    while not exit:
        try:
            itema = next(ita)
            itemb = next(itb)
            yield (itema, itemb)
        except:
            break


def main():
    for x, y in izip(["a", "b", "c"], [1, 2, 3, 4]):
        print(x, y)


if __name__ == '__main__':
    main()
