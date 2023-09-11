from datetime import datetime
def main():
    choices = ["Deposit", "Withdraw", "Print statement"]
    options(choices)

    def options(choices):
        print("Please choose:")
        for idx, element in enumerate(choices):
            print("{}) {}".format(idx+1,element))
        i = input("Enter number: ")
        try:
            if 0 < int(i) <= len(choices):
                return int(i)
        except:
            pass
        return None

if __name__ == "__main__":
    main()