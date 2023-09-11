class Client:
        def __init__(self, id, first_name, last_name, email, balance: float) -> None:
            self.id = id
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self._balance: int = balance

        def __str__(self):
            amount = self.balance + "💲"
            return amount

        def deposit(self, cash: float) -> None:
            self._balance = float(self._balance) + float(cash)
            new_balance = self._balance
            print(f"New blanace = {new_balance}")
            client.balance = new_balance


        def withdraw(self, cash: float) -> None:
            if float(cash) > float(self._balance):
                raise ValueError("Unavailable balance")
            else:
                self._balance = float(self._balance) - float(cash)
                new_balance = self._balance
                print(f"New blanace = {new_balance}")
                client.balance = new_balance
        @property
        def size(self):
            return self._balance
client = Client()
client.deposit(100)
client.withdraw(50)