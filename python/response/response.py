import sys
import re
import validators

def main():
    email = print(input("What's your email address? "))

    validation = validators.email(email)

    print(validation)






if __name__ == "__main__":
    main()