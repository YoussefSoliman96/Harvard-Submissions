x = input("camelCase: ")
for c in x:
    if c.isupper() == True:
        y = "_" + c.lower()
        c = y
        print(c, end="")
    else:
        print(c, end="")
print()