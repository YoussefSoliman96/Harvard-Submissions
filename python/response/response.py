import sys
import re
import validators

def main():
    email = input("What's your email address? ")
    print(validators.email(email))



def validation(email):
    validator = validators.email(email)
    if validator == True




if __name__ == "__main__":
    main()