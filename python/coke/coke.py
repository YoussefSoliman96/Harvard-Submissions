
print("Amount Due: 50")
x = input("Insert Coin: ")

while int(x) < 50:
    y = input("Insert Coin: ")
    due = 50 - int(y)
    print(f"Amount Due: {due}")
    if int(x) >= 50:
        change = int(x) - 50
        print("Change Owed: {change}")
