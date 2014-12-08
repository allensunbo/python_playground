def currency(currencySymbol):
    def currency_wrapper(f):
        def wrapper(*args, **kwargs):
            return currencySymbol + str(f(*args, **kwargs))
        return wrapper
    return currency_wrapper


class Product():

    def __init__(self, price):
        self.price = price

    @currency('$')
    def price_with_tax(self, tax_rate_percentage):
        """Return the price with *tax_rate_percentage* applied.
        *tax_rate_percentage* is the tax rate expressed as a float, like
        "7.0" for a 7% tax rate."""
        return self.price * (1 + (tax_rate_percentage * .01))


print(Product(50).price_with_tax(7.0))


class Play(object):

    """docstring for Play"""
    status = 'open'
    foo = lambda self: print('Hi!')

    def __init__(self, arg):
        super().__init__()
        self.arg = arg

    play = lambda self: print('play')

    def play2(self):
        print(Play.status)

Play('').foo()
Play('').play2()


def bar(a=None):
    if a == None:
        a = []
    a.append('bar')
    return a


print(bar())
print(bar())
print(bar())

try:
    l = [1, 2]
    a = l[2]
except (ValueError, IndexError) as e:
    print(e)


a = [10]

def test():
    a.append(10)

test()

print(a)