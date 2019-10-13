import os
import time
from hall.hall import Hall

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
            tableHeader = ("{0:^5}{1:^15}{2:^10}{3:^10}{4:^15}{5:^10}".format('Key', 'Venue', 'Tariff','Type', 'Addr', 'Capacity'))
            print("{0:^65}".format(tableHeader))
            for row in optionDisplay:
                rowWise = ("{0:^5}{1:^15}{2:^10}{3:^10}{4:^15}{5:^10}".format(row[0], row[1], row[3], row[4], row[5], row[6]))
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
        print('Your selection: {}'.format(optionDisplay[int(selection) - 1]))
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

def acceptHallDetails(userObj):
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
            hallInfo['dayTariff'] = input('Enter Hall Per Day Tariff: ')
            hallInfo['hallType'] = input('Enter Hall Type: ')
            hallInfo['hallAddr'] = input('Enter Hall Addr: ')
            hallInfo['hallCapacity'] = input('Enter Hall Capacity: ')
            hallInfo['ownerId'] = userObj.getRowId()
    return hallExistFlag, hallInfo

def acceptModifyHallDetails(userObj, optionDisplay):
    os.system('clear')
    print('=' * 65)
    print('{:^65}'.format('New Hall Page'))
    print('=' * 65)
    tableHeader = ("{0:^5}{1:^15}{2:^15}{3:^15}{4:^15}".format('Key', 'Venue', 'Type', 'Addr', 'Capacity'))
    print("{0:^65}".format(tableHeader))
    tempString = ("{0:^5}{1:^15}{2:^15}{3:^15}{4:^15}".format(optionDisplay[0], optionDisplay[1], optionDisplay[3], optionDisplay[4], optionDisplay[5]))
    print('{:^65}'.format(tempString))
    print('-' * 65)
    hallInfo = dict()
    hallExistFlag = True
    retryCount = 0
    while hallExistFlag and retryCount < 3:
        hallInfo['hallName'] = input('Enter new Hall Name: ')
        hallExistFlag = Hall.hallExists(hallInfo['hallName'], userObj)
        retryCount = retryCount + 1
        if hallExistFlag == True and retryCount < 3:
            print("Hall already exists, try another Hall name")
        elif hallExistFlag == True and retryCount == 3:
            print('Maximum attemps reached, taking back to Manage Halls page')
            time.sleep(2)
        else:
            hallInfo['dayTariff'] = input('Enter new Hall Per Day Tariff: ')
            hallInfo['hallType'] = input('Enter new Hall Type: ')
            hallInfo['hallAddr'] = input('Enter new Hall Addr: ')
            hallInfo['hallCapacity'] = input('Enter new Hall Capacity: ')
            hallInfo['ownerId'] = userObj.getRowId()
    return hallExistFlag, hallInfo


def ownerController(userObj):
    """ This method contains all functionalities related to owner"""
    state = 2
    while state >= 2:
        while state == 2:
            ownerPage = {'1': 'Manage Halls', '2': 'Manage Bookings', '3': 'View Quotation Request', '4': 'Manage Payments'}
            navPageDict = {'O': 'Logout', 'E': 'Exit', 'B': 'Back'}
            displayPage('Owner Page', userObj.getFirstName(), ownerPage, navPageDict)
            invalidSelectionFlag, selection = selectOption(ownerPage, navPageDict)
            # for navigation menu
            if not invalidSelectionFlag:
                if selection in navPageDict:
                    state = navOptions(selection, state)
                elif selection == '1':
                    # take to next state to display hall listing
                    state = 3
                elif selection == '2':
                    state = 5
                elif selection == '4':
                    state = 6
            else:
                print('Invalid selection, Please input again')

        while state == 3:
                hallList = Hall.viewUserHalls(userObj)
                navPageDict = {'O': 'Logout', 'E': 'Exit', 'B': 'Back', 'A': 'Add New Hall'}
                displayPage('Manage Hall Page', userObj.getFirstName(), hallList, navPageDict)
                invalidSelectionFlag, selection = selectOption(hallList, navPageDict)
                # for navigation menu
                if not invalidSelectionFlag:
                    if selection == 'A':
                        hallExistFlag, hallInfo = acceptHallDetails(userObj)
                        # create a user object
                        if hallExistFlag:
                            state = 3
                        else:
                            hallObj = Hall(hallInfo)
                            state = 3
                    elif selection in navPageDict:
                        state = navOptions(selection, state)
                    else:
                        # take to next state to display hall listing
                        state = 4
                else:
                    print('Invalid selection, Please input again')

        while state == 4:
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
            navPageDict = {'M': 'Modify Hall', 'D': 'Delete Hall','B': 'Go Back', 'O': 'Logout', 'E': 'Exit'}
            #placeholder dictionary
            bookHallPage = dict()
            # print
            # tempString = '{}\n Venue - {} Type - {} Addr - {} Capacity - {}'.format(userObj.getFirstName(), hallDetails[0], hallDetails[2], hallDetails[3], hallDetails[4])
            displayPage('Hall Details', userObj.getFirstName(), hallDetails, navPageDict)
            invalidSelectionFlag, selection = selectOption(bookHallPage, navPageDict)
            if not invalidSelectionFlag:
                if selection in navPageDict:
                    if selection == 'M':
                        hallExistFlag, hallModify = acceptModifyHallDetails(userObj, hallDetails)
                        # create a user object
                        if hallExistFlag:
                            state = 3
                        else:
                            hallModify['Modify'] = True
                            hallObj = Hall(hallModify)
                            hallObj.modifyhall(hallDetails[0], hallModify)
                            state = 3
                        state = 3
                    elif selection == 'D':
                        hallDelete = dict()
                        hallDelete['requested'] = True
                        hallObj = Hall(hallDelete)
                        hallObj.deletehall(hallDetails[0])
                        state = 3
                    else:
                        state = navOptions(selection, state)
            else:
                print('Invalid selection, Please input again')

    return state
