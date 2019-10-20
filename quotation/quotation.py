# class for user in prime events
import sqlite3
from pathlib import Path
import time


class Quotation:
    """
    The Quotation object contains information about quotation
    Args:
    Attributes:
    """

    # class variable to define the path to the DB file
    dbFileName = "databaseFiles/primeEventsDb.db"

    def __repr__(self):
        return "Quotation({}{}{}{}{})".format()

    def __str__(self):
        pass

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
        """
        This function adds a new quotation information into the Database
            Args:
            Raises:
            Returns:
        """
        try:
            conn = sqlite3.connect(Quotation.dbFileName)
            c = conn.cursor()
            with conn:
                c.execute("INSERT INTO quotations VALUES (:reqDate, :bookingStartDate, :bookingEndDate, :hallId, :customerId, :status, :quotationAmount)",
                          {'reqDate': self.reqDate, 'bookingStartDate': self.bookingStartDate, 'bookingEndDate': self.bookingEndDate, 'hallId': self.hallId, 'customerId': self.customerId, 'status': self.status, 'quotationAmount': self.quotationAmount })
                # print('Log point 3')
                # print('Hall ID = ',self.hallId,' and customer id =', self.customerId)
                # input('breakpoint')
            c.execute("SELECT rowid from quotations WHERE reqDate = :reqDate AND hallId = :hallId AND customerId = :customerId" , {'reqDate': self.reqDate, 'hallId': self.hallId, 'customerId': self.customerId})
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
        """This function returns quotation details
            Args:
            Raises:
            Returns:
                - row -- dictionary
                    reqDate
                    hallId
                    customerId
                    status
                    quotationAmount
                    bookingStartDate
                    bookingEndDate
        """
        conn = sqlite3.connect(Quotation.dbFileName)
        c = conn.cursor()
        c.execute("SELECT rowid, reqDate, bookingStartDate, bookingEndDate, hallId, customerId, status, quotationAmount FROM quotations WHERE rowid = :rowId",
            {'rowId': self.rowId,})
        row = c.fetchone()
        conn.close()
        return row

    def __init__(self, quoDict):
        """This is a constructor for quotation class
            Args:
                - quoDict -- dictionary
                    reqDate
                    hallId
                    customerId
                    quotationAmount
                    bookingStartDate
                    bookingEndDate
            Raises:
            Returns:
        """
        if len(quoDict) == 6:
            # input('first if statement')
            # check if database file already exists
            self.reqDate = quoDict['reqDate']
            self.hallId = quoDict['hallId']
            self.customerId = quoDict['customerId']
            self.status = 'Pending'
            self.quotationAmount = quoDict['quotationAmount']
            self.bookingStartDate = quoDict['bookingStartDate']
            self.bookingEndDate = quoDict['bookingEndDate']
            # input('breakpoint')

            self.insertIntoUserDb()
        elif len(quoDict) == 1:
            # input('second if statement')
            self.rowId = quoDict['quotationId']
            row = self.getQuotationEntry()
            # print('Row is of type', type(row))
            self.reqDate = row[1]
            self.hallId = row[4]
            self.customerId = row[5]
            self.status = row[6]
            self.quotationAmount = row[7]
            self.bookingStartDate = row[2]
            self.bookingEndDate = row[3]

    def getQuotationAmount(self):
        return self.quotationAmount

    def  getBookingStartDate(self):
        return self.bookingStartDate

    def getBookingEndDate(self):
        return self.bookingEndDate

    def getReqDate(self):
        return self.reqDate

    def getHallId(self):
        return self.hallId

    def getCustomerId(self):
        return self.customerId

    def getStatus(self):
        return self.status

    def getQuotationId(self):
        return self.rowId

    def getQuotationAmount(self):
        return self.quotationAmount

    @classmethod
    def listQuotationRequests(cls, customerId):
        """This function returns quotation details of all quotations of a customer
            Args:
            Raises:
            Returns:
                - list of quotationDetails -- dictionary
                    reqDate
                    hallId
                    customerId
                    status
                    quotationAmount
                    bookingStartDate
                    bookingEndDate
        """
        conn = sqlite3.connect(cls.dbFileName)
        c = conn.cursor()
        c.execute("SELECT rowid, reqDate, bookingStartDate, bookingEndDate, hallId, customerId, status, quotationAmount FROM quotations WHERE customerId = :customerId",
            {'customerId': customerId,})
        results = c.fetchall()
        conn.close()
        return results

    @classmethod
    def changeStatus(self, rowId, status):
        """This is a function to change quotation status
            Args:
                - rowId -- int - quotation ID whose status is to be changed
                - status -- string - new status to be updated
            Raises:
            Returns:
        """
        self.status = status
        """Only first name, last name and password can be modified"""
        conn = sqlite3.connect(Quotation.dbFileName)
        c = conn.cursor()
        try:
            with conn:
                c.execute(
                    """UPDATE quotations SET status = :status WHERE rowid = :quotationId""",
                    {'status': status, 'quotationId': rowId})
        except sqlite3.Error as sqlite3Error:
            print("SQLite3 Error -->", sqlite3Error)
        finally:
            conn.close()

    @classmethod
    def listOwnerQuotationRequests(cls, ownerId):
        """This function returns quotation details of all quotations of an owner
            Args:
                - ownerId -- int - owner ID of the user whose quotation info is to be retrieved
            Raises:
            Returns:
                - list of quotationDetails -- dictionary
                    reqDate
                    hallId
                    customerId
                    status
                    quotationAmount
                    bookingStartDate
                    bookingEndDate
        """
        conn = sqlite3.connect(cls.dbFileName)
        c = conn.cursor()
        c.execute("SELECT rowid, bookingStartDate, bookingEndDate, hallId, customerId, status, quotationAmount FROM quotations WHERE hallId IN" +
                    "(SELECT rowid from halls WHERE ownerId = :ownerId)", {'ownerId': ownerId,})
        results = c.fetchall()
        conn.close()
        return results

    @classmethod
    def viewQuotationDetails(cls,rowId):
        """This function returns quotation details of a particular quotation
            Args:
                - rowId -- int - quotation ID whose details is to be retrieved
            Raises:
            Returns:
                - quotationDetails -- dictionary
                    reqDate
                    hallId
                    customerId
                    status
                    quotationAmount
                    bookingStartDate
                    bookingEndDate
        """
        conn = sqlite3.connect(Quotation.dbFileName)
        c = conn.cursor()
        c.execute("""SELECT rowid, bookingStartDate, bookingEndDate, hallId, customerId, status, quotationAmount FROM quotations WHERE rowid = :rowId""",{'rowId' : rowId, })
        output = c.fetchone()
        #print(output)
        #print(type(output))
        conn.close()
        return output

    @classmethod
    def changeAmount(self, rowId, amount):
        """This is a function to change quotation amount
            Args:
                - rowId -- int - quotation ID whose status is to be changed
                - amount -- float - new amount to be updated
            Raises:
            Returns:
        """
        conn = sqlite3.connect(Quotation.dbFileName)
        c = conn.cursor()
        try:
            with conn:
                c.execute(
                    """UPDATE quotations SET quotationAmount = :amount WHERE rowid = :quotationId""",
                    {'amount': amount, 'quotationId': rowId})
        except sqlite3.Error as sqlite3Error:
            print("SQLite3 Error -->", sqlite3Error)
        finally:
            conn.close()
