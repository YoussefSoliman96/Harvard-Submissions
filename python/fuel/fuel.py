# Take user input
# Loop forever until user input is in the right format (True)
while True:
    fraction = input("Fraction: ")
    try:
        x = fraction.split("/")
        

    except ValueError:
        pass
    except ZeroDivisionError:
        pass


    result = (int(x[0]) / int(x[1]))*100
    print(f"%{result}")