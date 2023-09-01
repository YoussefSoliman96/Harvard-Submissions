def main():
    print("Amount Due: 50")
    # Calculate change
    change = calculate_change(x)
    print("Change Owed = 0")


def calculate_change(x):
    x = input("Insert Coin: ")
    if int(x) < 50:
        due = 50 - int(x)
        print(f"Amount Due: {due}")
        calculate_change(x)
    else:





main()