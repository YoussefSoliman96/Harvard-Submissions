import csv
import sys


def main():

    # TODO: Check for command-line usage
    while True:
        try:
            if len(sys.argv) < 3:
                print("Too few command-line arguments")
            elif len(sys.argv) > 3:
                print("Too many command-line arguments")
            else:
                if not ".csv" in sys.argv[1] or not ".txt" in sys.argv[2]:
                    print("Invalid file format")
                else:
                    break
        except EOFError:
            print("Program stopped")

    # TODO: Read database file into a variable
    database = read_database(1)
    # TODO: Read DNA sequence file into a variable
    dna_sequence = read_sequence(2)
    # TODO: Find longest match of each STR in DNA sequence
    subsequence_count = {}
    for key in database[0].keys():
        if key != "name":
            subsequence_count[key] = longest_match(dna_sequence, key)

    # TODO: Check database for matching profiles
    for name in database:
        match = 0
        subsequences = list(database[0].keys())[1:]
        for key in subsequences:
            if int(name[key]) == subsequence_count[key]:
                match += 1
            if match == len(subsequences):
                print(name["name"])
                return
    print("No match")

def read_database(n):
    database = []
    try:
        # Open the file containing clients' data
        with open(sys.argv[n], "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for line in csv_reader:
                database.append(line)
        return database
    except FileNotFoundError:
        sys.exit("File not found")


def read_sequence(n):
    try:
        # Open the file containing clients' data
        with open(sys.argv[n], "r") as txt_file:
            sequence = txt_file.read()
        return sequence
    except FileNotFoundError:
        sys.exit("File not found")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
