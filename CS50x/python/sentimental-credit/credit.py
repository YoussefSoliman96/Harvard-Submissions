def main():

    while True:
        try:
            card_number = str(input("Number: "))
            if (validate(card_number)) == "Invalid":
                print("INVALID")
            else:
                if (len(card_number)) == 15:
                    print("AMEX")
                elif if (len(card_number)) == 16:
                    print("")
        except ValueError:
            print("Invalid input")




def validate(number):
    multiplied = []
    # Identify every other number starting from index 0 then reversing them
    even_positions = ([number[i] for i in filter(lambda a: a % 2 == 0, range(len(number)))]) [::-1]
    # multiply every other number by 2
    for j in range(len(even_positions)):
        multiplied.append(int((even_positions[j])) * 2)

    # Modified multiplied with single digits only
    modified = []

    for i in range(len(multiplied)):
        if len(str(multiplied[i])) > 1:
            split = divmod(multiplied[i], 10)
            modified.append(split[0])
            modified.append(split[1])
        else:
            modified.append(multiplied[i])


    # Adding the numbers in the multiplied list together
    even_summed = sum(modified)

    # Identifying every other number that was not multiplied and adding them together
    odd_positions = ([number[i] for i in filter(lambda a: a % 2 == 1, range(len(number)))])
    odd_positions = [int(i) for i in odd_positions]
    odd_summed = sum(odd_positions)

    # Adding the 2 sums together
    sum_all = even_summed + odd_summed

    # Getting the last digit
    sum_all = [int(i) for i in str(sum_all)]
    last_digit = sum_all[-1]

    # Return Valid if last digit is "0", otherwise, return Invalid
    if last_digit == 0:
        return "Valid"
    else:
        return "Invalid"



def sum(number):
    summed = 0
    for k in range(len(number)):
        summed += number[int(k)]
    return summed

if __name__ == "__main__":
    main()

    """

    """