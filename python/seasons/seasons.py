from datetime import date
import re
import sys

def main():
    date = input("Date of Birth: ")
    try:
         year, month, day = get_date(date)
    except:
        sys.exit("Invalid format")
    print(year, month, day)

def get_date(date):

    if re.search(r"(^[0-9]{4})-([0-9]{2})-([0-9]{2})$", date):
        year, month, day = date.split("-")
        return(year, month, day)


if __name__ == "__main__":
    main()