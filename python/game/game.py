import random
# Loop forever until the user prompts a positive level
while True:
    n = input("Level: ")
    try:
        if int(n) > 0:
            level = random.randint(1, int(n))
            guess = input("Guess: ")
            if int(guess) < int(level):
                print("Too small!")
            elif int(guess) > int(level):
                print("Too large!")
            else:
                print("Just right!")
            break
    except ValueError:
        print("Input is not a number")


print(level)

