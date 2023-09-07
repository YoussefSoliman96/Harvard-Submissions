import re
import sys


def main():
   print(convert(input("Hours: ")))


def convert(s):
    format =  re.search(r"^([0-9]+):*([0-5]*) ([A-P]M) to ([0-9]+):*([0-5]*) ([A-P]M)$", s)
    if format:
        groups = format.groups()
        # Raise a value Error if hours are more than 12
        if int(groups[0]) > 12 or int(groups[3]) > 12:
            raise ValueError
        first_output = new_format(groups[0], groups[1], groups[2])
        second_output = new_format(groups[3], groups[4], groups[5])
        return f"{first_output} to {second_output}"

    else:
        raise ValueError

def new_format(hour, min, a_p):
    if a_p == "AM":
        # Set hours to 00 if input is 12 AM
        if int(hour) == 12:
            new_hour = 00
        else:
            new_hour = int(hour)
    else:
        if int(hour) == 12:
            new_hour = int(hour)
        else:
            new_hour = int(hour) + 12
    if min == "":
        time = f"{new_hour:02}" + ":00"
    else:
        time = f"{new_hour:02}" + ":" + min
    return time



if __name__ == "__main__":
    main()