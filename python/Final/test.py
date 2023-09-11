from datetime import datetime


def options(choices):
    print("Please choose:")
    for idx, element in enumerate(choices):
        print("{}) {}".format(idx+1,element))
    i = input("Enter number: ")
    try:
        if 0 < int(i) <= len(options):
            return int(i)
    except:
        pass
    return None