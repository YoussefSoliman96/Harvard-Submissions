x = input("What the answer to the Great Question of Life, the Universe and Everything: ")
y = str.casefold(x)
z = y.strip()
match z:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")