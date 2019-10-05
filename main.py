from controller import *
from user.user import *
from hall.hall import *
from controller import Session
def navOptions(selection, state):
    if selection == 'O':
        state = 1
    elif selection == 'B':
        state = state - 1 
    return state


def main():
    adminPage = {'1':'Manager Users/Owners','2':'Hall Listing','3':'Manage Discounts'}
    registerPage = {'F':'First Name', 'L': 'Last Name', 'E': 'Email', 'P': 'Password'}
    customerPage = {'1':'Search Halls','2':'Manager Bookings'}
    ownerPage = {'1':'Manager Halls','2':'Manage Bookings','3':'View Quotation Request','4':'Manage Payments','5':'Manage Discounts'}
    navPageDict = {'O': 'Logout', 'B': 'Go Back'}
    state = 1
    onFlag = True
    print(onFlag)
    while onFlag:
        while state == 1: 
            os.system('clear')
            landingPage = {'L': 'Login', 'O': 'Register as Owner', 'C': 'Register as Customer'}
            navPageDict = {'E' : 'Exit'}
            userNamePlaceHolder = ''
            displayPage('Login Page', userNamePlaceHolder, landingPage, navPageDict)
            invalidSelectionFlag, selection = selectOption(landingPage, navPageDict)
            if not invalidSelectionFlag:
                if selection == 'O':
                    fName,lName,email,passHash = acceptUserDetails()
                    #create a user object
                    userObj = Owner(fName,lName,email,passHash)
                    #initiate a session using user object 
                    sessionObj = Session(userObj.getRowId(), userObj.getUserType())
                    print(sessionObj.getSessionId())
                    state = 2
                    #print(owner.getRowId())
                elif selection == 'C':
                    fName,lName,email,passHash = acceptUserDetails()
                    userObj = Customer(fName,lName,email,passHash)
                    userId = userObj.getRowId()
                    userType = userObj.getUserType()
                    firstName = userObj.getFirstName()
                    print(userId)
                    state = 2
                    #print(customer.getRowId())
                elif selection == 'L':
                    userId, firstName, userType, allowFlag = userLogin()
                    if allowFlag == 0:
                        state = 2
                    else:
                        print('User blocked')
                        time.sleep(2)
                        state = 1
                elif selection == 'E':
                    exit()
            else:
                print('Invalid selection, Please input again')

        print('UserType',userType)
        time.sleep(2)
        while state == 2 and userType == 'Customer':
            displayPage('Customer Page', firstName, customerPage, navPageDict)
            invalidSelectionFlag, selection = selectOption(landingPage, navPageDict)
            selection = displayPage('Customer Page', firstName, customerPage, navPageDict)
            state = navOptions(selection, state)
            #print(selection,state)
            #time.sleep(4)
            if selection == '1':
                allEntries = Hall.viewAllHalls()
                print(allEntries)
                time.sleep(4)
                selection = displayPage('Customer Page', firstName, customerPage, navPageDict)
                state = navOptions(selection, state)

#                for startIndex in range(0,len(allEntries),4):
 #                   displayTableFormat(allEntries,startIndex)
                    

        while state == 2 and userType == 'Owner':
            selection = displayPage('Owner Page', firstName, ownerPage, navPageDict)
            state = navOptions(selection, state)

        while state == 2 and userType == 'Admin':
            selection = displayPage('Admin Page', firstName, adminPage, navPageDict)
            state = navOptions(selection, state)


































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

