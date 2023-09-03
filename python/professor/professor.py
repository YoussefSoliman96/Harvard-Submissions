import random
n = int(input("Level: "))
while True:
        x = random.randint(1, 10)
        y = random.randint(1,10)
        result = x + y
        print(f"{x} + {y} = ",end=" ")
        try:
            if n >= 1 and n < 4:
                while True:
                    answer = int(input(""))
                    if answer == result:
                        break
                    elif answer != result:
                        print("EEE")
        except ValueError:
            print("Input is not an integer ")