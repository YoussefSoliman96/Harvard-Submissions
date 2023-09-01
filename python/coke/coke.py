
print("Amount Due: 50")
x = input("Insert Coin: ")
y = calculate_change(x)

while int(x) < 50:
    due = 50 - int(x)
    print(f"Amount Due: {due}")
else:
    change = int(x) - 50
    print("Change Owed: {change}")
    return change
