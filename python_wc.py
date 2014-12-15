"""
    implement something like word count in linux
"""


def wc(filename):
    for line in open(filename):
        words = line.split()
        print(words)


def main(filename):
    wc(filename)


if __name__ == '__main__':
    main('/home/bsun/test.txt')
