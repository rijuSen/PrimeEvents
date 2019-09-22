from controller import *
from user.user import *
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import time
def acceptUserDetails():
    fName = input('Enter First Name: ')
    lName = input('Enter Last Name: ')
    mailFlag = True 
    while mailFlag:
        email = input('Enter Email Id: ')
        mailFlag = Owner.emailExists(email)
        if mailFlag == True:
            print("Mail id already used, try another mail id")
            time.sleep(2)

    #check password length more than or equal to 8
    passFlag = True
    while passFlag:
        passPlain = input('Enter Password(must be >= 8): ')
        if len(passPlain) >= 8:
            passFlag = False
            print("Password must have 8 or more characters")
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(bytes(passPlain, 'utf-8'))
    passHash = digest.finalize()
    print(passHash)
    return fName,lName,email,passHash 


def main():
    adminPage = {'0':'Logout','1':'Manager Users/Owners','2':'Hall Listing','3':'Manage Discounts'}
    landingPage = {'L': 'Login', 'O': 'Register as Owner', 'C': 'Register as Customer'}
    registerPage = {'F':'First Name', 'L': 'Last Name', 'E': 'Email', 'P': 'Password'}
    navPageDict = {'O': 'Logout', 'B': 'Go Back'}
    state = 1
    if state == 1:
        navPlaceHolder = dict()
        selection = displayPage('Home Page', landingPage, navPlaceHolder)
        if selection == 'O':
            fName,lName,email,passHash = acceptUserDetails()
            owner = Owner(fName,lName,email,passHash)
            print(owner.getRowId())
        elif selection == 'C':
            fName,lName,email,passHash = acceptUserDetails()
            customer = Customer(fName,lName,email,passHash)
            print(customer.getRowId())
































#   ownerPage = {'0':'Logout','1':'Manager Halls','2':'Manage Bookings','3':'View Quotation Request','4':'Manage Payments','5':'Manage Discounts'}
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

