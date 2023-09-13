while True:
    try:
        height = int(input("Height: "))
        if height > 0 and height <= 8:
            break
    except ValueError:
        print("Input is not an int")

for i in range(height):
    print(" " * int(height - i - 1) + "#" * int(i + 1) + "  " + "#" * int(i + 1))
