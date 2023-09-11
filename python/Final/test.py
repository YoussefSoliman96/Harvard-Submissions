from datetime import datetime
import sys
def main():

    choices = ["Deposit", "Withdraw", "Print statement"]
    options(choices)

def options(choices):
    print("Please choose:")
    for idx, element in enumerate(choices):
        print("{}) {}".format(idx+1,element))
    i = input("Enter number: ")
    while True:
        try:
            if 0 < int(i) <= len(choices):
                return int(i)
        except EOFError:
            sys.exit("Invalid choice")

if __name__ == "__main__":
    main()