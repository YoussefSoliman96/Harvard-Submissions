x = str.casefold(input("File name: "))
y = x.split(".", 1)
extension = y[1]
name = y[0].strip()
match extension:
    case "gif":
        print("image/" + extension)
    case "jpg":
        print("image/" + extension)
    case "jpeg":
        print("image/" + extension)
    case "png":
        print("image/" + extension)
    case "pdf":
        print("application/" + extension)
    case "txt":
        print("text/" + name)
    case "zip":
        print("application/" + extension)
    case _:
        print("application/octet-stream")