from datetime import date
import re
import sys


def main():
    date = input("Date of Birth: ")
    new_date = get_date(date)
    print(new_date)

def get_date(date):
    try:
        if re.search(r"(^[0-9]{4})-([0-9]{2})-([0-9]{2})$", date):
            year, month, day = date.split("-")
            return(year, month, day)
    except:
        sys.exit("Invalid date")
        

if __name__ == "__main__":
    main()