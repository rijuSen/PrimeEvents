#class for user in prime events
import sqlite3
from pathlib import Path

class User:
    '''docstring'''
    
    def insertIntoUserDb(self,firstName,lastName,email,password,userType,allowFlag):
        try:
            conn = sqlite3.connect(self.userDbFileName)
            c = conn.cursor()
            with conn:
                c.execute("INSERT INTO users VALUES (:firstName, :lastName, :email, :password, :userType, :allowFlag)",
                        {'firstName': firstName, 'lastName': lastName, 'email': email, 'password': password, 'userType': userType, 'allowFlag': allowFlag})
        except sqlite3.IntegrityError as sqlite3Error:
            print("SQLite3 Error : -->",sqlite3Error)
        finally:
            conn.close()

    def __init__(self,firstName,lastName,email,password,userType):
        self.userDbFileName = "../databaseFiles/primeEventsDb.db"
        self.userDbFilePath = Path(self.userDbFileName)
        #check if database file already exists
        if not self.userDbFilePath.is_file():
            conn = sqlite3.connect(self.userDbFileName)
            c = conn.cursor()
            c.execute("""CREATE TABLE users (
                        firstName text NOT NULL,
                        lastName text NOT NULL, 
                        email text NOT NULL UNIQUE,
                        password text NOT NULL,
                        userType text NOT NULL,
                        allowFlag int DEFAULT 0,
                        UNIQUE(email))
                        """)
            conn.close()
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.userType = userType
        self.allowFlag = 0
        self.insertIntoUserDb(firstName,lastName,email,password,userType,self.allowFlag)

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def fullName(self):
        return '{} {}'.format(self.firstName, sefl.lastName)

    def getEmail():
        return self.email

    def getPasswordHash():
        pass

    def createUser():
        pass

    def deleteUser():
        pass

    def editUser():
        pass



class Owner(User):
    '''Owner class extending User'''

    def __init__(self,firstName,lastName,email,password):
        self.userType = "Owner"            
        super().__init__(firstName,lastName,email,password,self.userType)

    
    def getOwnerHalls(userId):
        pass

    def listOwnerQuotationRequests(userId):
        pass

    def listOwnerBookings(userId):
        pass


class Customer(User):
    '''Customer class extending User'''

    def __init__(self,firstName,lastName,email,password):
       self.userType = "Customer"
       super().__init__(firstName,lastName,email,password,self.userType)

    def getCustomerBookingHistory(userId):
        pass

    def getCustomerQuotationRequestHistory(userId):
        pass



class Admin(User):
    '''Admin class extending User'''
    
    def __init__(self,firstName,lastName,email,password):
        self.userType = "Admin"            
        super().__init__(firstName,lastName,email,password,self.userType)

    def viewAllUsers():
        conn = sqlite3.connect('../databaseFiles/primeEventsDb.db')
        c = conn.cursor()
        c.execute("SELECT rowid,* FROM users")
        output = c.fetchall()
        for entry in output:
            print(entry,end='\n')
        conn.close()

    def blockUser(rowid):
        conn = sqlite3.connect('../databaseFiles/primeEventsDb.db')
        c = conn.cursor()
        try:
            with conn:
                #c.execute("SELECT last_insert_rowid()")
                #print(c.fetchall())
                c.execute("""UPDATE users SET allowFlag = :allowFlag WHERE rowid = :rowid""",{'allowFlag': 1, 'rowid':rowid})
                #print(c.fetchone())
                #if 'None' in str(c.fetchone()):
                 #   print('Id:',rowid,'is not present in the database')
               # else:
                #    c.execute("SELECT rowid,* FROM users WHERE rowid = :rowid",{'rowid': rowid,})
                 #   print(c.fetchone())
        except sqlite3.Error as sqlite3Error:
            print("SQLite3 Error -->",sqlite3Error)
        finally:
            conn.close()


    def viewAllBookings():
        pass
