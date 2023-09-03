import random
while True:
        n = int(input("Level: "))
        try:
            if n >= 1 and n < 4:
                x = random.randint(1, 10)
                y = random.randint(1,10)
                result = x + y
                print(f"{x} + {y} = ",end=" ")
                answer = int(input(""))
                if answer == result:
                     break
                try:

                except ValueError:
                     print("Input should be a positive integer")
                     break
        except ValueError:
            print("Input is not an integer ")
print(n)