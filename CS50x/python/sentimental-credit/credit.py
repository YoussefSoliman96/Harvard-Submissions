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
    even_numbers = ([number[i] for i in filter(lambda a: a % 2 == 0, range(len(number)))]) [::-1]

    for j in range(len(even_numbers)):
        multiplied.append(int((even_numbers[j])) * 2)


    even_summed = sum(multiplied)
    print(even_summed)

    odd_numbers = ([number[i] for i in filter(lambda a: a % 1 == 0, range(len(number)))])

    odd_summed = sum(int(odd_numbers))
    print(odd_summed)



def sum(number):
    summed = 0
    for k in range(len(number)):
        summed += number[int(k)]
    return summed

if __name__ == "__main__":
    main()

    """

    """