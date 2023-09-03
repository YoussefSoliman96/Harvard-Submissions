import random
while True:
        n = int(input("Level: "))
        try:
            if n >= 1 and n < 4:
                x = random.randint(1, 10)
                y = random.randint(1,10)
                result = x + y
                print(x, y, result)
                break
        except ValueError:
            print("Input is not an integer ")
print(n)