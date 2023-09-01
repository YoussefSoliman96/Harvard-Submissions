def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 and x > 6 or s[0].isalpha() == False or s[1].isalpha == False:
        return False
    for i in range(len(s)):
        if s[i].isalpha() == Flase:
            if s[i] == "0":
                return False



main()