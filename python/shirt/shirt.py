import sys
from os.path import splitext
from PIL import Image, ImageOps
def main():
    argument_check()
    # Try to open the file
    try:
        image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    # Open the shirt image
    shirt = Image.open("shirt.png")
    # Get the size of the shirt
    size = shirt.size
    # Resize the muppet
    muppet = ImageOps.fit(image, size)
    # Overlay shirt over new muppet and save it in output file
    muppet.paste(shirt, shirt)
    muppet.save(sys.argv[2])



# Check if input and output files are in correct format
def file_type_check(file):
     extensions = [".jpg", ".jpeg", ".png"]
     if file in extensions:
         return True
     return False

# Check if the command line arguments are 2
def argument_check():
    if (len(sys.argv) < 3):
        sys.exit("Too few command-line arguments")
    elif (len(sys.argv) > 3):
        sys.exit("Too many command-line arguments")
    # If command-line arguments pass the test, they are split into file_name and extensions
    first_name, first_extension = splitext(sys.argv[1].lower())
    second_name, second_extension = splitext(sys.argv[2].lower())

    if file_type_check(first_extension) == False:
        sys.exit("First file extension invalid")
    if file_type_check(second_extension) == False:
        sys.exit("Second file extension invalid")
    if first_extension != second_extension:
        sys.exit("Input and Output file got different formats")




if __name__ == "__main__":
    main()