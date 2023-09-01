due = 50
print("Amount Due: 50")
x = input("Insert Coin: ")

while int(x) < due:
    x = due - int(x)
    due = due - x
    print(f"Amount Due: {due}")
    y = input("Insert Coin: ")
    if int(x) >= 50:
        change = int(x) - 50
        print("Change Owed: {change}")
