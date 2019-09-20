#class for booking in prime events

class Booking:
    #to keep track of number of objects
    numOfUsers = 0
    #booking id to be generated
    bookingId = 0
    #payment id to be selected from payment
    paymentId = 0

    def __init__(self, hallId, userId, bookingDate, cateringChosen):
        self.hallId = hallId
        self.userId = userId
        self.bookingDate = bookingDate
        self.cateringChosen = cateringChosen
        Booking.numOfUsers += 1

    def getHallId(self):
        return self.hallId

    def getUserId(self):
        return self.userId

    def getBookingDate():
        return self.bookingDate

    def getCateringChosen():
        return self.cateringChosen

    def createBooking():
        #auto-generate booking id in the database on confirmation of payment
        #once booking id is fetched then booking entry is added in the database
        #get the existing sequence number and append 1 to it.
        pass

    def deleteBooking():
        pass

    def editBooking():
        #can't edit booking id
        pass

    def getBookingId():
        return self.bookingId
    
    def generateBookingId():
        #get booking id from database
        pass

    def generateReceipt():
        pass

    def selectPaymentMethod():
        #select from payment method in Payments
        pass

    def getNumOfUserObjectsCreated():
        return Booking.numOfUsers



