plate = input("Plate: ")
x = len(plate)
print(x)
letters = plate[0 : int(x/2)]
numbers = plate[int(x/2) : x]
print(letters, numbers)