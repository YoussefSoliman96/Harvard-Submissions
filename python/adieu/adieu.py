import inflect
p = inflect.engine()
# Make a list to keep all user inputs
names = []
# Take user input
# Loop forever and re-prompt the user for input
while True:
    try:
        name = input("Name: ")
        names.append(name)
# When user clicks ctrl-d, print an empty space and break
    except EOFError:
        print("")
        break

# print the output starting with Adieu, adieu, to
output = p.join(names)
print(f"Adieu, adieu, to {output}")