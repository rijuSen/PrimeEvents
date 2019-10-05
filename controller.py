from user.user import *
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import time
import getpass
import os

#controller class
def displayPage(pageName, userName, pageMenuDict, pageNavDict):
    os.system('clear') 
    #Display Page Name
    print('-'*40)
    print('{0:^40}'.format(pageName))
    print('-'*40)
    #Display User Name
    if not len(userName) == 0:
        print('{0:>40}'.format('Logged in as '+userName))
        print('-'*40)
    if not len(pageMenuDict) == 0:
        #Menu Options format
        print('Input key to select corresponding option')
        print('-'*40)
        print('{0:^10}{1:^30}'.format('[Keys]','Options'))
        print('-'*40)
        #display menu
        for key, option in pageMenuDict.items():
            print('{0:>4}{1}{2:<5}{3:^30}'.format('[', key, ']', option))
        print('-'*40)
            #navigation panel
        print('-'*40)
    if not len(pageNavDict) == 0:
        navBar = ''
        for key, option in pageNavDict.items():
            navBarTemp = '{:^10}'.format('['+key+']'+option)
            navBar = navBar + navBarTemp
        print('{:^41}'.format(navBar))
    print('-'*40)



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


def displayTableFormat(output,startIndex):
    print("{0:^5}{1:^10}{2:^10}{3:^10}{4:^10}".format('ID','Hall-Name','Hall-Type','Hall-Addr','Hall-Capacity'))
    for row in output[startIndex:startIndex + 4:1]:
        print("{0:^5}{1:^10}{2:^10}{3:^10}{4:^10}".format(row[0],row[1],row[3],row[4],row[5]))


class Session:
    '''class to maintain a session'''
    def _init_(self, rowId, userType):
        self.sessionId = rowId
        self.userType = userType

    def getSessionId(self):
        return self.rowId

    def getUserType(self):
        return self.userType

