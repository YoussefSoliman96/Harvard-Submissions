import random
# Loop forever until the user prompts a valid level
while True:
    n = input("Level: ")
    try:
        if int(n) > 0:
            # Generate a random number and assign it to level
            level = int(random.randint(1, int(n)))
            break
    except ValueError:
        print("Level is not a number")

# Loop forever until the user prompts a valid guess that's equal to the generated level
while True:
    guess = input("Guess: ")
    try:
        if int(guess) > 0:
            if int(guess) == level:
                print("Just right!")
                break
            elif int(guess) > level:
                print("Too large!")
            else:
                print("Too small!")

    except ValueError:
        print("Guess is not a number")

