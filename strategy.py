class Context:

    """

    """

    def __init__(self, strategy):
        self.strategy = strategy

    def execute_strategy(self):
        self.strategy.execute()


class Strategy:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self, a, b):
        raise NotImplementedError('should implement this')


class AddStrategy(Strategy):

    def __init__(self, a, b):
        super().__init__(a, b)

    def execute(self):
        print(self.a + self.b)


class MinusStrategy(Strategy):

    def __init__(self, a, b):
        super().__init__(a, b)

    def execute(self):
        print(self.a - self.b)


c = Context(AddStrategy(10, 5))
c.execute_strategy()

c = Context(MinusStrategy(10, 5))
c.execute_strategy()
