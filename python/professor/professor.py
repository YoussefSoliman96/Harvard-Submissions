
while True:
        n = input("Level: ")
        try:
            if n >= 1 and n < 4:
                break
        except ValueError:
            print("Input is not an integer ")
print(n)