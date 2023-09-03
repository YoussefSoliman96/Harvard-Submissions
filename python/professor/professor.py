import random

def main():
    get_level()
    count = 0
    wrong_count = 0
    while count < 10:
            x = random.randint(1, 10)
            y = random.randint(1,10)
            result = x + y
            print(f"{x} + {y} = ",end=" ")
            try:
                while True:
                    answer = int(input(""))
                    if answer == result or wrong_count == 2:
                        break
                    elif answer != result:
                        print("EEE")
                        print(f"{x} + {y} = ",end=" ")
                        wrong_count += 1
                count += 1
            except ValueError:
                print("Input is not an integer ")


def get_level():
    while True:
            n = input("Level: ")
            try:
                if int(n) > 0:
                    break
            except ValueError:
                print("Input is not an integer ")
                pass

def generate_integer(n):
    digits = n
    x = random.randint(1, d)
    y = random.randint(1, d)


if __name__ == "__main__":
    main()