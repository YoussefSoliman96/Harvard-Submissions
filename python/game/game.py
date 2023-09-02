import random
# Loop forever until the user prompts a positive level
while True:
    n = input("Level: ")
    try:
        if int(n) > 0:
            level = random.randint(1, int(n))
            break
    except ValueError:
        print("Input is not a number")
        break

print(level)

