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
