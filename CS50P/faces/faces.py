def main():
    x = input()
    y = convert(x)
    print(y)



def convert (x):
    x1 = x.replace(':)', '🙂')
    x2 = ":(" : x.replace(':)', '🙁')
    return x2
main()