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
        if n > self.capacity:
            raise ValueError("Amount requested is too big")
        elif (n + self.size) > self.capacity:
            raise ValueError("Amount requested is too big")
        else:
            self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Amount requested is unavailable")
        else:
            self.size -= n

"""
    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...
"""

jar = Jar()
jar.deposit(5)
jar.withdraw(2)
print(jar)