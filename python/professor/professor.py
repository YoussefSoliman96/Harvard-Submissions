import random
while True:
        n = int(input("Level: "))
        try:
            if n >= 1 and n < 4:
                x = random.randint(1, 10)
                y = random.randint(1,10)
                result = x + y
                print(f"{x} + {y} = ",end=" ")
                break
        except ValueError:
            print("Input is not an integer ")
print(n)


while True:
    answer = int(input(""))
        try:
            if answer == result:
                 break
            elif answer != result:
                 print("EEE")
                 
        except ValueError:
                print("Input should be a positive integer")