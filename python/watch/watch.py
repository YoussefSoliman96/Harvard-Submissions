import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search("<iframe(.)*><\/iframe>", s):
        url = re.search("http(s)*:\/\/(www\.)*youtube\.com\/embed\/([a-zA-Z0-9]+)", s)
        if url:
            split = url.groups()
            return "https://youtu.be/" + split[2]


if __name__ == "__main__":
    main()