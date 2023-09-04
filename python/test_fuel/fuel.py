def main():
    fraction = input("Fraction: ")
    number = convert(fraction)
    output = gauge(number)
    print(output)



def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            result =  x / y
            if result <= 1:
                p = int(result * 100)
                return p
            else:
                fraction = input("Fraction: ")
                pass
        except ValueError:
            raise
        except ZeroDivisionError:
            raise

def gauge(p):
    # If percentage < 1%, print E
    if p <= 1:
        return "E"
    elif p >= 99:
        return "F"
    else:
        return (f"{p}%")

if __name__ == "__main__":
    main()