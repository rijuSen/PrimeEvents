from user.user import *
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import time
import getpass
import os

import time

#controller class
def displayPage(pageName, userName, pageMenuDict, pageNavDict):
    invalidSelectionFlag = True
    while invalidSelectionFlag:
        os.system('clear') 
        #Display Page Name
        print('='*40)
        print('{0:^40}'.format(pageName))
        print('='*40)
        #Display User Name
        if not len(userName) == 0:
            print('{0:>40}'.format('Logged in as '+userName))
            print('='*40)
        #Menu Options format
        print('Input key to select corresponding option')
        print('='*40)
        print('{0:^10}{1:^30}'.format('[Keys]','Options'))
        print('='*40)
        #display menu
        for key, option in pageMenuDict.items():
            print('{0:>4}{1}{2:<5}{3:^30}'.format('[', key, ']', option))
        print('='*40)
        #navigation panel
        print('='*40)
        if not len(pageNavDict) == 0:
            for key, option in pageNavDict.items():
                print('{0}{1}{2}{3:>2}'.format('[',key,']',option), end = '')
            print()
        print('='*40)
        #selection variable can be used further when rest of the system would be developed
        invalidSelectionFlag, selection = selectOption(pageMenuDict,pageNavDict)
    return selection


def selectOption(pageMenuDict,pageNavDict):
    #prompt user to select option
    selection = input('Enter your selection: ')
    if selection in pageMenuDict.keys():
        print('Your selection: {}'.format(pageMenuDict.get(selection)))
        return False, selection
    elif selection in pageNavDict.keys():
        print('Your selection: {}'.format(pageNavDict.get(selection)))
        return False, selection
    else:
        print('Selection {} is not a valid. Kindly provide a valid selection'.format(selection))
        time.sleep(2)
        return True, ''
        


def getPass():
    #check password length more than or equal to 8
    passFlag = False
    while not passFlag:
        passPlain = getpass.getpass(prompt='Enter Password(must be >= 8): ')
        if len(passPlain) >= 8:
            passFlag = True 
        else:
            passFlag = False
            print("Password must have 8 or more characters")
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(bytes(passPlain, 'utf-8'))
    passHash = digest.finalize()
    return passHash

def acceptUserDetails():
    os.system('clear')
    print('='*41)
    print('{:^41}'.format('Registration Page'))
    print('='*41)
    fName = input('Enter First Name: ')
    lName = input('Enter Last Name: ')
    mailFlag = True 
    while mailFlag:
        email = input('Enter Email Id: ')
        mailFlag = Owner.emailExists(email)
        if mailFlag == True:
            print("Mail id already used, try another mail id")
            time.sleep(2)
    #call method to check password length and return hash of the password
    passHash = getPass() 
    return fName,lName,email,passHash 


def userLogin():
    os.system('clear')
    loginFlag = False
    while not loginFlag:
        email = input('Enter Email Id: ')
        passHash = getPass() 
        loginFlag, rowId, firstName, userType, allowFlag = User.checkPassword(email,passHash)
        print(str(loginFlag))
        if not loginFlag:
            print("Mail id and password combination doesn't exist, please try again")
            time.sleep(2)
            os.system('clear')
    return rowId, firstName, userType, allowFlag


