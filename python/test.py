plate = input("Plate: ")
x = len(plate)
print(x)
letters = plate[0 : x/2]
numbers = plate[x/2 : x]
print(letters, numbers)