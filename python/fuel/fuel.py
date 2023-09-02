# Take user input
# Loop forever until user input is in the right format (True)
while True:
    fraction = input("Fraction: ")
    try:
        x = fraction.split("/")
        result = round((int(x[0]) / int(x[1]))*100)
        if result <= 1:
            break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass

    print(f"%{result}")