class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0
        if capacity < 0:
            raise ValueError("Invalid Input")

    def __str__(self):
        amount = self.size * "🍪"
        return amount

    def deposit(self, n):
        if n < capacity:
            self.size -= n
        else:
            raise ValueError("Amount requested is unavailable")

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...