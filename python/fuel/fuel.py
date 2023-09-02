# Take user input
# Loop forever until user input is in the right format (True)
while True:
    fraction = input("Fraction: ")
    try:
        x = fraction.split("/")
        result = (int(x[0]) / int(x[1]))
        if result <= 1:
            break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass

# Calculate the percentage
p = round(result * 100)
# If percentage < 1%, print E
if p <= 1:
    print("E")
elif p >=99:
    print("F")
else:
    print(f"{p}%")