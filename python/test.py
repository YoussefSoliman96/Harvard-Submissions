plate = input("Plate: ")
for i in plate:
    letters = plate[0:int(i)/2]
    numbers = plate[int(i)/2:i]
    print(letters, numbers)