import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    format =  re.search(r"^([0-9]+:*[0-5]*[0-9]*) ([A-P]M) to ([0-9]:*[0-5]*[0-9]*) ([A-P]M)$", s)
    if format:
        groups = format.groups()
        return groups

    else:
        raise ValueError





if __name__ == "__main__":
    main()