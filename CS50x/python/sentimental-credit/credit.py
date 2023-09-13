def main():

    while True:
        try:
            card_number = str(input("Number: "))
            validate(card_number)
            break
        except ValueError:
            print("Invalid input")




def validate(number):
    every_other_number = []
    multiply = []
    for i in range(len(number)):
        if i % 2 == 0:
            every_other_number.append(number[i])
    every_other_number_reversed = every_other_number [::-1]

    for j in range(len(every_other_number_reversed)):
        every_other_number_reversed[j]
        multiply.append(int((every_other_number_reversed[j])) * 2)
    print(multiply)



if __name__ == "__main__":
    main()

    """
    one = (every_other_number[i] for i in (lambda a:a))
    """