def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    x = len(plate)
    letters = plate[0 : int(x/2)]
    numbers = plate[int(x/2) : x]
    if len(letters) >= 2 and x <=6 and letters.isaplha() == True:
        return True
    else:
        return False



main()