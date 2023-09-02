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
while True:
    try:
        item = input("Item: ")
        if item in menu:
            print(f"Total: {menu[item]}")
    except EOFError:
        print("")