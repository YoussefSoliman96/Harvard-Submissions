def main():

    while True:
        try:
            card_number = str(input("Number: "))
            validate(card_number)
        except ValueError:
            print("Invalid input")




def validate(number):
    every_other_number = []
    for i in range(len(number)):
        if i % 2 == 0:
            every_other_number.append(number[i])
    print (every_other_number)



if __name__ == "__main__":
    main()