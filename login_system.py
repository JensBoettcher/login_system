#this python project simulate an login system we know from websites

#import re module for creating and checking mail and password patterns
import re

#mail_checker function for existing mail address and new mail addresses
def mail_checker():
    mail = input("Please type in your email address. ")
    mail_pattern = ("^[a-zA-z0-9\.\-_]+@{1}[a-zA-z0-9]+\.{1}[a-zA-Z]{2,3}$")
    if re.search(mail_pattern, mail):
        print(f"The mail address {mail} is valid")
    else:
        print(f"The mail address {mail} is invalid, come back with a valid mail address. ")


#welcome the user
print("Welcome to the login screen.")

#ask the user for account information or account creation
account = input("Do you have an a account? (yes/no)").lower()
#the user have an account
if account == "yes":
    print("Ok you already have an account to login.")

    #ask for the mail address
    mail = input("Please type in your email address. ")

    #check the email address with the pattern
    mail_pattern = ("^[a-zA-z0-9\.\-_]+@{1}[a-zA-z0-9]+\.{1}[a-zA-Z]{2,3}$")
    if re.search(mail_pattern, mail):
        print(f"Youre email address {mail} is valid.")

        #ask the user for the password and save it to the variable "password"
        password = input("Please type in your password for the account. ")

        #check password with the "password database" txt file
        pw_db = open("pwdb.txt", 'r')
        for line in pw_db:
            line = line.strip().split(", ")
            if mail == line[0] and password == line[1]:
                print("Welcome to your account.")
                break
            else:
                print("Your password is invalid.")

    #kick the user after type in a invalid mail address
    else:
        print("Please come back with a valid email address.")


#the user have no account and create a new one    
else:
    mail = input("Please type in a valid email address. ")
    