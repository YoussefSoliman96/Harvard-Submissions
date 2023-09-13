import sys
import csv
from tabulate import tabulate

def main():
    argument_check()
    menu = []
    try:
        # Read the csv file
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
            for line in reader:
                menu.append(line)
    except FileNotFoundError:
        sys.exit("File does not exist")
    print(tabulate(menu[1:], headers = menu[0], tablefmt = "grid"))




def argument_check():
    # Check if command-line arguments are not 2
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # Check if file does not end with .py
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")










if __name__ == "__main__":
    main()