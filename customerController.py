import os
import time
import datetime
from hall.hall import Hall
from quotation.quotation import Quotation


def displayPage(pageName, userName, optionDisplay, pageNavDict, message = None):
    """if userName exists then will be displayed on selectOption
    if optionDisplay exists then display
        if optionDisplay is a dict display as dict
        if optionDisplay is a list display as list"""
    os.system('clear')
    # Display Page Name
    print('-' * 65)
    print('{0:^65}'.format(pageName))
    print('-' * 65)
    # Display User Name
    if not len(userName) == 0:
        print('{0:^65}'.format('Logged in as ' + userName.capitalize()))
        print('-' * 65)
    if not len(optionDisplay) == 0:
        if isinstance(optionDisplay, dict):
            # Menu Options format
            print('{:^65}'.format('Input key to select corresponding option'))
            print('-' * 65)
            tempString = '{0:^5}{1:^30}'.format('[Keys]', 'Options')
            print('{:^65}'.format(tempString))
            print('-' * 65)
            # display menu
            for key, option in optionDisplay.items():
                tempString = '{0:^5}{1:^30}'.format('['+ key +']', option)
                print('{:^65}'.format(tempString))
                # print('{0:>4}{1}{2:<5}{3:^30}'.format('[', key, ']', option))
            print('-' * 65)
            # navigation panel
        if isinstance(optionDisplay, list):
            # print("Its a list")
            # time.sleep(2)
            # Menu Options format
            print('{:^65}'.format('Input key to select corresponding option'))
            print('-' * 65)
            # display menu
            tableHeader = ("{0:^5}{1:^15}{2:^15}{3:^15}{4:^15}".format('Key', 'Venue', 'Type', 'Addr', 'Capacity'))
            print("{0:^65}".format(tableHeader))
            for row in optionDisplay:
                rowWise = ("{0:^5}{1:^15}{2:^15}{3:^15}{4:^15}".format(row[0], row[1], row[3], row[4], row[5]))
                print('{:^65}'.format(rowWise))
            print('-' * 65)
            # navigation panel

        if isinstance(optionDisplay, tuple):
            # print("Its a list")
            # time.sleep(2)
            # Menu Options format
            # print('Input key to select corresponding option')
            # print('-' * 65)
            # display menu
            tableHeader = ("{0:^5}{1:^15}{2:^15}{3:^15}{4:^15}".format('Key', 'Venue', 'Type', 'Addr', 'Capacity'))
            print("{0:^65}".format(tableHeader))
            # tempList = str(optionDisplay).split(',')
            # print(tempList)
            # for value in optionDisplay:
            tempString = ("{0:^5}{1:^15}{2:^15}{3:^15}{4:^15}".format(optionDisplay[0], optionDisplay[1], optionDisplay[3], optionDisplay[4], optionDisplay[5]))
            print('{:^65}'.format(tempString))
            print('-' * 65)
        if not message == None:
            print('{0:^65}'.format(message))
            print('-' * 65)
            # navigation panel
    if not len(pageNavDict) == 0:
        navBar = ''
        for key, option in pageNavDict.items():
            navBarTemp = '{:^11}'.format('[' + key + ']' + option)
            navBar = navBar + navBarTemp
        print('{:^65}'.format(navBar))
        print('-' * 65)


def selectOption(optionDisplay, pageNavDict):
    """selection made is from either dictionary keys or list indices
    return true and null string if invalid selection made and
    return false and selection in appropriate format if valid selection is made"""
    # prompt user to select option
    selection = input('Enter your selection: ')
    if isinstance(optionDisplay, dict) and selection in optionDisplay.keys():
        print('Your selection: {}'.format(optionDisplay.get(selection)))
        return False, selection
    elif isinstance(optionDisplay, list) and selection.isdigit() and int(selection) <= len(optionDisplay):
        print('Your selection: {}'.format(optionDisplay[int(selection)]))
        return False, selection
    elif selection in pageNavDict.keys():
        print('Your selection: {}'.format(pageNavDict.get(selection)))
        return False, selection
    else:
        print('Selection {} is not a valid. Kindly provide a valid selection'.format(selection))
        time.sleep(2)
        return True, ''


def navOptions(selection, state):
    """

    :param selection:
    :type state: object
    """
    if selection == 'O':
        state = 1
    elif selection == 'B':
        state = state - 1
    elif selection == 'E':
        state = 0
    return state

def calculateQuote(sDate,eDate,hallId):
    # hallObj = Hall(hallId)
    # hallObj.getDa()
    return 2000

def acceptDate(startDate = None):
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



