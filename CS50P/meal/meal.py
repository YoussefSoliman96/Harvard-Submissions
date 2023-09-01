x, y = input("What time is it: ").split(":")
x = float(x)
y = float(y)
if x >= 7 and x <=8:
    print("breakfast time")
elif x >= 12 and x <=13:
    print("lunch time")
elif x >= 18 and x <=19:
    print("dinner time")