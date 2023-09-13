import random
n = int(input("Level: "))
count = 0
wrong_count = 0
while count < 3:
        x = random.randint(1, 10)
        y = random.randint(1,10)
        result = x + y
        print(f"{x} + {y} = ",end=" ")
        try:
            if n >= 1 and n < 4:
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
