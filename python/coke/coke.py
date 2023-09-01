due = 50

while due > 0:
    print(f"Amount Due: {due}")
    x = input("Insert Coin: ")
    if x in [5, 10, 25]:
        due -= int(x)

else:
    change = abs(due)
    print(f"Change Owed: {change}")
