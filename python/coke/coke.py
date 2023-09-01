def main():
    print("Amount Due: 50")
    # Take user input
    x = input("Insert Coin: ")
    # Calculate change
    change = calculate_change(x)
    print("Change Owed = 0")


def calculate_change(change):
    if x >= 50:
        change = x - 50
    else:
        x = input("Insert Coin: ")
    return change




main()