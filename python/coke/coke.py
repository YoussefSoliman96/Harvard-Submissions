due = 50

while due > 0:
    print(f"Amount Due: {due}")
    x = input("Insert Coin: ")
    due = due - x
    x = input("Insert Coin: ")
else:
    change = int(x) - due
    print("Change Owed: {change}")
