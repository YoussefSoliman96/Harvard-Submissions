import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if re.search("[0-9]+:*[0-5]*[0-9]* AM to [0-9]:*[0-5]*[0-9]* PM", s):
        print(s)





if __name__ == "__main__":
    main()