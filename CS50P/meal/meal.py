def main():
    time = input("What time is it: ")
    n = convert(time)
    if n >= 7 and n <=8:
        print("breakfast time")
    elif n >= 12 and n <=13:
        print("lunch time")
    elif n >= 18 and n <=19:
        print("dinner time")

def convert(n):
    x, y = n.split(":")
    nx = float(x)
    ny = float(y) / 60
    return nx + ny

if __name__ == "__main__":
    main()