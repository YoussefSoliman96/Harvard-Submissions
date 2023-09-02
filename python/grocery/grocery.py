# Make an empty dict to store the user's inputs
list = { }
# Loop forever until the user inputs ctrl-d
while True:
    try:
        # Prompt the user for input
        item = input("")
    except EOFError:
        break