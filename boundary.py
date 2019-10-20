import getpass
import os
import time
import re

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

from user.user import User
from user.user import Admin
from user.user import Customer
from user.user import Owner

from customerController import CustomerController
from ownerController import OwnerController

class Boundary:
    """The Boundary object contains a user's interaction with the system

    Args:
    Attributes:
    """

    def __init__(self):
        self.runCode()

    def __repr__(self):
        return "Boundary()"

    def displayPage(self,inputDict):
        """This is the only function which will display on the Screen
            Args:
                - inputDict -- a dictionary with keys {'pageName', 'userName', 'optionDisplay', 'pageNavDict', 'footerDisplay', 'state', 'headerDisplay'}
                    pageName is mandatory and rest all are optional
            Raises:
            Returns:
        """
        os.system('clear')
        print('-' * 105)
        print('{0:^105}'.format(inputDict['pageName']))
        print('-' * 105)
        # Display User Name
        if 'userName' in inputDict.keys():
            print('{0:^105}'.format('Logged in as ' + inputDict['userName'].capitalize()))
            print('-' * 105)
        if 'headerDisplay' in inputDict.keys():
            print('{:^105}'.format(inputDict['headerDisplay']))
            print('-' * 105)
        if 'optionDisplay' in inputDict.keys():
            if isinstance(inputDict['optionDisplay'], dict):
                # Menu Options format
                tempString = '{0:^5}{1:^30}'.format('[Keys]', 'Options')
                print('{:^105}'.format(tempString))
                print('-' * 105)
                # display menu
                for key, option in inputDict['optionDisplay'].items():
                    tempString = '{0:^5}{1:^30}'.format('['+ key +']', option)
                    print('{:^105}'.format(tempString))
                    # print('{0:>4}{1}{2:<5}{3:^30}'.format('[', key, ']', option))
                print('-' * 105)
                # navigation panel
            elif isinstance(inputDict['optionDisplay'], list):
                # print("Its a list")
                # time.sleep(2)
                # Menu Options format
                # display menu
                tableHeader = ("{0:^5}{1:^15}{2:^15}{3:^15}{4:^15}".format('Key', 'Venue', 'Type', 'Addr', 'Capacity'))
                print("{0:^105}".format(tableHeader))
                for row in inputDict['optionDisplay']:
                    rowWise = ("{0:^5}{1:^15}{2:^15}{3:^15}{4:^15}".format(row[0], row[1], row[3], row[4], row[5]))
                    print('{:^105}'.format(rowWise))
                print('-' * 105)
        if 'footerDisplay' in inputDict.keys():
            print('{0:^105}'.format(inputDict['footerDisplay']))
            print('-' * 105)
        if 'pageNavDict' in inputDict.keys():
            navBar = ''
            for key, option in inputDict['pageNavDict'].items():
                navBarTemp = '{:^20}'.format('[' + key + ']' + option)
                navBar = navBar + navBarTemp
            print('{:^105}'.format(navBar))
            print('-' * 105)

    def selectOption(self,optionDisplay, pageNavDict):
        """This function allows selection to be made from either dictionary keys or list indices provided as arguments
            Args:
                - optionDisplay -- a dictionary or a list
                - pageNavDict -- a dictionary
            Raises:
            Returns:
                - success -- boolean
                    true if invalid selection made
                    false if valid selection is made
                - state -- int
        """
        selection = input('Enter your selection: ')
        selection = selection.upper()
        if isinstance(optionDisplay, dict) and selection in optionDisplay.keys():
            print('Your selection: {}'.format(optionDisplay.get(selection)))
            # input('Break')
            return False, selection
        # elif isinstance(optionDisplay, dict) and selection not in optionDisplay.keys():
        #     print('Your selection: {}'.format(selection))
        #     return True, ''
        elif isinstance(optionDisplay, list) and selection.isdigit():
            for row in optionDisplay:
                if row[0] == int(selection):
                    print('Your selection: {}'.format(selection))
                    return False, int(selection)
            else:
                print('Selection {} is not a valid. Kindly provide a valid selection'.format(selection))
                time.sleep(2)
                return True, ''
        elif selection in pageNavDict.keys():
            print('Your selection: {}'.format(pageNavDict.get(selection)))
            return False, selection
        else:
            print('Selection {} is not a valid. Kindly provide a valid selection'.format(selection))
            time.sleep(2)
            return True, ''

    def navOptions(self,selection, state):
        """This function returns the state necessary to Logout or Exit
            Args:
                - selection -- string
                - state -- int
            Raises:
            Returns:
                - state -- int
        """
        if selection == 'O':
            state = 1
        elif selection == 'E':
            state = 0
        return state

    def getPass(self,):
        """This function handles password prompt and hashing
            Args:
            Raises:
            Returns:
                - passHash -- string hashed password
        """
        # check password length more than or equal to 8
        passFlag = False
        while not passFlag:
            try:
                passPlain = getpass.getpass('Enter Password(must be >= 8): ')
            except UserWarning:
                print('Password will be visible')
                passPlain = input('Enter Password(must be >= 8): ')
            if len(passPlain) >= 8:
                passFlag = True
            else:
                passFlag = False
                print("Password must have 8 or more characters")
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(bytes(passPlain, 'utf-8'))
        passHash = digest.finalize()
        return passHash

    def acceptUserDetails(self,):
        """This function handles user registeration
            Args:
            Raises:
            Returns:
                - mailExistFlag -- boolean
                    true if mail id already exists in the system
                    false if mail id doesn't exist and can be used
                - userInfo -- dictionary
                    userName
                    password
        """
        os.system('clear')
        print('=' * 41)
        print('{:^41}'.format('Registration Page'))
        print('=' * 41)
        userInfo = dict()
        userInfo['firstName'] = input('Enter First Name: ')
        userInfo['lastName'] = input('Enter Last Name: ')
        mailExistFlag = True
        retryCount = 0
        while mailExistFlag and retryCount < 3:
            mailFormat = True
            while mailFormat == True and retryCount < 3:
                eMail = input('Enter Email Id: ')
                if re.match("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",eMail):
                    userInfo['email'] = eMail
                    mailFormat = False
                else:
                    retryCount = retryCount + 1
                    print("Not a valid mail id!! Kindly try again.")
            mailExistFlag = Owner.emailExists(userInfo['email'])
            retryCount = retryCount + 1
            if mailExistFlag == True and retryCount < 3:
                print("Mail id already used, try another mail id")
            elif mailExistFlag == True and retryCount == 3:
                print('Maximum attemps reached, taking back to login page')
                time.sleep(2)
            else:
                userInfo['password'] = self.getPass()
        return mailExistFlag, userInfo

    def userLogin(self,):
        """This function handles user login
            Args:
            Raises:
            Returns:
                - userInfo -- dictionary
                    success - boolean
                    userObj - object of User Class
        """
        loginFlag = False
        retryCount = 0
        while not loginFlag and retryCount < 3:
            userInfo = dict()
            userInfo['email'] = input('Enter Email Id: ')
            userInfo['password'] = self.getPass()
            userObj = (User(userInfo))
            retryCount = retryCount + 1
            loginFlag = userObj.success
            if not loginFlag and retryCount < 3:
                print('{}'.format('Mail id, password combination invalid'))
                success = False
            elif not loginFlag and retryCount == 3:
                print('{}'.format('Mail id, password combination invalid'))
                print('{}'.format('Maximum tries exceeded, redirecting to login page'))
                time.sleep(2)
                success = False
            else:
                success = True
        return {'success': success, 'userObj': userObj}

    def runCode(self):
        """This function controls flow of logic
            Args:
            Raises:
            Returns:
        """
        state = 1
        while state > 0:
            # state 1 represent login action
            while state == 1:
                pageName = 'Login Page'
                # userName = userName
                optionDisplay = {'L': 'Login', 'O': 'Register as Owner', 'C': 'Register as Customer'}
                pageNavDict = {'E': 'Exit'}
                os.system('clear')
                displayDict = {'pageName': pageName, 'optionDisplay': optionDisplay, 'pageNavDict': pageNavDict}
                self.displayPage(displayDict)
                invalidSelectionFlag, selection = self.selectOption(optionDisplay, pageNavDict)
                if not invalidSelectionFlag:
                    if selection == 'O':
                        mailExistFlag, userInfo = self.acceptUserDetails()
                        # create a user object
                        if mailExistFlag:
                            state = 1
                        else:
                            userObj = Owner(userInfo)
                            state = 2
                    elif selection == 'C':
                        mailExistFlag, userInfo = self.acceptUserDetails()
                        # create a user object
                        if mailExistFlag:
                            state = 1
                        else:
                            userObj = Customer(userInfo)
                            state = 2
                    elif selection == 'L':
                        objDict = self.userLogin()
                        if objDict['success']:
                            if objDict['userObj'].getAllowFlag() == 0:
                                state = 2
                                userObj = objDict['userObj']
                            elif objDict['userObj'].getAllowFlag() == 1:
                                print('User blocked, redirecting to login page')
                                time.sleep(2)
                                state = 1
                    elif selection == 'E':
                        exit()
                else:
                    print('Invalid selection, Please input again')
            print('State is {} and session ID is {} and user type is {}'.format(state, userObj.getRowId(),
                                                                                userObj.getUserType()))
            # call respective controller to deal with further action
            while state == 2 and userObj.getUserType() == 'Customer':
                customerController = CustomerController(userObj)
                state = customerController.getState()
            while state == 2 and userObj.getUserType() == 'Owner':
                ownerController = OwnerController(userObj)
                state = ownerController.getState()
            print(state)
        else:
            exit()



if __name__ == "__main__":
    boundaryObj = Boundary()
