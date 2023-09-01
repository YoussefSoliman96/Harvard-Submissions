import random

def main():
    level = get_level()
    score = count_score(level)
    print("Score: ", score)


def get_level():
    # Loop forever until user inputs a valid level (1 -> 3)
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                break
        except:
            pass
    return level


def generate_integer(level):
        # Determine the number of digits in comparison depending on the level
        if level == 1:
            x = random.randint(0,9)
            y = random.randint(0,9)
        elif level == 2:
            x = random.randint(10,99)
            y = random.randint(10,99)
        else:
            x = random.randint(100,999)
            y = random.randint(100,999)
        return x,y

def round(x, y):
    # Each round, compare user's answer to the actual result and give the user 3 tries
    count = 1
    result = x + y
    while count <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            # Break out of the loop if user's answer is right
            if answer == result:
                return True
            else:
                # Print "EEE" if answer is wrong and consume 1 of 3 tries
                print("EEE")
                count += 1
        except ValueError:
            # Print "EEE" if user inputs an answer that is not a positive integer
            count += 1
            print("EEE")
    print(f"{x} + {y} = {result}")
    return False

def count_score(level):
    # Calculate the score and return it only when all the 10 rounds are over
    count2 = 1
    score = 0
    while count2 <= 10:
        x, y = generate_integer(level)
        if round(x, y) == True:
            score += 1
        count2 += 1
    return score



if __name__ == "__main__":
    main()
