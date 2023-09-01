def main():
    print("Amount Due: 50")
    # Take user input
    x = input("Insert Coin: ")
    # Calculate change
    change = calculate_change(x)
    print("Change Owed = 0")


def calculate_change(x):
    if int(x) >= 50:
        change = x - 50
        return change
    else:
        due = 50 - int(x)
        print(f"Amount Due: {due}")
        x = input("Insert Coin: ")
    return due




main()