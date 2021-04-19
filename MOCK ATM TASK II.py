# DATETIME MODULE 
# Register 
#- firstName, lastName, Email, UserPin, BVN
#- Generate Account Number

# LOGIN
#- Account Number & UserPin

# BANK OPERATIONS

# Importing Datetime from Datetime module
from datetime import datetime

now = datetime.now()
dtString = now.strftime ("%d/%m/%y: %H:%M:%S %p")
print ("Date/Time =", dtString)

########### INITIALISING THE SYSTEM #########
import random

database = {}
saving_account_balance = (10000)
current_account_balance = (15000)

def init ():
    isValidOptionSelected = False
    print ("Welcome to Maxi Online Banking")

    while isValidOptionSelected == False:

        haveAccount = int ( input ("Do You Have an Account With Us?: 1. (YES) 2. (NO) \n"))

        if (haveAccount == 1):
            isValidOptionSelected = True 
            login ()
        
        elif(haveAccount == 2):
            isValidOptionSelected = True 
            register ()
        
        else:
            print ("Invalid Option Selected")

# USER LOGIN SECTION
def login ():

    print ("***** Login ***** \n")
    accountNumber = int (input ("Enter Account Number \n"))
    userPinLogin = int (input ("Enter User Pin \n"))

    for userAccountNumber, userDetails in database.items():
        if (accountNumber == userAccountNumber):
            if (userDetails[3] == userPinLogin):
                bankOperation()
            else:print ("Invalid username or Password ")
            print (" ")
            login ()
        
        else:
            print ("Invalid username or Password ")
            print (" ")
            login ()

# USER REGISTRATION SECTION
def register ():
    print ("******** Please Create An Account ******** \n")
    first_name = input ("What is your first name? \n")
    last_name = input ("What is your last name? \n")
    email = input ("What is your Email address? \n")
    userPin = int (input ("Create a 4 digit pin number? \n"))
    print ("Welcome %s, You have successfully created an account with us!!" %first_name)
    print ("====== ====== ====== ====== ====== ====== ======")

    userAccountNumber = generateUserAccountNumber ()

    #database[userAccountNumber] = [first_name, last_name, email, userPin]

    print ("Here is your Maxi Bank Account Number %d" % userAccountNumber)
    print ("====== ====== ====== ====== ====== ====== ======")
    print ("Make sure you keep it safe as it would be required to Login to your Account \n")

    database[userAccountNumber] = [first_name, last_name, email, userPin]
    login()

# USER BANKING OPERATION
def bankOperation():
    print ("Welcome, You are now logged in")
    selectedOption = int (input ("What would you like to do? \n 1. Withdrawal, \n 2. Deposit, \n 3. Check Balance, \n 4. Complaints, \n 5. Exit \n"))
    if (selectedOption == 1):
        withdrawal()
    elif (selectedOption == 2):
        deposit()
    elif (selectedOption == 3):
        checkbalance()
    elif (selectedOption == 4):
        complaint()

        
    elif (selectedOption == 5):
        exit()

        
def withdrawal():
    accountTypeSelection = int (input ("Select an Account Type 1. Savings, 2. Current \n"))
    if (accountTypeSelection == 1):
        print ("1. 1000")
        print ("2. 3000")
        print ("3. 5000")
        print ("4. 10000")
        print ("5. other")

        optionSelect = int (input ("Please select an option \n"))
        saving_account_balance = (10000)
        if (optionSelect == 1):
            print ("Please Wait, Your Transaction is Processing......")
            print ("Take Your Cash.")
            print ("Your New Savings Account Balance: ", saving_account_balance - optionSelect)
            

        elif (optionSelect == 2):
            saving_account_balance = (10000)
            print ("Please Wait, Your Transaction is Processing......")
            print ("Take Your Cash.")
            print ("Your New Savings Account Balance: ", saving_account_balance - optionSelect)
        
        elif (optionSelect == 3):
            saving_account_balance = (10000)
            print ("Please Wait, Your Transaction is Processing......")
            print ("Take Your Cash.")
            print ("Your New Savings Account Balance: ", saving_account_balance - optionSelect)

        elif (optionSelect == 4):
            saving_account_balance = (10000)
            print ("Please Wait, Your Transaction is Processing......")
            print ("Take Your Cash.")
            print ("Your New Savings Account Balance: ", saving_account_balance - optionSelect)

        elif (optionSelect == 5):
            print ("How Much Would You Like To Withdraw?")
            amount = int (input ("Enter Amount \n"))
            saving_account_balance = (10000)
            if amount < saving_account_balance:
                print ("Please Wait, Your Transaction is Processing......")
                print ("Take Your Cash.")
                print ("Your New Savings Account Balance: ", saving_account_balance - amount)

            else:
                print ("Insufficient Balance, Would you like to try something else?")
                print ("1. YES")
                print ("2. NO")

                option = int (input ("Please Select an Option \n"))
                if (option == 1):
                    bankOperation()

                elif (option == 2):
                    print ("Have a nice Day... \n")
                    login()
                    

    elif (accountTypeSelection == 2):
        print ("1. 1000")
        print ("2. 3000")
        print ("3. 5000")
        print ("4. 10000")
        print ("5. other")

        optionSelect = int (input ("Please select an option \n"))
        current_account_balance = (15000)
        if (optionSelect == 1):
            print ("Please Wait, Your Transaction is Processing......")
            print ("Take Your Cash.")
            print ("Your New Current Account Balance: ", current_account_balance - optionSelect)
            

        elif (optionSelect == 2):
            current_account_balance = (15000)
            print ("Please Wait, Your Transaction is Processing......")
            print ("Take Your Cash.")
            print ("Your New Current Account Balance: ", current_account_balance - optionSelect)
        
        elif (optionSelect == 3):
            current_account_balance = (15000)
            print ("Please Wait, Your Transaction is Processing......")
            print ("Take Your Cash.")
            print ("Your New Current Account Balance: ", current_account_balance - optionSelect)

        elif (optionSelect == 4):
            current_account_balance = (15000)
            print ("Please Wait, Your Transaction is Processing......")
            print ("Take Your Cash.")
            print ("Your New Current Account Balance: ", current_account_balance - optionSelect)

        elif (optionSelect == 5):
            print ("How Much Would You Like To Withdraw?")
            amount = int (input ("Enter Amount \n"))
            current_account_balance = (15000)
            if amount < current_account_balance:
                print ("Please Wait, Your Transaction is Processing......")
                print ("Take Your Cash.")
                print ("Your New Current Account Balance: ", current_account_balance - amount)

            else:
                print ("Insufficient Balance, Would you like to try something else?")
                print ("1. YES")
                print ("2. NO")

                option = int (input ("Please Select an Option \n"))
                if (option == 1):
                    bankOperation()

                elif (option == 2):
                    print ("Have a nice Day... \n")
                    login()

    else:
        print ("Invalid Option Selected")
        bankOperation ()



def deposit():
    print ("How much would you like to deposit?")

def checkbalance():
    print ("some operations")

def complaints():
    print ("some operatioms")

def exit():
    exit
    

def generateUserAccountNumber ():
    return random.randrange(1111111111,9999999999)
    generateUserAccountNumber ()


#print (generateUserAccountNumber())
init ()