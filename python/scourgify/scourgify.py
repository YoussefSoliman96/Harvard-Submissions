import sys
import csv

def main():
    argument_check()
    output = []
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for line in reader:
                last_name, first_name = line["name"].split(",")
                output.append({'first': first_name.lstrip(), 'last': last_name.lstrip(), 'house': line["house"].lstrip()})

    except FileNotFoundError:
        sys.exit("File does not Exist")
    with open(sys.argv[2], "w") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writerow({"first": "first", "last": "last", "house": "house"})
            for line in output:
                writer.writerow({"first": line["first"], "last": line["last"], "house": line["house"]})


def argument_check():
    # Check if the command line arguments are 2
    if (len(sys.argv) < 3):
        sys.exit("Too few command-line arguments")
    elif (len(sys.argv) > 3):
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")








if __name__ == "__main__":
    main()