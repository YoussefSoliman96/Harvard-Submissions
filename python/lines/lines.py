import sys
def main():
    argument_check()

    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()
        print(lines)
    except FileNotFoundError:
        sys.exit("File does not exit")

def argument_check():
for arg in sys.argv:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif ".py" not in sys.argv[1]:
        sys.exit("Not a python file")



if __name__ == "__main__"
    main()