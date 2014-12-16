"""
 	 Write a function invertdict to interchange keys and values in a dictionary. For simplicity, assume that all values are unique.
	 >>> invert_dict({'x': 1, 'y': 2, 'z': 3})
	 {1: 'x', 2: 'y', 3: 'z'}
"""


def invert_dict(a):
    return {a[k]:k for k in a}


def main():
    b = invert_dict({'x': 1, 'y': 2, 'z': 3})
    print(b)

if __name__ == '__main__':
    main()
