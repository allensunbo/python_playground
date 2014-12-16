"""
	Provide an implementation for zip function using list comprehensions.
	>>> zip([1, 2, 3], ["a", "b", "c"])
	[(1, "a"), (2, "b"), (3, "c")]
"""


def my_zip(a, b):
	return [(a[x],b[x]) for x in range(len(a))]

def main():
    b = my_zip([1, 2, 3], ["a", "b", "c"])
    print(b)


if __name__ == '__main__':
    main()
