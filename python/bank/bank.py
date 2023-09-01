x = input("Greeting: ").strip().split()
y = x[0].replace(',', '')
z = str.casefold(y)
print(y)

if z == "hello":
    print("$0")
elif z[0] == "h":
    print("$20")
else:
    print("$100")