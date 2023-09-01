x = input("camelCase: ")
for c in x:
    if c.isupper() == True:
        y = "_" + c.lower()
        print(y)