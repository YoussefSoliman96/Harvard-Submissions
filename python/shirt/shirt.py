import sys
def main():
    argument_check()
    output = []
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for line in reader:
                last_name, first_name = line["name"].split(",")
                output.append()

    except FileNotFoundError:
        sys.exit("File does not Exist")
    with open(sys.argv[2], "w") as file:
            writer = csv.DictWriter(file, fieldnames=[])
            writer.writerow({)
            for line in output:



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