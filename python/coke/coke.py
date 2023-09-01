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
        due = 50 - x
        print(f"Amount Due: {due}")
    return change




main()