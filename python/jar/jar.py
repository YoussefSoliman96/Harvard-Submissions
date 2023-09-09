class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        if capacity < 0:
            raise ValueError("Invalid Input")

    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...