input = input("Expression: ")
x, y, z = input.split()
nx = float(x)
nz = float(z)
match y:
    case "+":
        output = nx + nz
    case "-":
        output = nx - nz
    case "*":
        output = nx * nz
    case "/":
        output = nx / nz
print(output)

