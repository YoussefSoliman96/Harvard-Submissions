# Take user input
# Loop forever until user input is in the right format (True)
while True:
    try:
        fraction = input("Fraction: ")
    except ValueError:
        pass
    except ZeroDivisionError:
        pass

    x = fraction.split("/")
    result = (int(x[0]) / int(x[1]))*100
    print(f"%{result}")