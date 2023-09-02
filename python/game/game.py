import random
# Loop forever until the user prompts a positive level
while True:
    n = input("Level: ")
    try:
        if int(n) > 0:
            level = int(random.randint(1, int(n)))
            break
    except ValueError:
        print("Input is not a number")

while True:
    try:
        guess = input("Guess: ")
        if int(guess) == level:
            print("Just right!")
            break
        elif int(guess) > level:
            print("Too large!")
        else:
            print("Too small!")

    except ValueError:
        break
print(guess)