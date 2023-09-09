from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    date_of_birth = input("Date of Birth: ")
    try:
         # Exit the program if the user inputs a wrong format
         year, month, day = get_date(date_of_birth)
    except:
        sys.exit("Invalid format")
    # Get the original date of birth and today's date to calculate the number of days between them
    original_date = date(int(year), int(month), int(day))
    today_date = original_date.today()
    days = today_date - original_date
    mins = days.days * 24 * 60
    words = p.number_to_words(mins, andword="")
    final = words.capitalize() + " minutes"
    print(final)


def get_date(date):
    # Make sure the entered date is in correct format
    if re.search(r"(^[0-9]{4})-([0-9]{2})-([0-9]{2})$", date):
        year, month, day = date.split("-")
        return(year, month, day)


if __name__ == "__main__":
    main()