def product(a, b):
    """
            Implement a function product to multiply 2 numbers recursively using + and - operators only.
    """
    if b == 1:
        return a
    else:
        return a + product(a, b - 1)

print(product(2, 3))


def product3(a, b, c):
    """
            Implement a function product to multiply 3 numbers recursively using + and - operators only (with the help of product).
    """
    if c == 1:
        return product(a, b)
    else:
        return product(a, b) + product3(a, b, c - 1)

print(product3(2, 3, 4))
