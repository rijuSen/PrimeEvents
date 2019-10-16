import os
import time
import datetime
from hall.hall import Hall
from quotation.quotation import Quotation
from booking.booking import Booking

class CustomerController:
    """Customer Controller"""
    def __init__(self, userObj):
        self.userObj = userObj
        self.state = 2
        self.customerController(self.userObj)

    def getState(self):
        return self.state

    def displayPage(self, inputDict):
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
            elif isinstance(inputDict['optionDisplay'], list) and 'state' in inputDict.keys() and inputDict['state'] == 7:
                tableHeader = ("{0:^5}{1:^30}{2:^20}{3:^20}{4:^10}{5:^10}{6:^10}".format('ID', 'Request Date-Time', 'Booking Start-Date', 'Booking End-Date', 'Hall ID', 'Status', 'Charge'))
                print("{0:^105}".format(tableHeader))
                # for value in optionDisplay:
                for tup in inputDict['optionDisplay']:
                    tempString = ("{0:^5}{1:^30}{2:^20}{3:^20}{4:^10}{5:^10}{6:^10}".format(tup[0], tup[1], tup[2], tup[3], tup[4], tup[6], tup[7]))
                    print('{:^105}'.format(tempString))
                print('-' * 105)

            elif isinstance(inputDict['optionDisplay'], list) and 'state' in inputDict.keys() and inputDict['state'] == 9:
                # CREATE TABLE bookings (
                #                   bookingStartDate date NOT NULL,
                #                   bookingEndDate date NOT NULL,
                #                   hallId int NOT NULL,
                #                   customerId int NOT NULL,
                #                   status boolean NOT NULL,
                #                   bookingAmount float NOT NULL,
                #                   quotationId int NOT NULL,
                #                   UNIQUE(quotationId),
                #                   FOREIGN KEY(customerId) REFERENCES users(rowid),
                #                   FOREIGN KEY(quotationId) REFERENCES quotations(rowid),
                #                   FOREIGN KEY(hallId) REFERENCES halls(rowid));
                tableHeader = ("{0:^5}{1:^20}{2:^20}{3:^5}{4:^15}".format('ID', 'Start-Date', 'End-Date', 'Hall ID', 'Amount Paid'))
                print("{0:^105}".format(tableHeader))
                for row in inputDict['optionDisplay']:
                    rowWise = ("{0:^5}{1:^20}{2:^20}{3:^5}{4:^15}".format(row[0], row[1], row[2], row[3], row[6]))
                    print('{:^105}'.format(rowWise))
                print('-' * 105)
                # navigation panel
            elif isinstance(inputDict['optionDisplay'], list):
                tableHeader = ("{0:^5}{1:^15}{2:^15}{3:^15}{4:^15}".format('Key', 'Venue', 'Type', 'Addr', 'Capacity'))
                print("{0:^105}".format(tableHeader))
                for row in inputDict['optionDisplay']:
                    rowWise = ("{0:^5}{1:^15}{2:^15}{3:^15}{4:^15}".format(row[0], row[1], row[3], row[4], row[5]))
                    print('{:^105}'.format(rowWise))
                print('-' * 105)
                # navigation panel

            elif isinstance(inputDict['optionDisplay'], tuple) and inputDict['state'] == 5:
                tableHeader = ("{0:^5}{1:^15}{2:^15}{3:^15}{4:^15}{5:^15}".format('ID', 'Venue', 'Tariff/day', 'Function Type', 'Address', 'Capacity'))
                print("{0:^105}".format(tableHeader))
                # for value in optionDisplay:
                tempString = ("{0:^5}{1:^15}{2:^15}{3:^15}{4:^15}{5:^15}".format(inputDict['optionDisplay'][0], inputDict['optionDisplay'][1], inputDict['optionDisplay'][3], inputDict['optionDisplay'][4], inputDict['optionDisplay'][5], inputDict['optionDisplay'][6]))
                print('{:^105}'.format(tempString))
                print('-' * 105)
            #for display of booking
            # elif isinstance(inputDict['optionDisplay'], tuple) and inputDict['state'] == 9:
            #     tableHeader = ("{0:^5}{1:^20}{2:^20}{3:^15}{4:^15}{5:^15}".format('ID', 'Start-Date', 'End-Date', 'Hall ID', 'Status', 'Amount Paid'))
            #     print("{0:^105}".format(tableHeader))
            #     # for value in optionDisplay:
            #     tempString = ("{0:^5}{1:^15}{2:^15}{3:^15}{4:^15}{5:^15}".format(inputDict['optionDisplay'][0], inputDict['optionDisplay'][1], inputDict['optionDisplay'][2], inputDict['optionDisplay'][3], inputDict['optionDisplay'][5], inputDict['optionDisplay'][6]))
            #     print('{:^105}'.format(tempString))
            #     print('-' * 105)

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

    def selectOption(self, optionDisplay, pageNavDict):
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

    def navOptions(self, selection, state):
        """

        :param selection:
        :type state: object
        """
        if selection == 'O':
            state = 1
        elif selection == 'E':
            state = 0
        return state

    def calculateQuote(self, sDate,eDate,hallId):
        hallObj = Hall({'hallId': hallId,})
        rate = hallObj.getDayTariff()
        deltaDate = eDate - sDate
        numberOfDays = deltaDate.days
        # hallObj = Hall(hallId)
        # hallObj.getDa()
        return rate * numberOfDays

    def acceptDate(self, startDate = None):
        if startDate == None:
            try:
                dateStr = input('Enter start date of booking (DD/MM/YYYY): ')
                dateList = dateStr.split('/')
                dateObj = datetime.date(int(dateList[2]), int(dateList[1]), int(dateList[0]))
                return True, dateObj
            except ValueError as errorInfo:
                return False, errorInfo
            except TypeError as errorInfo:
                return False, errorInfo
        else:
            try:
                dateStr = input('Enter end date of booking (DD/MM/YYYY): ')
                dateList = dateStr.split('/')
                dateObj = datetime.date(int(dateList[2]), int(dateList[1]), int(dateList[0]))
                return True, dateObj
            except ValueError as errorInfo:
                return False, errorInfo
            except TypeError as errorInfo:
                return False, errorInfo
            finally:
                if dateObj < startDate:
                    errorInfo = 'End date cannot be before begin date!!!'
                    return False, errorInfo
                else:
                    return True, dateObj

    def customerController(self, userObj):
        """This method contains all functionality related to the customer"""
        state = 2
        while state >= 2:
            #display option to view all halls or search specific hall
            while state == 2:
                pageName = 'Customer Home Screen'
                userName = userObj.getFirstName()
                optionDisplay = {'1': 'View Halls', '2': 'Search Hall', '3': 'Book Hall', '4': 'View Quotation Requests', '5': 'View Bookings'}
                pageNavDict = {'O': 'Logout', 'E': 'Exit'}
                # footerDisplay = footerDisplay
                # state = state
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
                        state = 4
                    elif selection == '3':
                        state = 7
                    elif selection == '4':
                        state = 7
                    elif selection == '5':
                        state = 9
                else:
                    print('Invalid selection, Please input again')

            #display list of halls and provide selection option
            while state == 3:
                headerDisplay = 'Input key to select corresponding option'
                pageName = 'View All Halls'
                userName = userObj.getFirstName()
                optionDisplay = Hall.viewAllHalls()
                pageNavDict = {'B': 'Go Back', 'O': 'Logout', 'E': 'Exit'}
                # footerDisplay = footerDisplay
                # state = state
                # headerDisplay = headerDisplay
                displayDict = {'pageName': pageName, 'userName': userName, 'optionDisplay': optionDisplay, 'pageNavDict': pageNavDict, 'state': state , 'headerDisplay': headerDisplay}
                # tableHeader =
                self.displayPage(displayDict)
                invalidSelectionFlag, selection = self.selectOption(optionDisplay, pageNavDict)
                if not invalidSelectionFlag:
                    if selection in pageNavDict:
                        if selection == 'B':
                            state = 2
                        else:
                            state = self.navOptions(selection, state)
                    else:
                        state = 5
                        index = selection
                else:
                    print('Invalid selection, Please input again')

            #display hall details of the hall id entered
            while state == 4:
                # pageName = pageName
                # userName = userName
                # optionDisplay = optionDisplay
                # pageNavDict = pageNavDict
                # message = message
                # state = state
                # headerDisplay = headerDisplay
                hallList = Hall.viewAllHalls()
                navPageDict = {'B': 'Go Back', 'O': 'Logout', 'E': 'Exit'}
                # placeHolder = dict()
                print('Search hall by hall id ')
                invalidSelectionFlag, selection = self.selectOption(hallList, navPageDict)
                if not invalidSelectionFlag:
                    if selection in navPageDict:
                        if selection == 'B':
                            state = 2
                        else:
                            state = self.navOptions(selection, state)
                    else:
                        state = 5
                        index = selection
                        print(type(index), 'and value ',index)
                        input('index set to selection and state changed to 5')
                else:
                    print('Invalid selection, Please input again')

            #intermediary state not to be jumped onto
            while state == 5:
                pageName = 'Hall Details'
                userName = userObj.getFirstName()
                optionDisplay = Hall.viewHallDetails(index)
                pageNavDict = {'R': 'Request Quote', 'B': 'Go Back', 'O': 'Logout', 'E': 'Exit'}
                hallDetails = Hall.viewHallDetails(index)
                navPageDict = {'R': 'Request Quote', 'B': 'Go Back', 'O': 'Logout', 'E': 'Exit'}
                displayDict = {'pageName': pageName, 'userName': userName, 'optionDisplay': optionDisplay, 'pageNavDict': pageNavDict, 'state': state}
                self.displayPage(displayDict)
                placeHolder = dict()
                invalidSelectionFlag, selection = self.selectOption(placeHolder, pageNavDict)
                if not invalidSelectionFlag:
                    if selection in pageNavDict:
                        if selection == 'R':
                            state = 6
                        if selection == 'B':
                            state = 3
                        else:
                            state = self.navOptions(selection, state)
                else:
                    strDebug = 'Break with status: '+str(state)+' and selection: '+str(selection)
                    input(strDebug)
                    print('Invalid selection, Please input again')

            while state == 6:
                # pageName = pageName
                # userName = userName
                # optionDisplay = optionDisplay
                # pageNavDict = pageNavDict
                # message = message
                # state = state
                # headerDisplay = headerDisplay
                quotationInfo = dict()
                quotationInfo['reqDate'] = datetime.datetime.now()
                dateCounter = 3
                #accept date from user for booking start date
                while dateCounter > 0:
                    dateFlag, dateObj = self.acceptDate()
                    if dateFlag:
                        quotationInfo['bookingStartDate'] = dateObj
                        break
                    else:
                        dateCounter = dateCounter - 1
                        print(dateObj,', please try again')
                else:
                    print('Maximum retry reached, navigating back')
                    state = self.navOptions('B', state)
                #accept date from user for booking end date
                dateCounter = 3
                while dateCounter > 0:
                    dateFlag, dateObj = self.acceptDate(quotationInfo['bookingStartDate'])
                    if dateFlag:
                        quotationInfo['bookingEndDate'] = dateObj
                        break
                    else:
                        dateCounter = dateCounter - 1
                        print(dateObj,', please try again')
                else:
                    print('Maximum retry reached, navigating back')
                    state = self.navOptions('B', state)
                quotationInfo['hallId'] = index
                quotationInfo['customerId'] = userObj.getRowId()
                quotationInfo['quotationAmount'] = self.calculateQuote(quotationInfo['bookingStartDate'], quotationInfo['bookingEndDate'], quotationInfo['hallId'])
                print('Charge for booking from {} to {} is {}.'.format(quotationInfo['bookingStartDate'].isoformat(),quotationInfo['bookingEndDate'].isoformat(),quotationInfo['quotationAmount']))
                customerConfirmCounter = 3
                while customerConfirmCounter > 0:
                    confirmation = input('Confirm Quotation Request(Y/N): ')
                    if confirmation.isalpha():
                        if confirmation.lower() == 'y':
                            #create object of quotations
                            quotationObj = Quotation(quotationInfo)
                            state = 7
                            break
                        elif confirmation.lower() == 'n':
                            print('Taking back to previous menu')
                            time.sleep(2)
                            state = 5
                            break
                        else:
                            print('Invalid input!! Try again')
                            customerConfirmCounter = customerConfirmCounter - 1
                    else:
                        print('Invalid input!! Try again')
                        customerConfirmCounter = customerConfirmCounter - 1
                if customerConfirmCounter == 0:
                    print('Maximum Taking back to previous menu')
                    time.sleep(2)
                    state = self.navOptions('B', state)

            #display all quotation requests made by the customer
            while state == 7:
                pageName = 'Quotation Requests'
                userName = userObj.getFirstName()
                optionDisplay = Quotation.listQuotationRequests(userObj.getRowId())
                pageNavDict = {'B': 'Go Back', 'O': 'Logout', 'E': 'Exit'}
                headerDisplay = 'Select an ID to make a booking'
                footerDisplay = 'Booking can be made only for approved requests'
                displayDict = {'pageName': pageName, 'userName': userName, 'optionDisplay': optionDisplay, 'pageNavDict': pageNavDict, 'state': state, 'headerDisplay': headerDisplay, 'footerDisplay': footerDisplay}
                self.displayPage(displayDict)
                placeholder = dict()
                invalidSelectionFlag, selection = self.selectOption(optionDisplay, pageNavDict)
                if not invalidSelectionFlag:
                    if selection in pageNavDict:
                        if selection == 'B':
                            state = 2
                        else:
                            state = self.navOptions(selection, state)
                    else:
                        quotationObj = Quotation({'quotationId': selection})
                        if quotationObj.getStatus() == 'Approved':
                            state = 8
                        elif quotationObj.getStatus() == 'Pending':
                            print('Quotation ID {} is pending at Owner'.format(quotationObj.getQuotationId()))
                            time.sleep(2)
                            state = 7
                        else:
                            print('Quotation ID {} is rejected by Owner'.format(quotationObj.getQuotationId()))
                            time.sleep(2)
                            state = 7
                else:
                    print('Invalid selection, Please input again')
                    time.sleep(2)

            while state == 8:
                """bookingInfo['bookingStartDate','bookingEndDate','hallId','customerId','bookingAmount','quotationId']"""
                # pageName = pageName
                # userName = userName
                # optionDisplay = optionDisplay
                # pageNavDict = pageNavDict
                # message = message
                # state = state
                # headerDisplay = headerDisplay
                bookingInfo = {'bookingStartDate': quotationObj.getBookingStartDate(),'bookingEndDate': quotationObj.getBookingEndDate(),'hallId': quotationObj.getHallId(), 'customerId': quotationObj.getCustomerId(),'bookingAmount': quotationObj.getQuotationAmount(),'quotationId': quotationObj.getQuotationId()}
                optionDisplay = bookingInfo
                pageName = 'Book Hall'
                userName = userObj.getFirstName()
                pageNavDict = {'P': 'Make Payment', 'B': 'Go Back', 'O': 'Logout', 'E': 'Exit'}
                footerDisplay = 'Make payment and complete the booking'
                # state = state
                # headerDisplay = headerDisplay
                displayDict = {'footerDisplay': footerDisplay, 'pageName': pageName, 'userName': userName, 'optionDisplay': optionDisplay, 'pageNavDict': pageNavDict, 'state': state}
                # tableHeader =
                self.displayPage(displayDict)
                placeHolder = dict()
                invalidSelectionFlag, selection = self.selectOption(placeHolder, pageNavDict)
                if not invalidSelectionFlag:
                    if selection in pageNavDict:
                        if selection == 'B':
                            state = 7
                        elif selection == 'P':
                            input('Press enter to make payment')
                            bookingObj = Booking(bookingInfo)
                            state = 9
                        else:
                            state = self.navOptions(selection, state)
                else:
                    print('Invalid selection, Please input again')

            while state == 9:
                optionDisplay = Booking.viewUserBookings(userObj)
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
                            state = 7
                        else:
                            state = self.navOptions(selection, state)
                else:
                    print('Invalid selection, Please input again')

        self.state = state
