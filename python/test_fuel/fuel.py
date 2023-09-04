def main():
    fraction = convert(fraction)



def convert(fraction):
    while True:
        fraction = input("Fraction: ")
        try:
            x = fraction.split("/")
            result = (int(x[0]) / int(x[1]))
            if result <= 1:
                return result
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

def gauge(percentage):
    p = round(result * 100)
    # If percentage < 1%, print E
    if p <= 1:
        print("E")
    elif p >=99:
        print("F")
    else:
        print(f"{p}%")

if __name__ == "__main__":
    main()