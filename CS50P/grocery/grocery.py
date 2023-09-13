# Make an empty dict to store the user's inputs
list = {}
# Loop forever until the user inputs ctrl-d
while True:
    try:
        # Prompt the user for input and lowercase it
        item = input("").lower()
        # If the item is already in the list, increase item count
        if item in list:
            list[item] += 1
        # If item is not in the list make it 1
        else:
            list[item] = 1
    except EOFError:
        # Print items in order
        for key in sorted(list):
            # Output the keys in uppercase and their values
            print(list[key], key.upper())
        break

