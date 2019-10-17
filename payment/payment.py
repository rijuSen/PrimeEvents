#class for payment in prime events
import sqlite3
from pathlib import Path

class Payment:
    dbFileName = "databaseFiles/primeEventsDb.db"

    def insertIntoPaymentDb(self):
        try:
            conn = sqlite3.connect(Payment.dbFileName)
            c = conn.cursor()
            print('Log point 2')
            with conn:
                c.execute("INSERT INTO payments VALUES (:paymentType, :paymentCoupon, :paymentAmount, :paymentStatus, :bookingId, :customerId)",
                          {'paymentType': self.paymentType, 'paymentCoupon': self.paymentCoupon,'paymentAmount': self.paymentAmount, 'paymentStatus': self.paymentStatus, 'bookingId': self.bookingId, 'customerId': self.customerId})
            c.execute("SELECT rowid from payments WHERE bookingId = :bookingId " , {'bookingId': self.bookingId,})
            self.success = True
            # save the rowid of the inserted row in the variable rowId
            for id in c.fetchone():
                self.rowId = id
        except sqlite3.Error as sqlite3Error:
            self.success = False
            print("SQLite3 Error : -->", sqlite3Error)

    def __init__(self, quoDict):
        """docstring"""
        if len(quoDict) == 4:
            # check if database file already exists
            self.paymentType = quoDict['paymentType']
            self.paymentAmount = quoDict['paymentAmount']
            self.paymentStatus = 'Pending'
            self.bookingId = quoDict['bookingId']
            self.customerId = quoDict['customerId']
            self.paymentCoupon = 'NULL'
            print('Pass dictionary', quoDict)
            self.insertIntoPaymentDb()
        if len(quoDict) == 5:
            # check if database file already exists
            self.paymentType = quoDict['paymentType']
            self.paymentCoupon = quoDict['couponCode']
            self.paymentAmount = quoDict['paymentAmount']
            self.paymentStatus = 'Pending'
            self.bookingId = quoDict['bookingId']
            self.customerId = quoDict['customerId']
            print('Pass dictionary', quoDict)
            self.insertIntoPaymentDb()
        elif len(quoDict) == 1:

            self.rowId = quoDict['paymentId']

    def getPaymentType(self):
        return self.paymentType

    def getRowId(self):
        return self.rowId

    def getPaymentId(self):
        #get payment id from database
        pass

    def generatePaymentId(self):
        #fetch the next available payment id from the database
        pass

    @classmethod
    def changeStatus(self, paymentId, status):
        self.paymentStatus = status
        """Only first name, last name and password can be modified"""
        conn = sqlite3.connect(Payment.dbFileName)
        c = conn.cursor()
        try:
            with conn:
                c.execute(
                    "UPDATE payments SET paymentStatus = :paymentStatus WHERE rowid = :paymentId",
                    {'paymentStatus': status, 'paymentId': paymentId})
        except sqlite3.Error as sqlite3Error:
            print("SQLite3 Error -->", sqlite3Error)
        finally:
            conn.close()

    @classmethod
    def listOwnerPaymentRequests(cls, ownerId):
        conn = sqlite3.connect(Payment.dbFileName)
        c = conn.cursor()
        c.execute("SELECT rowid, * FROM payments WHERE bookingId IN" +
                    "(SELECT rowid FROM Bookings WHERE hallId IN" +
                                "(SELECT rowid from halls WHERE ownerId = :ownerId))", {'ownerId': ownerId,})
        results = c.fetchall()
        conn.close()
        return results

    @classmethod
    def viewPaymentDetails(cls,rowId):
        conn = sqlite3.connect(Payment.dbFileName)
        c = conn.cursor()
        c.execute("SELECT rowid, * FROM payments WHERE rowid = :rowId",{'rowId': rowId,})
        output = c.fetchone()
        #print(output)
        #print(type(output))
        conn.close()
        return output
