x = str.casefold(input("File name: "))
y = x.split(".", 1)
z = y.strip
extension = y[1]
name = y[0].strip()
match extension:
    case ".gif" in filename:
        print("image/" + extension)
