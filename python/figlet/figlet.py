import sys
if len(sys.argv) == 1:
    random = True
elif len(sys.argv) == 3:
    random = False






from pyfiglet import Figlet



input = ("Input: ")
figlet = Figlet()
figlet.getFonts()
figlet.setFont(font=f)
print(figlet.renderText(s))