def customerController(userObj):
    """This method contains all functionality related to the customer"""
    state = 2
    while state >= 2:
        #display option to view all halls or search specific hall
        while state == 2:
            customerPage = {'1': 'View Halls', '2': 'Search Hall', '3': 'Book Hall', '4': 'Request Quotation'}
            navPageDict = {'O': 'Logout', 'E': 'Exit'}
            message = 'Halls can be booked only if quotation request is accepted'
            displayPage('Customer Page', userObj.getFirstName(), customerPage, navPageDict, message)
            invalidSelectionFlag, selection = selectOption(customerPage, navPageDict)
            # for navigation menu
            if not invalidSelectionFlag:
                if selection in navPageDict:
                    state = navOptions(selection, state)
                elif selection == '1':
                    # take to next state to display hall listing
                    state = 3
                elif selection == '2':
                    state = 4
                elif selection == '4':
                    state = 6
            else:
                print('Invalid selection, Please input again')

        #display list of halls and provide selection option
        while state == 3:
            hallList = Hall.viewAllHalls()
            # print('Log message viewAllHalls:', type(hallList), len(hallList))
            # time.sleep(3)
            navPageDict = {'B': 'Go Back', 'O': 'Logout', 'E': 'Exit'}
            displayPage('View Halls', userObj.getFirstName(), hallList, navPageDict)
            invalidSelectionFlag, selection = selectOption(hallList, navPageDict)
            if not invalidSelectionFlag:
                if selection in navPageDict:
                    state = navOptions(selection, state)
                else:
                    state = 5
            else:
                print('Invalid selection, Please input again')

        #display hall details of the hall id entered
        while state == 4:
            hallList = Hall.viewAllHalls()
            navPageDict = {'B': 'Go Back', 'O': 'Logout', 'E': 'Exit'}
            invalidSelectionFlag, selection = selectOption(hallList, navPageDict)
            if not invalidSelectionFlag:
                if selection in navPageDict:
                    state = navOptions(selection, state)
                else:
                    state = 5
            else:
                print('Invalid selection, Please input again')

        while state == 5:
            #hallID = input("Enter Hall ID: ")
            index = int(selection)
            hallDetails = Hall.viewHallDetails(index)
            # print(hallDetails)
            # print(type(hallDetails))
            # time.sleep(2)
            #displayPage('Hall Details', userObj.getFirstName(), hallDetails, navPageDict)
            # tableHeader = ("{0:^10}{1:^10}{2:^10}{3:^10}".format('Venue', 'Type', 'Addr', 'Capacity'))
            # print("{}".format(tableHeader))
            # print("{0:^10}{1:^10}{2:^10}{3:^10}".format(hallDetails[0], hallDetails[2], hallDetails[3], hallDetails[4]))
            #print('{:^65}'.format(displayFormat))
            navPageDict = {'R': 'Request Quote', 'B': 'Go Back', 'O': 'Logout', 'E': 'Exit'}
            #placeholder dictionary
            bookHallPage = dict()
            # print
            # tempString = '{}\n Venue - {} Type - {} Addr - {} Capacity - {}'.format(userObj.getFirstName(), hallDetails[0], hallDetails[2], hallDetails[3], hallDetails[4])
            displayPage('Hall Details', userObj.getFirstName(), hallDetails, navPageDict)
            invalidSelectionFlag, selection = selectOption(bookHallPage, navPageDict)
            if not invalidSelectionFlag:
                if selection in navPageDict:
                    if selection == 'R':
                        state = 6
                    else:
                        state = navOptions(selection, state)
            else:
                print('Invalid selection, Please input again')

        while state == 6:
            quotationInfo = dict()
            quotationInfo['reqDate'] = datetime.datetime.now()
            dateCounter = 3
            #accept date from user for booking start date
            while dateCounter > 0:
                dateFlag, dateObj = acceptDate()
                if dateFlag:
                    quotationInfo['bookingStartDate'] = dateObj
                    break
                else:
                    dateCounter = dateCounter - 1
                    print(dateObj,', please try again')
            else:
                print('Maximum retry reached, navigating back')
                state = navOptions('B', state)
            #accept date from user for booking end date
            dateCounter = 3
            while dateCounter > 0:
                dateFlag, dateObj = acceptDate(quotationInfo['bookingStartDate'])
                if dateFlag:
                    quotationInfo['bookingEndDate'] = dateObj
                    break
                else:
                    dateCounter = dateCounter - 1
                    print(dateObj,', please try again')
            else:
                print('Maximum retry reached, navigating back')
                state = navOptions('B', state)
            quotationInfo['hallId'] = index
            quotationInfo['customerId'] = userObj.getRowId()
            quotationInfo['quotationAmount'] = calculateQuote(quotationInfo['bookingStartDate'], quotationInfo['bookingEndDate'], quotationInfo['hallId'])
            print('Charge for booking from {} to {} is {}.'.format(quotationInfo['bookingStartDate'].isoformat(),quotationInfo['bookingEndDate'].isoformat(),quotationInfo['quotationAmount']))
            customerConfirmCounter = 3
            while customerConfirmCounter > 0:
                confirmation = input('Confirm Quotation Request(Y/N): ')
                if confirmation.isalpha():
                    if confirmation.lower() == 'y':
                        #create object of quotations
                        state = 7
                        break
                    elif confirmation.lower() == 'n':
                        print('Taking back to previous menu')
                        state = navOptions('B', state)
                    else:
                        print('Invalid input!! Try again')
                        customerConfirmCounter = customerConfirmCounter - 1
                else:
                    print('Invalid input!! Try again')
                    customerConfirmCounter = customerConfirmCounter - 1
            if customerConfirmCounter == 0:
                print('Maximum Taking back to previous menu')
                state = navOptions('B', state)

        while state == 7:
            quotationObj = Quotation(quotationInfo)
            quotationList = Quotation.listQuotationRequests(userObj.getRowId())
            print(type(quotationList))
            time.sleep(3)
            displayPage('Quotation Requests', userObj.getFirstName(), quotationList, navPageDict)
            placeholder = dict()
            navPageDict = {'B': 'Go Back', 'O': 'Logout', 'E': 'Exit'}
            invalidSelectionFlag, selection = selectOption(placeholder, navPageDict)
            if not invalidSelectionFlag:
                if selection in navPageDict:
                    state = navOptions(selection, state)
                    state = state - 1
            else:
                print('Invalid selection, Please input again')

            # print('Booked')
            # exit()

    return state
