import sys

def main():
    argument_check()




def argument_check():
    # Check if the command line arguments are 2
    if (len(sys.argv) < 3):
        sys.exit("Too few command-line arguments")
    elif (len(sys.argv) > 3):
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")








if __name__ == "__main__"
    main()