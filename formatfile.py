"""
    Write a program that given a text file will create a new text file in which 
    all the lines from the original file are numbered from 1 to n 
    (where n is the number of lines in the file).
"""
#from itertools import map


def format(filename):
    out = open('/home/bsun/test.1.txt', 'w')
    # i = 1
    # normal approach
    # for line in open(filename):
    #     out.write(str(i) + ':' + line)
    #     i += 1

    # pythonic way
    y = map(lambda x: out.write(str(x[0]) + '# ' + x[1]),
            [(index, line) for (index, line) in enumerate(open(filename))])

    [s for s in y]  # have to consume the loop!

    out.close()


def main(filename):
    format(filename)


if __name__ == '__main__':
    main('/home/bsun/test.txt')
