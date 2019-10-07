from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import time
import getpass
import os
from user.user import *
from hall.hall import *
from controller import Session

def navOptions(selection, state):
    if selection == 'O':
        state = 1
    elif selection == 'B':
        state = state - 1 
    elif selection == 'E':
        state = 0
    return state

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
            userInfo['password'] = getPass() 
    return mailExistFlag, userInfo 

def userLogin():
    loginFlag = False
    retryCount = 0
    while not loginFlag and retryCount < 3:
        userInfo = dict()
        userInfo['email'] = input('Enter Email Id: ')
        userInfo['password'] = getPass()
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
    return {'success':success,'userObj':userObj}


def displayTableFormat(listData, startIndex):
    print("{0:^5}{1:^10}{2:^10}{3:^10}{4:^10}".format('ID','Hall-Name','Hall-Type','Hall-Addr','Hall-Capacity'))
    for row in listData[startIndex:startIndex + 4:1]:
        print("{0:^5}{1:^10}{2:^10}{3:^10}{4:^10}".format(row[0],row[1],row[3],row[4],row[5]))


def main():
    adminPage = {'1':'Manager Users/Owners','2':'Hall Listing','3':'Manage Discounts'}
    registerPage = {'F':'First Name', 'L': 'Last Name', 'E': 'Email', 'P': 'Password'}
    ownerPage = {'1':'Manager Halls','2':'Manage Bookings','3':'View Quotation Request','4':'Manage Payments','5':'Manage Discounts'}
    state = 1
    onFlag = True
    print(onFlag)
    while state > 0:
        #state 1 represent login action
        while state == 1: 
            os.system('clear')
            landingPage = {'L': 'Login', 'O': 'Register as Owner', 'C': 'Register as Customer'}
            navPageDict = {'E' : 'Exit'}
            userNamePlaceHolder = ''
            displayPage('Login Page', userNamePlaceHolder, landingPage, navPageDict)
            invalidSelectionFlag, selection = selectOption(landingPage, navPageDict)
            if not invalidSelectionFlag:
                if selection == 'O':
                    mailExistFlag, userInfo = acceptUserDetails()
                    #create a user object
                    if mailExistFlag:
                        state = 1
                    else:
                        userObj = Owner(userInfo)
                        print('User info is {}'.format(userInfo))
                        time.sleep(2)
                        sessionObj = Session(userObj)
                        #print(sessionObj.getSessionId())
                        state = 2
                        print('State is {} and session ID is {} and user type is {}'.format(state,sessionObj.getSessionId(),sessionObj.getUserType()))
                        #print(owner.getRowId())
                elif selection == 'C':
                    mailExistFlag, userInfo = acceptUserDetails()
                    #create a user object
                    if mailExistFlag:
                        state = 1
                    else:
                        userObj = Customer(userInfo)
                        print('User info is {}'.format(userInfo))
                        time.sleep(2)
                        sessionObj = Session(userObj)
                        #print(sessionObj.getSessionId())
                        state = 2
                        #print(customer.getRowId())
                elif selection == 'L':
                    objDict = userLogin()
                    if objDict['success']:
                        if objDict['userObj'].getAllowFlag() == 0:
                            sessionObj = Session(objDict['userObj'])
                            state = 2
                        elif objDict['userObj'].getAllowFlag() == 1:
                            print('User blocked, redirecting to login page')
                            time.sleep(2)
                            state = 1
                elif selection == 'E':
                    exit()
            else:
                print('Invalid selection, Please input again')
        print('State is {} and session ID is {} and user type is {}'.format(state,sessionObj.getSessionId(),sessionObj.getUserType()))
        
        #state 2 represent actions post login
        while state == 2 and sessionObj.getUserType() == 'Customer':
            customerPage = {'1':'Search Halls','2':'Manager Bookings'}
            navPageDict = {'O': 'Logout', 'E': 'Exit'}
            displayPage('Customer Page', sessionObj.getFirstName(), customerPage, navPageDict)
            invalidSelectionFlag, selection = selectOption(customerPage, navPageDict)
            #for navigation menu
            if not invalidSelectionFlag:
                if selection in navPageDict:
                    state = navOptions(selection, state)
                else:
                    #take to next state to display hall listing
                    state = 3
            else:
                print('Invalid selection, Please input again')
        
        #state 3 is for hall listing for any user
        while state == 3 and selection == '1':
#            navPageDict = {'B': 'Go Back', 'N': 'Next Page', 'O': 'Logout', 'E': 'Exit'}
            navPageDict = {'B': 'Go Back', 'O': 'Logout', 'E': 'Exit'}
            allEntries = Hall.viewAllHalls()
            index = 0
            displayPage('Hall Listing', sessionObj.getFirstName(), allEntries, navPageDict)
            invalidSelectionFlag, selection = selectOption(allEntries, navPageDict)
            if not invalidSelectionFlag:
                if selection in navPageDict:
                    state = navOptions(selection, state)
                if selection.isdigit():
                    if int(selection) < len(allEntries) + 1:
                        print(allEntries[int(selection) + 1])
                        exit()


