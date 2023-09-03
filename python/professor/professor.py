import random
def main():
    level = get_level()
    get_level()
    equation()


def get_level():
    while True:
        n = int(input("Level: "))
        try:
            if n == 1 or n == 2 or n == 3:
                break
        except:
            pass
    return n


def generate_integer(level):
    i = 0
    while i < 10:
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

def equation(x, y):
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

if __name__ == "__main__":
    main()
