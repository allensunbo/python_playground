def readFiles(filenames):
    for file in filenames:
        for line in open(file):
            yield line


def filter(lines, line_max=40):
    return [line for line in lines if len(line) < line_max]


def printLines(lines):
    for line in lines:
        print(line)


def main(filenames, *line_max):
    lines = readFiles(filenames)
    lines = filter(lines, line_max[0]) if len(line_max) == 1 else filter(lines)
    printLines(lines)

if __name__ == '__main__':
    print('---use default value---')
    main(['c:\passwords.txt'])
    print('---use specified value---')
    main(['c:\passwords.txt'], 23)
