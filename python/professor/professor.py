import random
def main():
    level = get_level()
    get_level(level)


def get_level():
    while True:
        n = int(input("Level: "))
        try:
            if n == 1 or n == 2 or n == 3:
                break
        except:
            pass
    return n


def generate_integer(level):
    i = 0
    while i < 10:
        


if __name__ == "__main__":
    main()
