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
    even_positions = ([number[i] for i in filter(lambda a: a % 2 == 0, range(len(number)))]) [::-1]

    for j in range(len(even_positions)):
        multiplied.append(int((even_positions[j])) * 2)


    even_summed = sum(multiplied)
    print(even_summed)

    odd_positions = ([number[i] for i in filter(lambda a: a % 2 == 1, range(len(number)))])

    print(multiplied)



def sum(number):
    summed = 0
    for k in range(len(number)):
        summed += number[int(k)]
    return summed

if __name__ == "__main__":
    main()

    """

    """