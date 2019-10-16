#class for Booking in prime events
import sqlite3
from pathlib import Path

class Booking:
    '''docstring'''

    #class variable to define the path to the DB file
    dbFileName = "databaseFiles/primeEventsDb.db"
    def insertIntoBookingDb(self):
        try:
            conn = sqlite3.connect(Booking.dbFileName)
            c = conn.cursor()
# CREATE TABLE bookings (
#                   bookingStartDate date NOT NULL,
#                   bookingEndDate date NOT NULL,
#                   hallId int NOT NULL,
#                   customerId int NOT NULL,
#                   status boolean NOT NULL,
#                   bookingAmount float NOT NULL,
#                   quotationId int NOT NULL,
#                   UNIQUE(quotationId),
#                   FOREIGN KEY(customerId) REFERENCES users(rowid),
#                   FOREIGN KEY(quotationId) REFERENCES quotations(rowid),
#                   FOREIGN KEY(hallId) REFERENCES halls(rowid));
            with conn:
                c.execute("INSERT INTO Bookings VALUES (:bookingStartDate, :bookingEndDate, :hallId, :customerId, :status, :bookingAmount, :quotationId)",
                        { 'bookingStartDate': self.bookingStartDate, 'bookingEndDate': self.bookingEndDate, 'hallId': self.hallId, 'customerId': self.customerId, 'status': self.status, 'bookingAmount': self.bookingAmount, 'quotationId': self.quotationId})
            c.execute("SELECT rowid from Bookings WHERE quotationId = :quotationId",{'quotationId': self.quotationId,})
            #save the rowid of the inserted row in the variable rowId
            for id in c.fetchone():
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
        conn = sqlite3.connect(Booking.dbFileName)
        c = conn.cursor()
        c.execute("""SELECT rowid, * FROM bookings WHERE quotationId = :quotationId""",{'quotationId' : self.quotationId, })
        output = c.fetchone()
        conn.close()
        return output

    def __init__(self,bookingInfo):
        """bookingInfo['bookingStartDate','bookingEndDate','hallId','customerId','bookingAmount','quotationId']"""
        if len(bookingInfo) == 6:
            self.bookingStartDate = bookingInfo['bookingStartDate']
            self.bookingEndDate = bookingInfo['bookingEndDate']
            self.hallId = bookingInfo['hallId']
            self.customerId = bookingInfo['customerId']
            self.status = 'Completed'
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
    def editBooking(cls,editBookingOfbookingEndDate,editbookingStartDate,bookingStartDate,customerId,status,bookingAmount):
        """Except bookingEndDate rest all attributes can be modified"""
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


    @classmethod
    def viewAllBookings(cls):
        conn = sqlite3.connect(Booking.dbFileName)
        c = conn.cursor()
        c.execute("SELECT rowid,* FROM Bookings")
        output = c.fetcBooking()
        #print(output)
        #print(type(output))
        conn.close()
        return output

    @classmethod
    def viewUserBookings(cls, userObj):
        conn = sqlite3.connect(Booking.dbFileName)
        c = conn.cursor()
        c.execute("SELECT rowid,* from Bookings WHERE customerId = :customerId",{'customerId': userObj.getRowId(),})
        output = c.fetchall()
        conn.close()
        return output

    @classmethod
    def viewBookingDetails(cls,rowId):
        conn = sqlite3.connect(Booking.dbFileName)
        c = conn.cursor()
        c.execute("""SELECT rowid, * FROM Bookings WHERE rowid = :rowId""",{'rowId' : rowId, })
        output = c.fetchone()
        #print(output)
        #print(type(output))
        conn.close()
        return output


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
