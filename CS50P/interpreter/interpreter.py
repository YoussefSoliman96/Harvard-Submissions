input = input("Expression: ")
x, y, z = input.split(" ")
nx = float(x)
nz = float(z)
if y == "+":
    output = nx + nz
elif y == "-":
    output = nx - nz
elif y == "*":
    output = nx * nz
elif y == "/":
    output = nx / nz
    print(output)

