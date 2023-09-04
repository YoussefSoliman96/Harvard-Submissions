def main():
    number = input("Fraction: ")
    fraction = convert(number)
    output = gauge(fraction)
    print(output)



def convert(fraction):
    while True:
        try:
            x = fraction.split("/")
            result = int((int(x[0]) / int(x[1])))
            if result <= 1:
                return result
        except ValueError:
            raise
        except ZeroDivisionError:
            raise

def gauge(result):
    p = round(result * 100)
    # If percentage < 1%, print E
    if p <= 1:
        return "E"
    elif p >= 99:
        return "F"
    else:
        return (f"{p}%")

if __name__ == "__main__":
    main()