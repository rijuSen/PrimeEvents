import os
import time
import datetime
from hall.hall import Hall
from quotation.quotation import Quotation
from booking.booking import Booking
from payment.payment import Payment

class OwnerController:
    """Owner Controller"""
    def __init__(self, userObj):
        self.userObj = userObj
        self.state = 2
        self.ownerController(self.userObj)

    def getState(self):
        return self.state

    def displayPage(self, inputDict):
        """This is the only function which will display on the Screen
            Args:
                - inputDict -- a dictionary with keys {'pageName', 'userName', 'optionDisplay', 'pageNavDict', 'footerDisplay', 'state', 'headerDisplay'}
                    pageName is mandatory and rest all are optional
            Raises:
            Returns:
        """
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
            if isinstance(inputDict['optionDisplay'], dict) and 'state' in inputDict.keys() and inputDict['state'] == 8:
                tempString = '{0:^30}{1:^40}'.format('Attribute', 'Value')
                print('{:^105}'.format(tempString))
                for key, value in inputDict['optionDisplay'].items():
                    tempString = '{0:^30}{1:^40}'.format(key.capitalize(), value)
                    print('{:^105}'.format(tempString))
                print('-' * 105)

            elif isinstance(inputDict['optionDisplay'], dict):
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
            elif isinstance(inputDict['optionDisplay'], list) and 'state' in inputDict.keys() and inputDict['state'] == 5:
                tableHeader = ("{0:^5}{1:^30}{2:^20}{3:^20}{4:^10}{5:^10}{6:^10}".format('Key', 'Start-Date', 'End-Date','Venue', 'Customer', 'Status','Amount'))
                print("{0:^105}".format(tableHeader))
                # for value in optionDisplay:
                for tup in inputDict['optionDisplay']:
                    tempString = ("{0:^5}{1:^30}{2:^20}{3:^20}{4:^10}{5:^10}{6:^10}".format(tup[0], tup[1], tup[2], tup[3], tup[4], tup[5], tup[6]))
                    print('{:^105}'.format(tempString))
                print('-' * 105)

            elif isinstance(inputDict['optionDisplay'], list) and 'state' in inputDict.keys() and inputDict['state'] == 8:
                tableHeader = ("{0:^5}{1:^10}{2:^20}{3:^10}{4:^10}{5:^20}{6:^20}".format('Key', 'Booking ID', 'Type', 'Amount', 'Customer', 'Coupon Code', 'Status'))
                print("{0:^105}".format(tableHeader))
                # for value in optionDisplay:
                for tup in inputDict['optionDisplay']:
                    tempString = ("{0:^5}{1:^10}{2:^20}{3:^10}{4:^10}{5:^20}{6:^20}".format(tup[0], tup[5], tup[1], tup[3], tup[6], tup[2], tup[4]))
                    print('{:^105}'.format(tempString))
                print('-' * 105)

            elif isinstance(inputDict['optionDisplay'], list) and 'state' in inputDict.keys() and inputDict['state'] == 7:
                tableHeader = ("{0:^5}{1:^15}{2:^15}{3:^10}{4:^10}{5:^10}{6:^10}".format('ID', 'Start-Date', 'End-Date', 'Hall ID', 'Customer','Amount Paid', 'Status'))
                print("{0:^105}".format(tableHeader))
                for row in inputDict['optionDisplay']:
                    rowWise = ("{0:^5}{1:^15}{2:^15}{3:^10}{4:^10}{5:^10}{6:^10}".format(row[0], row[1], row[2], row[3], row[4], row[6], row[5]))
                    print('{:^105}'.format(rowWise))
                print('-' * 105)
                # navigation panel
            elif isinstance(inputDict['optionDisplay'], list):
                tableHeader = ("{0:^5}{1:^15}{2:^15}{3:^15}{4:^20}{5:^15}".format('ID', 'Venue', 'Tariff/Day', 'Type', 'Addr', 'Capacity'))
                print("{0:^105}".format(tableHeader))
                for row in inputDict['optionDisplay']:
                    rowWise = ("{0:^5}{1:^15}{2:^15}{3:^15}{4:^20}{5:^15}".format(row[0], row[1], row[3], row[4], row[5], row[6]))
                    print('{:^105}'.format(rowWise))
                print('-' * 105)
                # navigation panel

            elif isinstance(inputDict['optionDisplay'], tuple) and inputDict['state'] == 4:
                tableHeader = ("{0:^5}{1:^15}{2:^15}{3:^15}{4:^15}{5:^15}".format('ID', 'Venue', 'Tariff/day', 'Function Type', 'Address', 'Capacity'))
                print("{0:^105}".format(tableHeader))
                # for value in optionDisplay:
                tempString = ("{0:^5}{1:^15}{2:^15}{3:^15}{4:^15}{5:^15}".format(inputDict['optionDisplay'][0], inputDict['optionDisplay'][1], inputDict['optionDisplay'][3], inputDict['optionDisplay'][4], inputDict['optionDisplay'][5], inputDict['optionDisplay'][6]))
                print('{:^105}'.format(tempString))
                print('-' * 105)

            elif isinstance(inputDict['optionDisplay'], tuple) and inputDict['state'] == 6:
                tableHeader = ("{0:^5}{1:^30}{2:^20}{3:^20}{4:^10}{5:^10}{6:^10}".format('Key', 'StartDate', 'EndDate','Venue', 'Customer', 'Status','Amount'))
                print("{0:^105}".format(tableHeader))
                # for value in optionDisplay:
                tempString = ("{0:^5}{1:^30}{2:^20}{3:^20}{4:^10}{5:^10}{6:^10}".format(inputDict['optionDisplay'][0], inputDict['optionDisplay'][1], inputDict['optionDisplay'][2], inputDict['optionDisplay'][3], inputDict['optionDisplay'][4], inputDict['optionDisplay'][5], inputDict['optionDisplay'][6]))
                print('{:^105}'.format(tempString))
                print('-' * 105)

            elif isinstance(inputDict['optionDisplay'], tuple) and inputDict['state'] == 9:
                tableHeader = ("{0:^5}{1:^10}{2:^20}{3:^10}{4:^10}{5:^20}{6:^20}".format('Key', 'Booking ID', 'Type', 'Amount', 'Customer', 'Coupon Code', 'Status'))
                print("{0:^105}".format(tableHeader))
                # for value in optionDisplay:
                tempString = ("{0:^5}{1:^10}{2:^20}{3:^10}{4:^10}{5:^20}{6:^20}".format(inputDict['optionDisplay'][0], inputDict['optionDisplay'][5], inputDict['optionDisplay'][1], inputDict['optionDisplay'][3], inputDict['optionDisplay'][6], inputDict['optionDisplay'][2], inputDict['optionDisplay'][4]))
                print('{:^105}'.format(tempString))
                print('-' * 105)

        if 'footerDisplay' in inputDict.keys():
            print('{0:^105}'.format(inputDict['footerDisplay']))
            print('-' * 105)
            # navigation panel
        if 'pageNavDict' in inputDict.keys():
            navBar = ''
            for key, option in inputDict['pageNavDict'].items():
                navBarTemp = '{:^15}'.format('[' + key + ']' + option)
                navBar = navBar + navBarTemp
            print('{:^105}'.format(navBar))
            print('-' * 105)

    def selectOption(self, optionDisplay, pageNavDict):
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
        # prompt user to select option
        selection = input('Enter your selection: ')
        selection = selection.upper()
        if isinstance(optionDisplay, dict) and selection in optionDisplay.keys():
            print('Your selection: {}'.format(optionDisplay.get(selection)))
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

    def navOptions(self, selection, state):
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

    def acceptHallDetails(self, userObj):
        """This function handles Hall registration
            Args:
                - userObj -- User
            Raises:
            Returns:
                - hallExistFlag -- boolean
                    true if hall name already exists in the system for the same user
                    false if hall name doesn't exist and can be used
                - hallInfo -- dictionary
                    hallName
                    dayTariff
                    hallType
                    hallAddr
                    hallCapacity
                    ownerId
        """
        os.system('clear')
        print('=' * 65)
        print('{:^65}'.format('New Hall Page'))
        print('=' * 65)
        hallInfo = dict()
        hallExistFlag = True
        retryCount = 0
        while hallExistFlag and retryCount < 3:
            hallInfo['hallName'] = input('Enter Hall Name: ')
            hallExistFlag = Hall.hallExists(hallInfo['hallName'], userObj)
            retryCount = retryCount + 1
            if hallExistFlag == True and retryCount < 3:
                print("Hall already exists, try another Hall name")
            elif hallExistFlag == True and retryCount == 3:
                print('Maximum attemps reached, taking back to Manage Halls page')
                time.sleep(2)
            else:
                invalidPriceFlag = True
                while invalidPriceFlag:
                    dayTariff = input('Enter Hall Per Day Tariff: ')
                    if dayTariff.isdigit():
                        invalidPriceFlag = False
                    else:
                        print('{}{}'.format(dayTariff,' is not a valid Tariff. Please enter valid value'))
                hallInfo['dayTariff'] = dayTariff
                hallInfo['hallType'] = input('Enter Hall Type: ')
                hallInfo['hallAddr'] = input('Enter Hall Addr: ')
                invalidCapacityFlag = True
                while invalidCapacityFlag:
                    hallCapacity = input('Enter Hall Capacity: ')
                    if hallCapacity.isdigit():
                        invalidCapacityFlag = False
                    else:
                        print('{}{}'.format(hallCapacity,' is not a valid Capacity. Please enter valid value'))
                hallInfo['hallCapacity'] = hallCapacity
                hallInfo['ownerId'] = userObj.getRowId()
        return hallExistFlag, hallInfo

    def acceptModifyHallDetails(self, userObj, optionDisplay):
        """This function handles Hall registration
            Args:
                - userObj -- User
                - optionDisplay -- Tuple contaning hall info which is to be modified
            Raises:
            Returns:
                - hallExistFlag -- boolean
                    true if hall name already exists in the system for the same user
                    false if hall name doesn't exist and can be used
                - hallInfo -- dictionary - updated
                    hallName
                    dayTariff
                    hallType
                    hallAddr
                    hallCapacity
                    ownerId
        """
        os.system('clear')
        print('=' * 65)
        print('{:^65}'.format('Modify Hall Page'))
        print('=' * 65)
        tableHeader = ("{0:^5}{1:^15}{2:^10}{3:^10}{4:^15}{5:^10}".format('Key', 'Venue', 'Tariff','Type', 'Addr', 'Capacity'))
        print("{0:^65}".format(tableHeader))
        tempString = ("{0:^5}{1:^15}{2:^10}{3:^10}{4:^15}{5:^10}".format(optionDisplay[0], optionDisplay[1], optionDisplay[3], optionDisplay[4], optionDisplay[5], optionDisplay[6]))
        print('{:^65}'.format(tempString))
        print('-' * 65)
        hallInfo = dict()
        hallExistFlag = True
        retryCount = 0
        while hallExistFlag and retryCount < 3:
            hallInfo['hallName'] = input('Enter new Hall Name: ')
            if optionDisplay[1] != hallInfo['hallName']:
                hallExistFlag = Hall.hallExists(hallInfo['hallName'], userObj)
            else:
                hallExistFlag = False
            retryCount = retryCount + 1
            if hallExistFlag == True and retryCount < 3:
                print("Hall already exists, try another Hall name")
            elif hallExistFlag == True and retryCount == 3:
                print('Maximum attemps reached, taking back to Manage Halls page')
                time.sleep(2)
            else:
                invalidPriceFlag = True
                while invalidPriceFlag:
                    dayTariff = input('Enter Hall Per Day Tariff: ')
                    if dayTariff.isdigit():
                        invalidPriceFlag = False
                    else:
                        print('{}{}'.format(dayTariff,' is not a valid Tariff. Please enter valid value'))
                hallInfo['dayTariff'] = dayTariff
                hallInfo['hallType'] = input('Enter new Hall Type: ')
                hallInfo['hallAddr'] = input('Enter new Hall Addr: ')
                invalidCapacityFlag = True
                while invalidCapacityFlag:
                    hallCapacity = input('Enter Hall Capacity: ')
                    if hallCapacity.isdigit():
                        invalidCapacityFlag = False
                    else:
                        print('{}{}'.format(hallCapacity,' is not a valid Capacity. Please enter valid value'))
                hallInfo['hallCapacity'] = hallCapacity
                hallInfo['ownerId'] = userObj.getRowId()
        return hallExistFlag, hallInfo

    def ownerController(self, userObj):
        """
        This method contains all functionality related to the owner along with the flow
            Args:
                - userObj -- User
            Raises:
            Returns:
        """
        state = 2
        while state >= 2:
            while state == 2:
                pageName = 'Owner Home Screen'
                userName = userObj.getFirstName()
                optionDisplay = {'1': 'Manage Halls', '2': 'View Quotation Request', '3': 'Manage Bookings', '4': 'Manage Payments'}
                pageNavDict = {'O': 'Logout', 'E': 'Exit'}
                headerDisplay = 'Input key to select corresponding option'
                displayDict = {'pageName': pageName, 'userName': userName, 'optionDisplay': optionDisplay, 'pageNavDict': pageNavDict, 'headerDisplay': headerDisplay}
                self.displayPage(displayDict)
                invalidSelectionFlag, selection = self.selectOption(optionDisplay, pageNavDict)
                # for navigation menu
                if not invalidSelectionFlag:
                    if selection in pageNavDict:
                        state = self.navOptions(selection, state)
                    elif selection == '1':
                        # take to next state to display hall listing
                        state = 3
                    elif selection == '2':
                        state = 5
                    elif selection == '3':
                        state = 7
                    elif selection == '4':
                        state = 8
                else:
                    print('Invalid selection, Please input again')

            while state == 3:
                    optionDisplay = Hall.viewUserHalls(userObj)
                    pageName = 'Manage Hall Page'
                    userName = userObj.getFirstName()
                    pageNavDict = {'O': 'Logout', 'E': 'Exit', 'B': 'Back', 'A': 'Add New Hall'}
                    headerDisplay = 'Input key to select corresponding option'
                    displayDict = {'pageName': pageName, 'userName': userName, 'optionDisplay': optionDisplay, 'pageNavDict': pageNavDict, 'headerDisplay': headerDisplay}
                    self.displayPage(displayDict)
                    invalidSelectionFlag, selection = self.selectOption(optionDisplay, pageNavDict)
                    # for navigation menu
                    if not invalidSelectionFlag:
                        if selection in pageNavDict:
                            if selection == 'A':
                                hallExistFlag, hallInfo = self.acceptHallDetails(userObj)
                                # create a user object
                                if hallExistFlag:
                                    state = 3
                                else:
                                    confirmation = input('Confirm Addition Request(Y/N): ')
                                    if confirmation.isalpha():
                                        if confirmation.lower() == 'y':
                                            #create object of quotations
                                            hallObj = Hall(hallInfo)
                                        elif confirmation.lower() == 'n':
                                            print('Taking back to previous menu')
                                            time.sleep(1)
                                    state = 3
                            if selection == 'B':
                                state = 2
                            state = self.navOptions(selection, state)
                        else:
                            # take to next state to display hall listing
                            state = 4
                    else:
                        print('Invalid selection, Please input again')

            while state == 4:
                index = int(selection)
                optionDisplay = Hall.viewHallDetails(index)
                pageName = 'Hall Detail Page'
                userName = userObj.getFirstName()
                pageNavDict = {'M': 'Modify Hall', 'D': 'Delete Hall','B': 'Go Back', 'O': 'Logout', 'E': 'Exit'}
                headerDisplay = 'Input key to select corresponding option'
                displayDict = {'pageName': pageName, 'userName': userName, 'optionDisplay': optionDisplay, 'pageNavDict': pageNavDict, 'headerDisplay': headerDisplay, 'state': state}
                self.displayPage(displayDict)
                #placeholder dictionary
                bookHallPage = dict()
                #displayPage('Hall Details', userObj.getFirstName(), hallDetails, navPageDict, state)
                invalidSelectionFlag, selection = self.selectOption(optionDisplay, pageNavDict)
                if not invalidSelectionFlag:
                    if selection in pageNavDict:
                        if selection == 'B':
                            state = 3
                        if selection == 'M':
                            hallExistFlag, hallModify = self.acceptModifyHallDetails(userObj, optionDisplay)
                            # create a user object
                            if not hallExistFlag:
                                hallModify['Modify'] = True
                                confirmation = input('Confirm Modification Request(Y/N): ')
                                if confirmation.isalpha():
                                    if confirmation.lower() == 'y':
                                        #create object of quotations
                                        hallObj = Hall(hallModify)
                                        hallObj.modifyhall(optionDisplay[0], hallModify)
                                    elif confirmation.lower() == 'n':
                                        print('Taking back to previous menu')
                                        time.sleep(1)
                            state = 3
                        elif selection == 'D':
                            hallDelete = dict()
                            hallDelete['requested'] = True
                            confirmation = input('Confirm Delete Request(Y/N): ')
                            if confirmation.isalpha():
                                if confirmation.lower() == 'y':
                                    #create object of quotations
                                    hallObj = Hall(hallDelete)
                                    hallObj.deletehall(optionDisplay[0])
                                elif confirmation.lower() == 'n':
                                    print('Taking back to previous menu')
                                    time.sleep(1)
                            state = 3
                        else:
                            state = self.navOptions(selection, state)
                else:
                    print('Invalid selection, Please input again')

            while state == 5:
                optionDisplay = Quotation.listOwnerQuotationRequests(userObj.getRowId())
                pageName = 'Requested Quotations Page'
                userName = userObj.getFirstName()
                pageNavDict = {'O': 'Logout', 'E': 'Exit', 'B': 'Back'}
                headerDisplay = 'Input key to select corresponding option'
                displayDict = {'pageName': pageName, 'userName': userName, 'optionDisplay': optionDisplay, 'pageNavDict': pageNavDict, 'headerDisplay': headerDisplay, 'state': state}
                self.displayPage(displayDict)
                #navPageDict = {'O': 'Logout', 'E': 'Exit', 'B': 'Back'}
                #displayPage('Requested Quotations Page', userObj.getFirstName(), quotationList, navPageDict, state)
                invalidSelectionFlag, selection = self.selectOption(optionDisplay, pageNavDict)
                if not invalidSelectionFlag:
                    if selection == 'B':
                        state = 2
                    elif selection in pageNavDict:
                        state = self.navOptions(selection, state)
                    else:
                        # take to next state to display hall listing
                        state = 6
                else:
                    print('Invalid selection, Please input again')

            while state == 6:
                index = int(selection)
                optionDisplay = Quotation.viewQuotationDetails(index)
                pageName = 'Quotation Details Page'
                userName = userObj.getFirstName()
                if(optionDisplay[5] == 'Pending'):
                    pageNavDict = {'A': 'Accept', 'M':'Modify','R': 'Reject','B': 'Go Back', 'O': 'Logout', 'E': 'Exit'}
                else:
                    pageNavDict = {'B': 'Go Back', 'O': 'Logout', 'E': 'Exit'}
                headerDisplay = 'Input key to select corresponding option'
                displayDict = {'pageName': pageName, 'userName': userName, 'optionDisplay': optionDisplay, 'pageNavDict': pageNavDict, 'headerDisplay': headerDisplay, 'state': state}
                self.displayPage(displayDict)
                #displayPage('Quotation Details', userObj.getFirstName(), quotationDetails, navPageDict, state)
                #placeholder dictionary
                QuotationPage = dict()
                invalidSelectionFlag, selection = self.selectOption(optionDisplay, pageNavDict)
                if not invalidSelectionFlag:
                    if selection in pageNavDict:
                        if selection == 'B':
                            state = 5
                        if selection == 'M':
                            newAmount = input('Enter New Quotation Amount: ')
                            if newAmount.isdigit():
                                confirmation = input('Confirm Modification Request(Y/N): ')
                                if confirmation.isalpha():
                                    if confirmation.lower() == 'y':
                                        #create object of quotations
                                        Quotation.changeAmount(optionDisplay[0], newAmount)
                                    elif confirmation.lower() == 'n':
                                        print('Taking back to previous menu')
                                        time.sleep(1)
                                    state = 5
                            else:
                             print('Please enter a valid value[float only]')
                             selection = index
                             time.sleep(1)
                        elif selection == 'A':
                            confirmation = input('Confirm Accept Request(Y/N): ')
                            if confirmation.isalpha():
                                if confirmation.lower() == 'y':
                                    #create object of quotations
                                    Quotation.changeStatus(optionDisplay[0], 'Approved')
                                elif confirmation.lower() == 'n':
                                    print('Taking back to previous menu')
                                    time.sleep(1)
                                state = 5
                        elif selection == 'R':
                            confirmation = input('Confirm Reject Request(Y/N): ')
                            if confirmation.isalpha():
                                if confirmation.lower() == 'y':
                                    #create object of quotations
                                    Quotation.changeStatus(optionDisplay[0], 'Rejected')
                                elif confirmation.lower() == 'n':
                                    print('Taking back to previous menu')
                                    time.sleep(1)
                                state = 5
                        else:
                            state = self.navOptions(selection, state)
                else:
                    print('Invalid selection, Please input again')

            while state == 7:
                optionDisplay = Booking.listOwnerBookings(userObj.getRowId())
                pageName = 'Completed Bookings'
                userName = userObj.getFirstName()
                pageNavDict = {'B': 'Go Back', 'O': 'Logout', 'E': 'Exit'}
                displayDict = {'pageName': pageName, 'userName': userName, 'optionDisplay': optionDisplay, 'pageNavDict': pageNavDict, 'state': state}
                # tableHeader =
                self.displayPage(displayDict)
                placeHolder = dict()
                invalidSelectionFlag, selection = self.selectOption(placeHolder, pageNavDict)
                if not invalidSelectionFlag:
                    if selection in pageNavDict:
                        if selection == 'B':
                            state = 2
                        else:
                            state = self.navOptions(selection, state)
                else:
                    print('Invalid selection, Please input again')

            while state == 8:
                optionDisplay = Payment.listOwnerPaymentRequests(userObj.getRowId())
                pageName = 'Requested Payments Page'
                userName = userObj.getFirstName()
                pageNavDict = {'O': 'Logout', 'E': 'Exit', 'B': 'Back'}
                headerDisplay = 'Input key to select corresponding option'
                displayDict = {'pageName': pageName, 'userName': userName, 'optionDisplay': optionDisplay, 'pageNavDict': pageNavDict, 'headerDisplay': headerDisplay, 'state': state}
                self.displayPage(displayDict)
                #navPageDict = {'O': 'Logout', 'E': 'Exit', 'B': 'Back'}
                #displayPage('Requested Quotations Page', userObj.getFirstName(), quotationList, navPageDict, state)
                invalidSelectionFlag, selection = self.selectOption(optionDisplay, pageNavDict)
                if not invalidSelectionFlag:
                    if selection == 'B':
                        state = 2
                    elif selection in pageNavDict:
                        state = self.navOptions(selection, state)
                    else:
                        # take to next state to display hall listing
                        state = 9
                else:
                    print('Invalid selection, Please input again')

            while state == 9:
                index = int(selection)
                optionDisplay = Payment.viewPaymentDetails(index)
                pageName = 'Payments Details Page'
                userName = userObj.getFirstName()
                if(optionDisplay[4] == 'Pending'):
                    pageNavDict = {'A': 'Accept', 'R': 'Reject','B': 'Go Back', 'O': 'Logout', 'E': 'Exit'}
                else:
                    pageNavDict = {'B': 'Go Back', 'O': 'Logout', 'E': 'Exit'}
                headerDisplay = 'Input key to select corresponding option'
                displayDict = {'pageName': pageName, 'userName': userName, 'optionDisplay': optionDisplay, 'pageNavDict': pageNavDict, 'headerDisplay': headerDisplay, 'state': state}
                self.displayPage(displayDict)
                #displayPage('Quotation Details', userObj.getFirstName(), quotationDetails, navPageDict, state)
                #placeholder dictionary
                QuotationPage = dict()
                invalidSelectionFlag, selection = self.selectOption(optionDisplay, pageNavDict)
                if not invalidSelectionFlag:
                    if selection in pageNavDict:
                        if selection == 'B':
                            state = 8
                        elif selection == 'A':
                            confirmation = input('Confirm Accept Request(Y/N): ')
                            if confirmation.isalpha():
                                if confirmation.lower() == 'y':
                                    #create object of quotations
                                    Payment.changeStatus(optionDisplay[0], 'Approved')
                                    Booking.changeStatus(optionDisplay[5], 'Confirmed')
                                elif confirmation.lower() == 'n':
                                    print('Taking back to previous menu')
                                    time.sleep(1)
                                state = 8
                        elif selection == 'R':
                            confirmation = input('Confirm Reject Request(Y/N): ')
                            if confirmation.isalpha():
                                if confirmation.lower() == 'y':
                                    #create object of quotations
                                    Payment.changeStatus(optionDisplay[0], 'Rejected')
                                    Booking.changeStatus(optionDisplay[5], 'Declined')
                                elif confirmation.lower() == 'n':
                                    print('Taking back to previous menu')
                                    time.sleep(1)
                                state = 8
                        else:
                            state = self.navOptions(selection, state)
                else:
                    print('Invalid selection, Please input again')

        self.state =  state
