import sys
def main():
    argument_check()
    output = []




def argument_check():
    extensions = [".jpg", ".jpeg", "png"]
    # Check if the command line arguments are 2
    if (len(sys.argv) < 3):
        sys.exit("Too few command-line arguments")
    elif (len(sys.argv) > 3):
        sys.exit("Too many command-line arguments")
    elif ".jpg" or "jpeg" or ".png" not in sys.argv[1]:
        sys.exit("Input not a photo")
    elif ".jpg" or "jpeg" or ".png" not in sys.argv[2]:
        sys.exit("Output not a photo")








if __name__ == "__main__":
    main()