def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    x = len(plate)
    print(x)
    letters = plate[0 : int(x/2)]
    numbers = plate[int(x/2) : x]
    print(letters, numbers)



main()