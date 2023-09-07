import re
import sys


def main():
    groups = print(convert(input("Hours: ")))
    time = new_format(groups[0], groups[1], groups[2])


def convert(s):
    format =  re.search(r"^([0-9]+):*([0-5]*) ([A-P]M) to ([0-9]+):*([0-5]*) ([A-P]M)$", s)
    if format:
        groups = format.groups()
        if int(groups[0]) > 12 or int(groups[4]) > 12:
            raise ValueError
        return groups

    else:
        raise ValueError

def new_format(hour, min, a_p):
    if int(a_p) == "AM":
        if hour == 12:
            new_hour == 00
        else:
            new_hour == hour
    else:
        if hour == 12:
            new_hour == hour
        else:
            new_hour = hour + 12
    if min == None:
        min = ":00"




if __name__ == "__main__":
    main()