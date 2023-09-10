import csv
import sys


def main():
    class Client:
        def __init__(self, first_name, last_name, email, savings):
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.savings = savings
    client_data = read_file()
    print(client_data[0])

# Read the file containing clients' data
def read_file():
    clients = []
    try:
        # Open the file containing clients' data
        with open("clients.csv", "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            # Loop through the file and append data to the clients stack
            for line in csv_reader:
                clients.append({'first_name': line["first_name"], 'last_name': line["last_name"], 'email': line["email"], 'savings': line["savings"]})
        return clients
    except FileNotFoundError:
        sys.exit("File not found")


if __name__ == "__main__":
    main()




"""


def get_date():




def deposit():


def withdraw():



def calculate_savings():

"""