from datetime import date
import re


def main():
    date = input("Date of Birth: ")
    get_date(date)

def get_date(date):
    date = re.search(r"(^[0-9]+)-([0-9]+)-([0-9]+)$")
    print(date)


if __name__ == "__main__":
    main()