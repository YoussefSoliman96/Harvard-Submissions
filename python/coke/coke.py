due = 50

if due > 0:
    print(f"Amount Due: {due}")
    x = input("Insert Coin: ")
    due -= int(x)

change = abs(due)
print(f"Change Owed: {change}")
