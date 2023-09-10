import csv
import sys

"""
def main():
    class Client:
        def __init__(self, first_name, last_name, email, savings):
            self.first_name = first_name
            self.last_name = last_name
            self.email = email



def get_date():




def deposit():


def withdraw():



def calculate_savings():






if __name__ == "__main__"
    main()

"""

def read_file():
    clients = []
    try:
        with open("clients.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for line in csv_reader:
                clients.append(line)
        return clients
    except FileNotFoundError:
        sys.exit("File not found")

client = read_file()
print(client)
