import sys

for arg in sys.argv:
    if str.len(sys.argv) < 2:
        print("Too few command-line arguments")
    elif str.len(sys.argv > 2):
        print("Too many command-line arguments")
    else:
        break