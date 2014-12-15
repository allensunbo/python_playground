"""
 	Write a function lensort to sort a list of strings based on length.
 	>>> lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
	['c', 'perl', 'java', 'ruby', 'python', 'haskell']
"""


def lensort(a):
    return sorted(a, key=lambda x: len(x))


def main():
    b = lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
    print(b)

if __name__ == '__main__':
    main()
