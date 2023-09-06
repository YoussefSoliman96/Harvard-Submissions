import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        input = ip.split(".")
        for number in input:
            if 0 > int(number) > 255:
                return False
        return True
    else:
        return False




if __name__ == "__main__":
    main()