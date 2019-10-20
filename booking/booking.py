#class for Booking in prime events
import sqlite3
import time
import datetime
from pathlib import Path

class Booking:
    """This class is the entity class for all bookings of the system
        Args:
        Raises:
        Returns:
    """
    #class variable to define the path to the DB file
    dbFileName = "databaseFiles/primeEventsDb.db"
    def insertIntoBookingDb(self):
        """This method inserts into the database the attributes of a booking
            Args:
            Raises:
            Returns:
        """
        try:
            conn = sqlite3.connect(Booking.dbFileName)
            c = conn.cursor()
            with conn:
                c.execute("INSERT INTO Bookings VALUES (:bookingStartDate, :bookingEndDate, :hallId, :customerId, :status, :bookingAmount, :quotationId, NULL)",
                        { 'bookingStartDate': self.bookingStartDate, 'bookingEndDate': self.bookingEndDate, 'hallId': self.hallId, 'customerId': self.customerId, 'status': self.status, 'bookingAmount': self.bookingAmount, 'quotationId': self.quotationId})
            c.execute("SELECT rowid from Bookings WHERE quotationId = :quotationId",{'quotationId': self.quotationId,})
            #save the rowid of the inserted row in the variable rowId
            time.sleep(2)
            for id in c.fetchone():
                #print('reached')
                #time.sleep(2)
                input(id)
                self.rowId = id
                # strDebug = '{}{}'.format('Booking row inserted and rowId is ',id)
                # input(strDebug)
            self.success = True
        except sqlite3.Error as sqlite3Error:
            self.success = False
            print("SQLite3 Error : -->",sqlite3Error)
        finally:
            conn.close()


    def getBookingDetails(self):
        """This method fetches booking details from the database
            Args:
            Raises:
            Returns: tuple - a booking entry
        """
        conn = sqlite3.connect(Booking.dbFileName)
        c = conn.cursor()
        c.execute("""SELECT rowid, * FROM bookings WHERE quotationId = :quotationId""",{'quotationId' : self.quotationId, })
        output = c.fetchone()
        conn.close()
        return output

    def __init__(self,bookingInfo):
        """This is the constructor of the class booking
            Args: Dictionary of booking details
            Raises:
            Returns: Object of Booking
        """
        if len(bookingInfo) == 6:
            self.bookingStartDate = bookingInfo['bookingStartDate']
            self.bookingEndDate = bookingInfo['bookingEndDate']
            self.hallId = bookingInfo['hallId']
            self.customerId = bookingInfo['customerId']
            self.status = 'Initiated'
            self.bookingAmount = bookingInfo['bookingAmount']
            self.quotationId = bookingInfo['quotationId']
            self.insertIntoBookingDb()
        elif len(bookingInfo) == 1:
            self.rowId = bookingInfo['bookingId']
            row = getBookingDetails()
            self.bookingStartDate = row[1]
            self.bookingEndDate = row[2]
            self.hallId = row[3]
            self.customerId = row[4]
            self.status = row[5]
            self.bookingAmount = row[6]
            self.quotationId = row[7]


    def completeBooking(self):
        """This method changes the status of the booking to complete
            Args:
            Raises:
            Returns:
        """
        self.status = 'Completed'
        conn = sqlite3.connect(Booking.dbFileName)
        c = conn.cursor()
        try:
            with conn:
                c.execute("""UPDATE Bookings SET status = :status WHERE rowid = :rowId""",{'status': self.status, 'rowId': self.rowId})
        except sqlite3.Error as sqlite3Error:
            print("SQLite3 Error -->",sqlite3Error)
        finally:
            conn.close()

    @classmethod
    def editBooking(cls,editBookingInfo):
        """This is a class method to edit a booking entry
            Args: Dictionary of booking details to be modified
            Raises:
            Returns:
        """
        editBookingOfbookingEndDate = editBookingInfo['editBookingOfbookingEndDate']
        editbookingStartDate = editBookingInfo['editbookingStartDate']
        bookingStartDate = editBookingInfo['bookingStartDate']
        customerId = editBookingInfo['customerId']
        status = editBookingInfo['status']
        bookingAmount = editBookingInfo['bookingAmount']
        conn = sqlite3.connect(self.dbFileName)
        c = conn.cursor()
        try:
            with conn:
                c.execute("""UPDATE Bookings SET bookingStartDate = :hname, customerId = :hType, status = :hAddr, bookingAmount = :hCapacity WHERE bookingEndDate = :oId AND bookingStartDate = :bookingStartDate""",{'hname': bookingStartDate, 'hType': customerId, 'hAddr': status, 'hCapacity': bookingAmount, 'bookingEndDate': editBookingOfbookingEndDate, 'bookingStartDate': editbookingStartDate })
        except sqlite3.Error as sqlite3Error:
            print("SQLite3 Error -->",sqlite3Error)
        finally:
            conn.close()

    def completeBooking(self):
        """This method changes the status of the booking to complete
            Args:
            Raises:
            Returns:
        """
        self.status = 'Completed'
        conn = sqlite3.connect(Booking.dbFileName)
        c = conn.cursor()
        try:
            with conn:
                c.execute("""UPDATE Bookings SET status = :status WHERE rowid = :rowId""",{'status': self.status, 'rowId': self.rowId})
        except sqlite3.Error as sqlite3Error:
            print("SQLite3 Error -->",sqlite3Error)
        finally:
            conn.close()

    def getRowId(self):
        return self.rowId


    def getBookingStartDate(self):
        return self.bookingStartDate

    def getBookingEndDate(self):
        return self.bookingEndDate

    def getCustomerId(self):
        return self.customerId

    def getStatus(self):
        return self.status

    def getBookingAmount(self):
        return self.bookingAmount

    def addPaymentInfo(self, paymentId):
        """This method adds payment details to the booking
            Args: paymentId
            Raises:
            Returns:
        """
        self.paymentId = paymentId
        conn = sqlite3.connect(Booking.dbFileName)
        c = conn.cursor()
        try:
            with conn:
                c.execute("""UPDATE Bookings SET paymentId = :paymentId WHERE rowid = :rowId""",{'paymentId ': self.paymentId , 'rowId': self.rowId})
        except sqlite3.Error as sqlite3Error:
            print("SQLite3 Error -->",sqlite3Error)
        finally:
            conn.close()

    @classmethod
    def viewAllBookings(cls):
        """This is a class method that returns a list of all bookings
            Args:
            Raises:
            Returns: list of tuples
        """
        conn = sqlite3.connect(Booking.dbFileName)
        c = conn.cursor()
        c.execute("SELECT rowid,* FROM Bookings")
        output = c.fetchall()
        conn.close()
        return output

    @classmethod
    def viewUserBookings(cls, userObj):
        """This is a class method that returns a list of all bookings of a specific user
            Args:
            Raises:
            Returns: list of tuples
        """
        conn = sqlite3.connect(Booking.dbFileName)
        c = conn.cursor()
        c.execute("SELECT rowid,* from Bookings WHERE customerId = :customerId",{'customerId': userObj.getRowId(),})
        output = c.fetchall()
        conn.close()
        return output

    @classmethod
    def viewBookingDetails(cls,rowId):
        """This is a class method returns booking details
            Args:
            Raises:
            Returns: tuples containing details
        """
        conn = sqlite3.connect(Booking.dbFileName)
        c = conn.cursor()
        c.execute("""SELECT rowid, * FROM Bookings WHERE rowid = :rowId""",{'rowId' : rowId, })
        output = c.fetchone()
        conn.close()
        return output

    @classmethod
    def listOwnerBookings(cls, ownerId):
        """This is a class method that returns a list of all bookings of a specific owner
            Args:
            Raises:
            Returns: list of tuples
        """
        conn = sqlite3.connect(Booking.dbFileName)
        c = conn.cursor()
        c.execute("SELECT rowid, * FROM Bookings WHERE hallId IN" +
                    "(SELECT rowid from halls WHERE ownerId = :ownerId)", {'ownerId': ownerId,})
        results = c.fetchall()
        conn.close()
        return results

    @classmethod
    def changeStatus(self, rowId, status):
        """This is a class method that returns a list of all bookings
            Args:
            Raises:
            Returns: list of tuples
        """
        self.status = status
        """Only first name, last name and password can be modified"""
        conn = sqlite3.connect(Booking.dbFileName)
        c = conn.cursor()
        try:
            with conn:
                c.execute(
                    """UPDATE Bookings SET status = :status WHERE rowid = :bookingId""",
                    {'status': status, 'bookingId': rowId})
        except sqlite3.Error as sqlite3Error:
            print("SQLite3 Error -->", sqlite3Error)
        finally:
            conn.close()

    @classmethod
    def getOwnerBookingIds(cls, ownerId):
        """This is a class method that returns a list of all bookings of a specific owner
            Args:
            Raises:
            Returns: list of tuples
        """
        conn = sqlite3.connect(Booking.dbFileName)
        c = conn.cursor()
        c.execute("SELECT rowid FROM Bookings WHERE hallId IN" +
                    "(SELECT rowid from halls WHERE ownerId = :ownerId)", {'ownerId': ownerId,})
        results = c.fetchall()
        conn.close()
        return results


    # @classmethod
    # def BookingExists(cls, bookingStartDate, userObj):
    #     conn = sqlite3.connect(Booking.dbFileName)
    #     c = conn.cursor()
    #     bookingEndDate = userObj.getRowId()
    #     c.execute("SELECT count(*) FROM Bookings WHERE bookingEndDate = :bookingEndDate AND bookingStartDate = :bookingStartDate",{'bookingEndDate': bookingEndDate, 'bookingStartDate': bookingStartDate})
    #     data = c.fetchone()[0]
    #     if data == 0:
    #         return False
    #     else:
    #         return True
