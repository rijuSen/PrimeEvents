#class for hall in prime events
import sqlite3
from pathlib import Path

class Hall:
    '''docstring'''
#    
#    def insertIntoHallDb(self,firstName,lastName,email,password,hallType,allowFlag):
#        try:
#            conn = sqlite3.connect('hall.db')
#            c = conn.cursor()
#            with conn:
#                c.execute("INSERT INTO halls VALUES (:firstName, :lastName, :email, :password, :hallType, :allowFlag)",
#                        {'firstName': firstName, 'lastName': lastName, 'email': email, 'password': password, 'hallType': hallType, 'allowFlag': allowFlag})
#        except sqlite3.IntegrityError as sqlite3Error:
#            print("SQLite3 Error : -->",sqlite3Error)
#        finally:
#            conn.close()
#
    def __init__(self,hallName,ownerId,hallType,hallCapacity,hallAddr):
        self.hallDbFileName = "hall.db"
        self.hallDbFilePath = Path(self.hallDbFileName)
        #check if database file already exists
        if not self.hallDbFilePath.is_file():
            conn = sqlite3.connect('hall.db')
            c = conn.cursor()
            c.execute("""CREATE TABLE halls (
                        hallName text NOT NULL,
                        hallType text NOT NULL, 
                        ownerId int,

                        password text NOT NULL,
                        hallType text NOT NULL,
                        allowFlag int DEFAULT 0,
                        UNIQUE(email))
                        """)
#            conn.close()
#        self.firstName = firstName
#        self.lastName = lastName
#        self.email = email
#        self.password = password
#        self.hallType = hallType
#        self.allowFlag = 0
#        self.insertIntoHallDb(firstName,lastName,email,password,hallType,self.allowFlag)
#
#    def getFirstName(self):
#        return self.firstName
#
#    def getLastName(self):
#        return self.lastName
#
#    def fullName(self):
#        return '{} {}'.format(self.firstName, sefl.lastName)
#
#    def getEmail():
#        return self.email
#
#    def getPasswordHash():
#        pass
#
#    def createHall():
#        pass
#
#    def deleteHall():
#        pass
#
#    def editHall():
#        pass
#
#
#
#class Owner(Hall):
#    '''Owner class extending Hall'''
#
#    def __init__(self,firstName,lastName,email,password):
#        self.hallType = "Owner"            
#        super().__init__(firstName,lastName,email,password,self.hallType)
#
#    
#    def getOwnerHalls(hallId):
#        pass
#
#    def listOwnerQuotationRequests(hallId):
#        pass
#
#    def listOwnerBookings(hallId):
#        pass
#
#
#class Customer(Hall):
#    '''Customer class extending Hall'''
#
#    def __init__(firstName,lastName,email,password):
#       self.hallType = "Customer"
#       super().__init__(firstName,lastName,email,password,self.hallType)
#
#    def getCustomerBookingHistory(hallId):
#        pass
#
#    def getCustomerQuotationRequestHistory(hallId):
#        pass
#
#
#
#class Admin(Hall):
#    '''Admin class extending Hall'''
#    
#    def __init__(self,firstName,lastName,email,password):
#        self.hallType = "Admin"            
#        super().__init__(firstName,lastName,email,password,self.hallType)
#
#    def viewAllHalls():
#        conn = sqlite3.connect('hall.db')
#        c = conn.cursor()
#        c.execute("SELECT rowid,* FROM halls")
#        output = c.fetchall()
#        for entry in output:
#            print(entry,end='\n')
#        conn.close()
#
#    def blockHall(rowid):
#        conn = sqlite3.connect('hall.db')
#        c = conn.cursor()
#        try:
#            with conn:
#                c.execute("""UPDATE halls SET allowFlag = :allowFlag WHERE rowid = :rowid""",{'allowFlag': 1, 'rowid':rowid})
#                if str(c.fetchone()) == "None":
#                    print('Id:',rowid,'is not present in the database')
#                else:
#                    c.execute("SELECT rowid,* FROM halls WHERE rowid = :rowid",{'rowid': rowid,})
#        except sqlite3.Error as sqlite3Error:
#            print("SQLite3 Error -->",sqlite3Error)
#        finally:
#            conn.close()
#
#
#    def viewAllBookings():
#        pass
