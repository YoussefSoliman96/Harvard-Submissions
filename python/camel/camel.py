x = input("camelCase: ")
print("snake_case: ", end="")
for c in x:
    if c.isupper():
        y = "_" + c.lower()
        c = y
        print(c, end = "")
    else:
        print(c, end = "")