#            while index + 4 < len(allEntries):
#                displayPage('Hall Listing', sessionObj.getFirstName(), allEntries[index: index + 4] navPageDict)
#                invalidSelectionFlag, selection = selectOption(customerPage, navPageDict)
#                if not invalidSelectionFlag:
#                    if selection == 'B' and index == 0:
#                        state = navOptions(selection,state)
#                    elif selection == 'B' and index > 0:
#                        index = index - 4
#                        displayPage('Hall Listing', sessionObj.getFirstName(), allEntries[index:index + 4] navPageDict)
#                    elif selection == 'N'  and index + 4 < len(allEntries):
#                        displayPage('Hall Listing', sessionObj.getFirstName(), allEntries[index:index + 4] navPageDict)
#                        index = index + 4
#                    elif selection == 'N' and index + 4 > len(allEntries):
#                        displayPage('Hall Listing', sessionObj.getFirstName(), allEntries[index:] navPageDict)
#                    if selection in navPageDict:
#                        state = navOptions(selection, state)
#if selecti print('Yo')
            #exit()
        
        
#        while state == 3 and selection == '2':
#            pass
#
#
#
#                if selection == '1':
#                    navPageDict = {'B': 'Go Back', 'N': 'Next Page', 'O': 'Logout', 'E': 'Exit'}
#                    allEntries = Hall.viewAllHalls()
#                    index = 0
#                    displayTableFormat(allEntries, index)
#                    invalidSelectionFlag, selection = selectOption(customerPage, navPageDict)
#                    while not invalidSelectionFlag:
#                        if selection == 'B':
#                            break
#                        if selection == 'P':
#                            if index != 0:
#                                index = index - 4
#                                displayTableFormat(allEntries, index)
#                            else:
#                                pass
#
#
#                elif selection == 'E':
#                                    exit()
#            else:
#                print('Invalid selection, Please input again')
#            print('State is {} and session ID is {} and user type is {}'.format(state,sessionObj.getSessionId(),sessionObj.getUserType()))

                    #                for startIndex in range(0,len(allEntries),4):
                     #                   displayTableFormat(allEntries,startIndex)
                                        

#        while state == 2 and userType == 'Owner':
#            selection = displayPage('Owner Page', firstName, ownerPage, navPageDict)
#            state = navOptions(selection, state)
#
#        while state == 2 and userType == 'Admin':
#            selection = displayPage('Admin Page', firstName, adminPage, navPageDict)
#            state = navOptions(selection, state)
#
#
































       #    displayPage('OwnerHomePage',ownerPage)
    #    manageHallPage = {'0':'Go Back','1':'View Halls','2':'Create Hall'}
    #    displayPage('ManageHallPage',manageHallPage)
    #    createHallPage = {'0':'Go Back','1':'Enter Hall Name: ','2':'Enter Hall Capacity: ','3':'Enter Hall Size: ','4':'Enter Hall Location: '}
    #    displayPage('CreateHallPage',createHallPage)
    #    viewHallPage = {'0':'Go Back','1':'Hall 1','2':'Hall 2'}
    #    displayPage('ViewHallPage',viewHallPage)
    #    hallInfoPage = {'0':'Go Back','1':'View Discount','2':'Modify Hall', '3':'Delete Hall'}
    #    displayPage('HallInfoPage',hallInfoPage)
    #    modifyHallPage = {'0':'Go Back','1':'Modify Hall Name: ','2':'Modify Hall Capacity: ','3':'Modify Hall Size: ','4':'Modify Hall Location: '}
    #    displayPage('ModifyHallPage',modifyHallPage)
    #    discountInfoPage = {'0':'Go Back','1':'Edit Discount','2':'Delete Discount'}
    #    displayPage('DiscountInfoPage',discountInfoPage)
    #    editDiscountPage = {'0':'Go Back','1':'Modify Discount Value: '}
    #    displayPage('EditDiscountPage',editDiscountPage)
    #    deleteDiscountPage = {'0':'Go Back','1':'Confirm Yes','2':'Confirm No'}
    #    displayPage('DeleteDiscountPage',deleteDiscountPage)
    #    manageBookingPage = {'0':'Go Back','1':'Delete Booking: '}
    #    displayPage('ManageBookingPage',manageBookingPage)
    #    deleteBookingPage = {'0':'Go Back','1':'Confirm Yes','2':'Confirm No'}
    #    displayPage('DeleteBookingPage',deleteBookingPage)
    #    viewQuotationRequestPage = {'0':'Go Back','1':'Quotation 1','2':'Quotation 2'}
    #    displayPage('ViewQuotationRequestPage',viewQuotationRequestPage)
    #    quotationInfoPage = {'0':'Go Back','1':'Provide Quotation','2':'Accept', '3':'Reject'}
    #    displayPage('QuotationInfoPage',quotationInfoPage)
    #    provideQuotationPage = {'0':'Go Back','1':'Enter Quotation Amount: '}
    #    displayPage('ProvideQuotationPage',provideQuotationPage)
    #    managePaymentPage = {'0':'Go Back','1':'Payment 1','2':'Payment 2'}
    #    displayPage('ManagePaymentPage',managePaymentPage)
    #    paymentInfoPage = {'0':'Go Back','1':'Modify Payment Details: '}
    #    displayPage('PaymentInfoPage',paymentInfoPage)
    #    manageDiscountPage = {'0':'Go Back','1':'View Discount','2':'Create Discount'}
    #    displayPage('ManageDiscountPage',manageDiscountPage)
    #    createDiscountPage = {'0':'Go Back','1':'Enter Hall Name: ','2':'Enter Discount Percentage: '}
    #    displayPage('CreateDiscountPage',createDiscountPage)

if __name__=="__main__":
    main()

