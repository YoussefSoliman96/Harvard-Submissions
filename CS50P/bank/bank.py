x = input("Greeting: ").strip().split()
y = x[0].replace(',', '')
print(y)

if y == "hello":
    print("$0")
elif y[0] == "h":
    print("$20")
else:
    print("$100")