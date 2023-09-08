import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    ums = re.findall(r"\bum\b", s, re.IGNORECASE)
    print(ums)


...


if __name__ == "__main__":
    main()