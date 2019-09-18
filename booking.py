#class for booking in prime events

class Booking:

    def __init__(self, hallId, userId, bookingDate, cateringChosen):
        #booking id to be generated
        #self.bookingId = 1
        #payment id to be selected from payment
        #self.paymentId = 1
        self.hallId = hallId
        self.userId = userId
        self.bookingDate = bookingDate
        self.cateringChosen = cateringChosen

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
        #get booking id from database
        pass

    def generateReceipt():
        pass

    def selectPaymentMethod():
        #select from payment method in Payments
        pass



