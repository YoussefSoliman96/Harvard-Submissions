# Take user input
# Loop forever until user input is in the right format (True)
try:
    fraction = input("Fraction: ")
except ValueError:
    print("")
except ZeroDivisionError:
    print("")
x = fraction.split("/")
result = (int(x[0]) / int(x[1]))*100
print(f"%{result}")