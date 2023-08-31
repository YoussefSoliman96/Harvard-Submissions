x = input("Greeting: ").strip().split()
y = x[0].replace(',', '')
print(y)

if y == "hello":
    print("$0")