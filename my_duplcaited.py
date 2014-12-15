"""
 	Write a function dups to find all duplicates in the list.
 	>>> dups([1, 2, 1, 3, 2, 5])
	[1, 2]
"""


def my_duplicate(a, tmp=[], result=[]):
    i = 0
    while i < len(a):
        if a[i] in tmp:
            if not a[i] in result:
                result.append(a[i])
            i = i + 1
        else:
            tmp.append(a[i])
            i = i + 1

    return result


def main():
    b = list(my_duplicate([1, 2, 1, 3, 2, 5]))
    print(b)

if __name__ == '__main__':
    main()
