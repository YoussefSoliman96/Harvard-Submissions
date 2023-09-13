

while True:
    try:
        card_number = int(input("Number: "))
    except ValueError:
        print("Invalid input")
