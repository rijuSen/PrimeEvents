# class for user in prime events
import sqlite3
from pathlib import Path
import time


class Quotation:
    '''docstring'''

    # class variable to define the path to the DB file
    dbFileName = "databaseFiles/primeEventsDb.db"

# CREATE TABLE quotations (
#                   reqDate datetime NOT NULL,
#                   bookingStartDate date NOT NULL,
#                   bookingEndDate date NOT NULL,
#                   hallId int NOT NULL,
#                   customerId int NOT NULL,
#                   status boolean NOT NULL,
#                   quotationAmount float NOT NULL,
#                   UNIQUE(reqDate, customerId, hallId),
#                   FOREIGN KEY(customerId) REFERENCES users(rowid),
#                   FOREIGN KEY(hallId) REFERENCES halls(rowid));

    def insertIntoUserDb(self):
        try:
            conn = sqlite3.connect(Quotation.dbFileName)
            c = conn.cursor()
            print('Log point 2')
            with conn:
                c.execute("INSERT INTO quotations VALUES (:reqDate, :hallId, :customerId, :status, :quotationAmount, :bookingStartDate, :bookingEndDate)",
                          {'reqDate': self.reqDate, 'hallId': self.hallId, 'customerId': self.customerId, 'status': self.status,
                           'quotationAmount': self.quotationAmount, 'bookingStartDate': self.bookingStartDate, 'bookingEndDate': self.bookingEndDate})
                # print('Log point 3')
                # print('Hall ID = ',self.hallId,' and customer id =', self.customerId)
                # input('breakpoint')
            c.execute("SELECT rowid from quotations WHERE reqDate = :reqDate", {'reqDate': self.reqDate,})
            # c.execute("SELECT rowid from quotations WHERE reqDate = :reqDate AND hallId = :hallId AND customerId = :customerId",
                      # {'reqDate': self.reqDate, 'hallId': self.hallId, 'customerId': self.customerId})
            self.success = True
            # print('Log point 1', self.success)
            # input('breakpoint')
            # save the rowid of the inserted row in the variable rowId
            for id in c.fetchone():
                self.rowid = id
        except sqlite3.Error as sqlite3Error:
            self.success = False
            print("SQLite3 Error : -->", sqlite3Error)
            # input('breakpoint')
# CREATE TABLE quotations (
#                   reqDate datetime NOT NULL,
#                   bookingStartDate date NOT NULL,
#                   bookingEndDate date NOT NULL,
#                   hallId int NOT NULL,
#                   customerId int NOT NULL,
#                   status boolean NOT NULL,
#                   quotationAmount float NOT NULL,
#                   UNIQUE(reqDate, customerId, hallId),
#                   FOREIGN KEY(customerId) REFERENCES users(rowid),
#                   FOREIGN KEY(hallId) REFERENCES halls(rowid));

    def getQuotationEntry(self):
        conn = sqlite3.connect(cls.dbFileName)
        c = conn.cursor()
        c.execute("SELECT rowid, reqDate, bookingStartDate, bookingEndDate, hallId, customerId, status, quotationAmount FROM quotations WHERE rowid = :rowId",
            {'rowId': self.rowId,})
        row = c.fetchone()
        conn.close()
        return row

    def __init__(self, quoDict):
        """docstring"""
        if len(quoDict) == 6:
            # check if database file already exists
            self.reqDate = quoDict['reqDate']
            self.hallId = quoDict['hallId']
            self.customerId = quoDict['customerId']
            self.status = False
            self.quotationAmount = quoDict['quotationAmount']
            self.bookingStartDate = quoDict['bookingStartDate']
            self.bookingEndDate = quoDict['bookingEndDate']
            print('Log point 1')
            self.insertIntoUserDb()
        elif len(quoDict) == 1:
            self.rowId = quoDict['quotationId']
            row = getQuotationEntry()
            print('Row is of type', type(row))
            self.reqDate = row[1]
            self.hallId = row[4]
            self.customerId = row[5]
            self.status = row[6]
            self.quotationAmount = row[7]
            self.bookingStartDate = row[2]
            self.bookingEndDate = row[3]



    def getReqDate(self):
        return self.reqDate

    def getHallId(self):
        return self.hallId

    def getCustomerId(self):
        return self.customerId

    def getStatus(self):
        return self.status

    def getQuotationId(self):
        return self.rowid

    def getQuotationAmount(self):
        return self.quotationAmount

    @classmethod
    def listQuotationRequests(cls, customerId):
        conn = sqlite3.connect(cls.dbFileName)
        c = conn.cursor()
        c.execute("SELECT rowid, reqDate, bookingStartDate, bookingEndDate, hallId, customerId, status, quotationAmount FROM quotations WHERE customerId = :customerId",
            {'customerId': customerId,})
        results = c.fetchall()
        conn.close()
        return results

    def changeStatus(self, status):
        self.status = status
        """Only first name, last name and password can be modified"""
        conn = sqlite3.connect(Quotation.dbFileName)
        c = conn.cursor()
        try:
            with conn:
                c.execute(
                    """UPDATE quotations SET status = :status WHERE quotationID = :quotationId""",
                    {'status': self.status, 'quotationId': self.rowid})
        except sqlite3.Error as sqlite3Error:
            print("SQLite3 Error -->", sqlite3Error)
        finally:
            conn.close()
