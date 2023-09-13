def main():

    while True:
        try:
            card_number = str(input("Number: "))
            validate(card_number)
        except ValueError:
            print("Invalid input")




def validate(number):
    multiplied = []
    reversed = number [::-1]
    # Identify every other number starting from index 0 then reversing them
    even_positions = ([reversed[i] for i in filter(lambda a: a % 2 == 0, range(len(reversed)))]) [::-1]
    # multiply every other number by 2
    for j in range(len(even_positions)):
        multiplied.append(int((even_positions[j])) * 2)
    print(even_positions)

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
    odd_positions = ([reversed[i] for i in filter(lambda a: a % 2 == 1, range(len(reversed)))])
    odd_positions = [int(i) for i in odd_positions]
    odd_summed = sum(odd_positions)

    # Adding the 2 sums together
    sum_all = even_summed + odd_summed

    # Getting the last digit
    sum_all = [int(i) for i in str(sum_all)]
    last_digit = sum_all[-1]

"""
378282246310005
    0034227
"""
def sum(number):
    summed = 0
    for k in range(len(number)):
        summed += number[int(k)]
    return summed

if __name__ == "__main__":
    main()

