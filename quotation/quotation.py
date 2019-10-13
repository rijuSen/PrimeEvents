# class for user in prime events
import sqlite3
from pathlib import Path


class Quotation:
    '''docstring'''

    # class variable to define the path to the DB file
    dbFileName = "databaseFiles/primeEventsDb.db"

    def insertIntoUserDb(self, reqDate, hallId, customerId, status, quotationAmount, bookingStartDate, bookingEndDate):
        try:
            conn = sqlite3.connect(Quotation.dbFileName)
            c = conn.cursor()
            with conn:
                c.execute("INSERT INTO quotation VALUES (:reqDate, :hallId, :customerId, :status, :quotationAmount, :bookingStartDate, :bookingEndDate)",
                          {'reqDate': reqDate, 'hallId': hallId, 'customerId': customerId, 'status': status,
                           'quotationAmount': quotationAmount, 'bookingStartDate': bookingStartDate, 'bookingEndDate': bookingEndDate})
            c.execute("SELECT rowid from quotation WHERE reqDate = :reqDate AND hallId = :hallId AND customerId = "
                      ":customerId",
                      {'reqDate': reqDate, 'hallId': hallId, 'customerId': customerId})

            # save the rowid of the inserted row in the variable rowId
            for id in c.fetchone():
                self.rowId = id

        except sqlite3.Error as sqlite3Error:
            print("SQLite3 Error : -->", sqlite3Error)
        finally:
            conn.close()

    def __init__(self, quoDict):
        self.quotationDbFilePath = Path(Quotation.dbFileName)
        # check if database file already exists
        self.reqDate = quoDict['reqDate']
        self.hallId = quoDict['hallId']
        self.customerId = quoDict['customerId']
        self.status = False
        self.quotationAmount = quoDict['quotationAmount']
        self.bookingStartDate = quoDict['bookingStartDate']
        self.bookingEndDate = quoDict['bookingEndDate']
        self.insertIntoUserDb(self.date, self.hallId, self.customerId, self.status, self.quotationAmount, self.bookingStartDate, self.bookingEndDate)

    def getReqDate(self):
        return self.reqDate

    def getHallId(self):
        return self.hallId

    def getCustomerId(self):
        return self.customerId

    def getStatus(self):
        return self.status

    def getQuotationId(self):
        return self.quotationId

    def getQuotationAmount(self):
        return self.quotationAmount

    def deleteUser(self):
        pass

    @classmethod
    def changeDatabase(cls, newDbName):
        cls.dbFileName = newDbName

    @classmethod
    def changeStatus(cls, status):
        """Only first name, last name and password can be modified"""
        conn = sqlite3.connect(self.dbFileName)
        c = conn.cursor()
        try:
            with conn:
                c.execute(
                    """UPDATE quotation SET status = :status WHERE quotationID = :quotationId""",
                    {'status': status, 'quotationId': self.quotationId})
        except sqlite3.Error as sqlite3Error:
            print("SQLite3 Error -->", sqlite3Error)
        finally:
            conn.close()
