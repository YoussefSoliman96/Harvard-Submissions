import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
# Checking whether to print a random font or a certain font that the user requested
if len(sys.argv) == 1:
    randomn = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    randomn = False
else:
    sys.exit(1)

# Import fonts
figlet.getFonts()
# Set the font after importing it and setting it's name to f
if randomn == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("Wrong command line argument")
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts())

# Take user input
input = input("Input: ")

print(f"Output:\n {figlet.renderText(input)}")