"""
     Improve the unique function written in previous problems to take an optional key function as argument and use the return value of the key function to check for uniqueness.
     >>> unique(["python", "java", "Python", "Java"], key=lambda s: s.lower())
     ["python", "java"]
"""


def my_unique2(a, result=[], **kwargs):
    f = kwargs['key']
    for e in a:
        tmp = [f(r) for r in result]

        if not f(e) in tmp:
            result.append(e)

    return result


def main():
    p = my_unique2(
        ["python", "java", "Python", "Java"], key=lambda s: s.lower())
    print(p)

if __name__ == '__main__':
    main()
