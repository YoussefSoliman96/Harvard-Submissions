def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # All vanity plates must start with at least two letters
    # Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
    if 6 >= len(s) >= 2 or s[0].isalpha() == False or s[1].isalpha == False:
    # Numbers cannot be used in the middle of a plate; they must come at the end


    # No periods, spaces, or punctuation marks are allowed
    for c in s:
        if c in [' ', '.', '!', '?']:
            return False
    return True




main()