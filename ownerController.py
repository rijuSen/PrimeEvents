import os
import time
from hall.hall import Hall

def displayPage(pageName, userName, optionDisplay, pageNavDict):
    os.system('clear')
    #Display Page Name
    print('-'*45)
    print('{0:^45}'.format(pageName))
    print('-'*45)
    #Display User Name
    if not len(userName) == 0:
        print('{0:^45}'.format('Logged in as '+userName.capitalize()))
        print('-'*45)
    if not len(optionDisplay) == 0:
        if isinstance(optionDisplay,dict):
            #Menu Options format
            print('{:^45}'.format('Input key to select corresponding option'))
            print('-'*45)
            print('{0:^10}{1:^30}'.format('[Keys]','Options'))
            print('-'*45)
            #display menu
            for key, option in optionDisplay.items():
                print('{0:>4}{1}{2:<5}{3:^30}'.format('[', key, ']', option))
            print('-'*45)
            #navigation panel
            print('-'*45)
        if isinstance(optionDisplay,list):
            #Menu Options format
            print('Input key to select corresponding option')
            print('-'*45)
            #display menu
            tableHeader = ("{0:^5}{1:^10}{2:^10}{3:^10}{4:^10}".format('Key','Venue','Type','Addr','Capacity'))
            print("{0:^45}".format(tableHeader))
            for row in optionDisplay:
                rowWise = ("{0:^5}{1:^10}{2:^10}{3:^10}{4:^10}".format(row[0],row[1],row[3],row[4],row[5]))
                print('{:^45}'.format(rowWise))
            print('-'*45)
            #navigation panel
            print('-'*45)
    if not len(pageNavDict) == 0:
        navBar = ''
        for key, option in pageNavDict.items():
            navBarTemp = '{:^11}'.format('['+key+']'+option)
            navBar = navBar + navBarTemp
        print('{:^45}'.format(navBar))
    print('-'*45)


def selectOption(optionDisplay,pageNavDict):
    #prompt user to select option
    selection = input('Enter your selection: ')
    if isinstance(optionDisplay, dict) and selection in optionDisplay.keys():
        print('Your selection: {}'.format(optionDisplay.get(selection)))
        return False, selection
    elif isinstance(optionDisplay, list) and selection.isdigit() and int(selection) <= len(optionDisplay):
        print('Your selection: {}'.format(optionDisplay[int(selection)-1]))
        return False, selection
    elif selection in pageNavDict.keys():
        print('Your selection: {}'.format(pageNavDict.get(selection)))
        return False, selection
    else:
        print('Selection {} is not a valid. Kindly provide a valid selection'.format(selection))
        time.sleep(2)
        return True, ''


def navOptions(selection, state):
    if selection == 'O':
        state = 1
    elif selection == 'B':
        state = state - 1
    elif selection == 'E':
        state = 0
    return state

def acceptHallDetails(userObj):
    os.system('clear')
    print('=' * 41)
    print('{:^41}'.format('New Hall Page'))
    print('=' * 41)
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
            hallInfo['hallType'] = input('Enter Hall Type: ')
            hallInfo['hallAddr'] = input('Enter Hall Addr: ')
            hallInfo['hallCapacity'] = input('Enter Hall Capacity: ')
            hallInfo['ownerId'] = userObj.getRowId()
    return hallExistFlag, hallInfo


def ownerController(userObj):
    """ This method contains all functionalities related to owner"""
    state = 2
    ownerPage = {'1': 'Manage Halls', '2': 'Manage Bookings', '3': 'View Quotation Request', '4': 'Manage Payments'}
    navPageDict = {'O': 'Logout', 'E': 'Exit', 'B': 'Back'}
    displayPage('Owner Page', userObj.getFirstName(), ownerPage, navPageDict)
    invalidSelectionFlag, selection = selectOption(ownerPage, navPageDict)
    # for navigation menu
    if not invalidSelectionFlag:
        if selection in navPageDict:
            state = navOptions(selection, state)
        else:
            # take to next state to display hall listing
            state = 3
    else:
        print('Invalid selection, Please input again')

    while state == 3 and selection == '1':
        hallslist = Hall.viewUserHalls(userObj)
        navPageDict = {'O': 'Logout', 'E': 'Exit', 'A': 'Add New Hall'}
        displayPage('Owner Page', userObj.getFirstName(), hallslist, navPageDict)
        invalidSelectionFlag, selection = selectOption(hallslist, navPageDict)
        # for navigation menu
        if not invalidSelectionFlag:
            if selection == 'A':
                hallExistFlag, hallInfo = acceptHallDetails(userObj)
                # create a user object
                if hallExistFlag:
                    state = 3
                else:
                    hallObj = Hall(hallInfo)
                    state = 4

            if selection in navPageDict:
                state = navOptions(selection, state)
            else:
                # take to next state to display hall listing
                state = 4
        else:
            print('Invalid selection, Please input again')

    return state
