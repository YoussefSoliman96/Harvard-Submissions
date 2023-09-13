def main():

    while True:
        try:
            card_number = str(input("Number: "))
            validate(card_number)
            break
        except ValueError:
            print("Invalid input")




def validate(number):
    multiplied = []
    summed = 0
    every_other_number_reversed = ([number[i] for i in filter(lambda a: a % 2 == 0, range(len(number)))]) [::-1]

    for j in range(len(every_other_number_reversed)):
        multiplied.append(int((every_other_number_reversed[j])) * 2)


    for k in range(len(multiplied)):
        summed += multiplied[int(k)]



if __name__ == "__main__":
    main()

    """

    """