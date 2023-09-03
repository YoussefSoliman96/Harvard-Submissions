import random
def main():
    level = get_level()
    score = count_score(level)
    print("Score: ", score)


def get_level():
    # Loop forever until user inputs a valid level (1 -> 3)
    while True:
        n = int(input("Level: "))
        try:
            if n == 1 or n == 2 or n == 3:
                break
        except:
            pass
    return n


def generate_integer(level):
        # Determine the number of digits in comparison depending on the level
        if level == 1:
            x = random.randint(1, 9)
            y = random.randint(1, 9)
        elif level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        else:
            x = random.randint(100, 999)
            y = random.randint(100, 999)
        return x,y

def round(x, y):
    # Each round, compare user's answer to the actual result
    count = 1
    result = x + y
    while count <= 3:
        try:
            answer = int(input(f"{x} + {y} ="))
            if answer == result:
                return True
            else:
                print("EEE")
                count += 1
        except:
            count += 1
            print("EEE")
    print(f"x + y = {result}")
    return False

def count_score(n):
    count2 = 1
    score = 0
    while count2 <= 10:
        x, y = generate_integer(n)
        if round(x, y) == True:
            score += 1
        count2 += 1
    return score



if __name__ == "__main__":
    main()
