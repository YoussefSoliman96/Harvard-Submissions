import sys
if len(sys.argv) == 1:
    random = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    random = False
else:
    sys.exit(1)

input = ("Input: ")






from pyfiglet import Figlet




figlet = Figlet()
figlet.getFonts()
figlet.setFont(font=f)
print(figlet.renderText(s))