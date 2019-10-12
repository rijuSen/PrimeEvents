import os
import time
from hall.hall import Hall


def displayPage(pageName, userName, optionDisplay, pageNavDict):
    """if userName exists then will be displayed on selectOption
    if optionDisplay exists then display
        if optionDisplay is a dict display as dict
        if optionDisplay is a list display as list"""
    os.system('clear')
    # Display Page Name
    print('-' * 45)
    print('{0:^45}'.format(pageName))
    print('-' * 45)
    # Display User Name
    if not len(userName) == 0:
        print('{0:^45}'.format('Logged in as ' + userName.capitalize()))
        print('-' * 45)
    if not len(optionDisplay) == 0:
        if isinstance(optionDisplay, dict):
            # Menu Options format
            print('{:^45}'.format('Input key to select corresponding option'))
            print('-' * 45)
            print('{0:^10}{1:^30}'.format('[Keys]', 'Options'))
            print('-' * 45)
            # display menu
            for key, option in optionDisplay.items():
                print('{0:>4}{1}{2:<5}{3:^30}'.format('[', key, ']', option))
            print('-' * 45)
            # navigation panel
            print('-' * 45)
        if isinstance(optionDisplay, list):
            # Menu Options format
            print('Input key to select corresponding option')
            print('-' * 45)
            # display menu
            tableHeader = ("{0:^5}{1:^10}{2:^10}{3:^10}{4:^10}".format('Key', 'Venue', 'Type', 'Addr', 'Capacity'))
            print("{0:^45}".format(tableHeader))
            for row in optionDisplay:
                rowWise = ("{0:^5}{1:^10}{2:^10}{3:^10}{4:^10}".format(row[0], row[1], row[3], row[4], row[5]))
                print('{:^45}'.format(rowWise))
            print('-' * 45)
            # navigation panel
            print('-' * 45)
    if not len(pageNavDict) == 0:
        navBar = ''
        for key, option in pageNavDict.items():
            navBarTemp = '{:^11}'.format('[' + key + ']' + option)
            navBar = navBar + navBarTemp
        print('{:^45}'.format(navBar))
    print('-' * 45)


def selectOption(optionDisplay, pageNavDict):
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


def customerController(userObj):
    """This method contains all functionality related to the customer"""
    state = 2
    while state == 2:
        customerPage = {'1': 'View Halls'}
        navPageDict = {'O': 'Logout', 'E': 'Exit'}
        displayPage('Customer Page', userObj.getFirstName(), customerPage, navPageDict)
        invalidSelectionFlag, selection = selectOption(customerPage, navPageDict)
        # for navigation menu
        if not invalidSelectionFlag:
            if selection in navPageDict:
                state = navOptions(selection, state)
            else:
                # take to next state to display hall listing
                state = 3
        else:
            print('Invalid selection, Please input again')
    #display list of halls and provide selection option
    while state == 3 and selection == '1':
        hallList = Hall.viewAllHalls()
        navPageDict = {'B': 'Go Back', 'O': 'Logout', 'E': 'Exit'}
        displayPage('View Halls', userObj.getFirstName(), hallList, navPageDict)
        invalidSelectionFlag, selection = selectOption(hallList, navPageDict)
        if not invalidSelectionFlag:
            if selection in navPageDict:
                state = navOptions(selection, state)
            else:
                state = 4
        else:
            print('Invalid selection, Please input again')

    while state == 4:
        #hallID = input("Enter Hall ID: ")
        index = int(selection)
        hallDetails = Hall.viewHallDetails(index)
        #print(hallDetails)
        #displayPage('Hall Details', userObj.getFirstName(), hallDetails, navPageDict)
        # tableHeader = ("{0:^10}{1:^10}{2:^10}{3:^10}".format('Venue', 'Type', 'Addr', 'Capacity'))
        # print("{}".format(tableHeader))
        # print("{0:^10}{1:^10}{2:^10}{3:^10}".format(hallDetails[0], hallDetails[2], hallDetails[3], hallDetails[4]))
        #print('{:^45}'.format(displayFormat))
        navPageDict = {'B': 'Go Back', 'O': 'Logout', 'E': 'Exit'}
        bookHallPage = {'R': 'Request Quotation'}
        tempString = '{}\n Venue - {} Type - {} Addr - {} Capacity - {}'.format(userObj.getFirstName(), hallDetails[0], hallDetails[2], hallDetails[3], hallDetails[4])
        displayPage('Hall Details', '{:^45}'.format(tempString), bookHallPage, navPageDict)
        invalidSelectionFlag, selection = selectOption(bookHallPage, navPageDict)
        if not invalidSelectionFlag:
            if selection in navPageDict:
                state = navOptions(selection, state)
            else:
                state = 5
        else:
            print('Invalid selection, Please input again')
    while state == 5 and selection == 'R':
        print('Booked')
        exit()

    return state
