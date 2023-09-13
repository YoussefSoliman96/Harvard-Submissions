while True:
    try:
        height = int(input("Height: "))
        break
    except ValueError:
        print("Input is not an int")

for i in range(height):
    print(" " * int(height - i - 1) + "#" * int(i+1)"#" * int(i+1))

for i in range(height):
    print()
