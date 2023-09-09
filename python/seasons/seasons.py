from datetime import date
import re


def main():
    date = input("Date of Birth: ")
    get_date(date)

def get_date(date):
    new_date = date.fromisoformat(date)
    print(new_date)


if __name__ == "__main__":
    main()