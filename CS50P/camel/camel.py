x = input("camelCase: ")
print("snake_case: ", end="")
for c in x:
    if c.isupper():
        y = "_" + c.lower()
        print(y, end="")
    else:
        print(c, end="")
print()