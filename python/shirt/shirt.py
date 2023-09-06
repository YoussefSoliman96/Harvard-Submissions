import sys
def main():
    argument_check()
    file_type_check(file)
    output = []



# Check if the command line arguments are 2
def argument_check():
    if (len(sys.argv) < 3):
        sys.exit("Too few command-line arguments")
    elif (len(sys.argv) > 3):
        sys.exit("Too many command-line arguments")
    # If command-line arguments pass the test, they are split into file_name and extensions
    first_name, first_extension = splitext(sys.argv[1])
    second_name, second_extension = splitext(sys.argv[2])


# Check if input and output files are in correct format
def file_type_check(file):
     extensions = [".jpg", ".jpeg", "png"]
     if file in extensions:
         return True
     return False










if __name__ == "__main__":
    main()