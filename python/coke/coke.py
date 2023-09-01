due = 50

while due > 0:
    print("Amount Due:", due)
    x = int(input("Insert Coin:"))
    if x == 5 or x == 10 or x == 25:
        due = due - x
        if due <= 0:
            change = abs(due)
            print(f"Change Owed: {change}")
            break


