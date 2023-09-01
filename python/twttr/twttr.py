x = input("Input: ")
print("Output: ", end="")
for c in x:
    y = c.lower()
    if y == "a" or y == "e" or y == "i" or y == "o" or y == "u":
        v = c.replace(c, "")
        print(v, end="")
    else:
        print(c, end="")
print()