"""
    Write a program to find anagrams in a given list of words. Two words are called anagrams if one word can be formed by rearranging letters of another. 
    For example ‘eat’, ‘ate’ and ‘tea’ are anagrams.
    >>> anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node'])
    [['eat', 'ate', 'tea], ['done', 'node'], ['soup']]
"""


def anagrams(a, result={}):
    for e in a:
        t = [x for x in e]
        t.sort()
        t = ''.join(t)
        if not t in result:
            result[t] = [e]
        else:
            result[t].append(e)
    return [result[k] for k in result]


def main():
    b = anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node'])
    print(b)


if __name__ == '__main__':
    main()
