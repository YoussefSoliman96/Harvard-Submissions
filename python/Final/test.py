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

        client = Client(id, first, last, email, balance)

        if client_choice == "Deposit":
            client.deposit(cash)

        if client_choice == "Withdraw":
            client.withdraw(cash)

        update_balance(int(client.id), client._balance)