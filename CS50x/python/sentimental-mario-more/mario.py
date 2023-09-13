while True:
    try:
        height = int(input("Height: "))
        break
    except ValueError:
        print("Input is not an int")

for i in range(height):
    print("#" * int(i+1))

for i in range(height):
    print("#" * int(i+1))