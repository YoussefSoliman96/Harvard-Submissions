import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search("<iframe(.)*><\/iframe>", s)

...


if __name__ == "__main__":
    main()