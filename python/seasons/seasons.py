from datetime import date
import re


def main():
    date = input("Date of Birth: ")
    get_date(date)

def get_date(date):
    new_date = date.fromisoformat('2019-12-04')
    datetime.date(2019, 12, 4)
    print(new_date)


if __name__ == "__main__":
    main()