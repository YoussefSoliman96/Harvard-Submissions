x = input("Input: ")
for c in x:
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
        y = c.replace("c", "")
        print(y)
    else:
        print(c)