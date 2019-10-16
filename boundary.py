import getpass
import os
import time

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

from user.user import *

from customerController import CustomerController
from ownerController import OwnerController

class Boundary:
    """Boudary class for Primer Events"""

    def __init__(self):
        self.runCode()


    def displayPage(self,inputDict):
        """if userName exists then will be displayed on self.selectOption
        if optionDisplay exists then display
            if optionDisplay is a dict display as dict
            if optionDisplay is a list display as list
            {'pageName':, 'userName': , 'optionDisplay':, 'pageNavDict': , 'footerDisplay': , 'state': , 'headerDisplay': }
        pageName = inputDict['pageName']
        userName = inputDict['userName']
        optionDisplay = inputDict['optionDisplay']
        pageNavDict = inputDict['pageNavDict']
        footerDisplay = inputDict['footerDisplay']
        state = inputDict['state']
        headerDisplay = inputDict['headerDisplay']
        {'pageName': pageName = None, 'userName': userName = None, 'optionDisplay': optionDisplay = None, 'pageNavDict': pageNavDict = None, 'state': state}"""
        os.system('clear')
        # Display Page Name
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
            if isinstance(inputDict['optionDisplay'], list) and inputDict['state'] == 7:
                tableHeader = ("{0:^5}{1:^30}{2:^20}{3:^20}{4:^10}{5:^10}{6:^10}".format('ID', 'Request Date-Time', 'Booking Start-Date', 'Booking End-Date', 'Hall ID', 'Status', 'Charge'))
                print("{0:^105}".format(tableHeader))
                # for value in optionDisplay:
                for tup in inputDict['optionDisplay']:
                    tempString = ("{0:^5}{1:^30}{2:^20}{3:^20}{4:^10}{5:^10}{6:^10}".format(tup[0], tup[1], tup[2], tup[3], tup[4], tup[6], tup[7]))
                    print('{:^105}'.format(tempString))
                print('-' * 105)

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
                # navigation panel

            if isinstance(inputDict['optionDisplay'], tuple) and inputDict['state'] == 5:
                tableHeader = ("{0:^5}{1:^15}{2:^15}{3:^15}{4:^15}{5:^15}".format('ID', 'Venue', 'Tariff/day', 'Function Type', 'Address', 'Capacity'))
                print("{0:^105}".format(tableHeader))
                # for value in optionDisplay:
                tempString = ("{0:^5}{1:^15}{2:^15}{3:^15}{4:^15}{5:^15}".format(inputDict['optionDisplay'][0], inputDict['optionDisplay'][1], inputDict['optionDisplay'][3], inputDict['optionDisplay'][4], inputDict['optionDisplay'][5], inputDict['optionDisplay'][6]))
                print('{:^105}'.format(tempString))
                print('-' * 105)

            if 'footerDisplay' in inputDict.keys():
                print('{0:^105}'.format(inputDict['footerDisplay']))
                print('-' * 105)
                # navigation panel
        if 'pageNavDict' in inputDict.keys():
            navBar = ''
            for key, option in inputDict['pageNavDict'].items():
                navBarTemp = '{:^20}'.format('[' + key + ']' + option)
                navBar = navBar + navBarTemp
            print('{:^105}'.format(navBar))
            print('-' * 105)

    def selectOption(self,optionDisplay, pageNavDict):
        """selection made is from either dictionary keys or list indices
        return true and null string if invalid selection made and
        return false and selection in appropriate format if valid selection is made"""
        # prompt user to select option
        selection = input('Enter your selection: ')
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
        """

        :param selection:
        :type state: object
        """
        if selection == 'O':
            state = 1
        elif selection == 'E':
            state = 0
        return state

    def getPass(self,):
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
            userInfo['email'] = input('Enter Email Id: ')
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
        state = 1
        while state > 0:
            # state 1 represent login action
            while state == 1:
                pageName = 'Login Page'
                # userName = userName
                optionDisplay = {'L': 'Login', 'O': 'Register as Owner', 'C': 'Register as Customer'}
                pageNavDict = {'E': 'Exit'}
                # message = message
                # state = state
                # headerDisplay = headerDisplay
                os.system('clear')
                # landingPage = {'L': 'Login', 'O': 'Register as Owner', 'C': 'Register as Customer'}
                # navPageDict = {'E': 'Exit'}
                # userNamePlaceHolder = ''
                displayDict = {'pageName': pageName, 'optionDisplay': optionDisplay, 'pageNavDict': pageNavDict}
                self.displayPage(displayDict)
                # self.displayPage('Login Page', userNamePlaceHolder, landingPage, pageNavDict)
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
                            print('User info is {}'.format(userInfo))
                            print('State is {} and session ID is {} and user type is {}'.format(state,
                                                                                                userObj.getRowId(),
                                                                                                userObj.getUserType()))
                            time.sleep(2)
                            # print(owner.getRowId())
                    elif selection == 'C':
                        mailExistFlag, userInfo = self.acceptUserDetails()
                        # create a user object
                        if mailExistFlag:
                            state = 1
                        else:
                            userObj = Customer(userInfo)
                            state = 2
                            print('User info is {}'.format(userInfo))
                            print('State is {} and session ID is {} and user type is {}'.format(state,
                                                                                                userObj.getRowId(),
                                                                                                userObj.getUserType()))
                            time.sleep(2)
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
    boundaryObj.main()
