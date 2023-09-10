import csv
import sys


def main():
    class Client:
        def __init__(self, first_name, last_name, email, savings):
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.savings = savings
    # Get all the clients' data
    clients_data = read_file()
    # Extract all the clients' names out of the file
    get_names(clients_data)
    # Get the requested client's data
    client_data = get_data(clients_data)
    # Get the requested client's savings
    client_savings = (client_data["savings"])
    print(client_savings)


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

# Get all the clients' names
def get_names(client_data):
    for d in client_data:
        return([d["first_name"]])

# Get the a certain client's data
def get_data(client_data):
    # Loop forever untill the user inputs a valid name or (Control-d)
    while True:
        try:
            # Take user's input of a certain client's name
            client_search = input("Client name: ")
            # Loop through all the client names untill you find the client then return the data
            for name in client_data:
                if name["first_name"] == client_search:
                    return(name)
        except EOFError:
            sys.exit("User input invalid")

if __name__ == "__main__":
    main()



"""


def get_date():




def deposit():


def withdraw():



def calculate_savings():

"""