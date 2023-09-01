plate = input("Plate: ")
x = int(len(plate))
letters = plate[0:x/2]
numbers = plate[x/2/x]
print(letters, numbers)