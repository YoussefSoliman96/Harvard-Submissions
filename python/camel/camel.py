x = input("camelCase: ")
print("snake_case: ", end="")
for c in x:
    if c.isupper():
        y = "_" + c.lower()
        print(y, end="")
    else:
        print(c, end="")
print()x = input("camelCase: ")
for c in x:
    print(c)
    if c.isupper() = True
        