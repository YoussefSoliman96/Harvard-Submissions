import sys
import validators

def main():
    email = input("What's your email address? ")
    print(validation(email))



def validation(email):
    validator = validators.email(email)
    if validator == True:
        return "Valid"
    else:
        return "Invalid"




if __name__ == "__main__":
    main()