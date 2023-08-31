x = str.casefold(input("File name: "))
y = x.split(".", 1)
extension = y[1]
print(extension)
match extension:
    case jpg