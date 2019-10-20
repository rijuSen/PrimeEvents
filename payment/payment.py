#class for payment in prime events
import sqlite3
from pathlib import Path

class Payment:
    """The Payment object contains information about payment
    Args:
    Attributes:
    """

    dbFileName = "databaseFiles/primeEventsDb.db"

    def insertIntoPaymentDb(self):
        """This function adds a new payment information into the Database
            Args:
            Raises:
            Returns:
        """
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
        """This is a constructor for payment class
            Args:
                - quoDict -- dictionary
                    paymentType
                    couponCode
                    paymentAmount
                    bookingId
                    customerId
            Raises:
            Returns:
        """
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

    @classmethod
    def changeStatus(self, paymentId, status):
        """This is a function to change payment status
            Args:
                - paymentId -- int - payment ID whose status is to be changed
                - status -- string - new status to be updated
            Raises:
            Returns:
        """
        self.paymentStatus = status
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
        """This is a function which returns all the payment info for an owner
            Args:
                - ownerId -- int - owner ID of the user whose payment info is to be retrieved
            Raises:
            Returns:
                - list of paymentInfo -- dictionary
                    paymentId
                    paymnetType
                    couponCode
                    paymentStatus
                    paymentAmount
                    bookingId
        """
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
        """This is a function which returns payment info for a particular payment Id
            Args:
                - rowId -- int - paymnet ID whose details is to be retrieved
            Raises:
            Returns:
                - paymentInfo -- dictionary
                    paymentId
                    paymnetType
                    couponCode
                    paymentStatus
                    paymentAmount
                    bookingId
        """
        conn = sqlite3.connect(Payment.dbFileName)
        c = conn.cursor()
        c.execute("SELECT rowid, * FROM payments WHERE rowid = :rowId",{'rowId': rowId,})
        output = c.fetchone()
        #print(output)
        #print(type(output))
        conn.close()
        return output
