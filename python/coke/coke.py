due = 50
print("Amount Due: 50")
x = input("Insert Coin: ")


if int(x) < due:
    x = due - int(x)
    due = due - x
    print(f"Amount Due: {due}")
    x = input("Insert Coin: ")
else:
    change = int(x) - due
    print("Change Owed: {change}")
