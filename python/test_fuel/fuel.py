def main():
    number = input("Fraction: ")
    fraction = convert(number)
    output = gauge(fraction)
    print(output)



def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            result = (int(x) / int(y))
            if result <= 1:
                return result
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

def gauge(result):
    p = int(result * 100)
    # If percentage < 1%, print E
    if p <= "1":
        return p
    elif p >= "99":
        return "F"
    else:
        return (f"{p}%")

if __name__ == "__main__":
    main()