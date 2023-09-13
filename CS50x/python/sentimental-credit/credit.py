def main():

    while True:
        try:
            card_number = str(input("Number: "))
            validate(card_number)
            break
        except ValueError:
            print("Invalid input")




def validate(number):
    multiply = []
    every_other_number_reversed = ([number[i] for i in filter(lambda a: a % 2 == 0, range(len(number)))]) [::-1]

    multiplied = ([(lambda b: b * 2, range(len(every_other_number_reversed)))])

    print(multiplied)




if __name__ == "__main__":
    main()

    """
    multiplied = (every_other_number_reversed[i] for i in (lambda a: int(a) * 2, range(len(ever_other_number_reversed))))
    """