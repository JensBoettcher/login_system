#this python project simulate an login system we know from websites

#import re module for creating and checking mail and password patterns
import re

#mail_checker function for existing mail address and new mail addresses
def mail_checker():
    mail_pattern = ("^[a-zA-z0-9\\.\\-_]+@{1}[a-zA-z0-9]+\\.{1}[a-zA-Z]{2,3}$")
    if re.search(mail_pattern, mail):
        print(f"The mail address {mail} is valid")
    else:
        print(f"The mail address {mail} is invalid, come back with a valid mail address. ")


def pw_checker():
    pw_pattern = ("^[a-zA-z0-9{1}\\.\\-]$")


#welcome the user
print("Welcome to the login screen.")

#ask the user for account information or account creation
account = input("Do you have an a account? (yes/no)").lower()
#the user have an account
if account == "yes":
    print("Ok you already have an account to login.")
    mail = input("Please type in your email address. ")

    #mail_checker function for mail pattern check
    mail_checker()

    #ask the user for the password and save it to the variable "password"
    password = input("Please type in your password for the account. ")

    #check password with the "password database" txt file
    pw_db = open("pwdb.txt", 'r')
    for line in pw_db:
        line = line.strip().split(", ")
        if mail == line[0] and password == line[1]:
            print("Welcome to your account.")
        
        else:
            print("Your password is invalid.")


#the user have no account and create a new one    
else:
    #mail address for the new account
    mail = input("Please type in a valid email address. ")

    #mail_checker function for mail pattern check
    mail_checker()

    #new password for the account
    new_password = input("Please type in a password for your account. ")


    