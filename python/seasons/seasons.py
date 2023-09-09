from datetime import date
import re
import sys

def main():
    date_of_birth = input("Date of Birth: ")
    try:
         year, month, day = get_date(date_of_birth)
    except:
        sys.exit("Invalid format")
    print(date(int(year), int(month), int(day)))

def get_date(date):

    if re.search(r"(^[0-9]{4})-([0-9]{2})-([0-9]{2})$", date):
        year, month, day = date.split("-")
        return(year, month, day)


if __name__ == "__main__":
    main()