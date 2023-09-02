menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Loop forever until the user inputs ctrl-d
price = 0
while True:
    try:
        item = input("Item: ").title()
        if item in menu:
            # Increase the price each time the user inputs and item
            price += menu[item]
            print("Total: ${:.2f}".format(price))
    except EOFError:
            print("")
            break