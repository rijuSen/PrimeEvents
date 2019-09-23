#class for user in prime events
import sqlite3
from pathlib import Path

class User:
    '''docstring'''
    
    #class variable to define the path to the DB file
    dbFileName = "databaseFiles/primeEventsDb.db"
    def insertIntoUserDb(self,firstName,lastName,email,password,userType,allowFlag):
        try:
            conn = sqlite3.connect(User.dbFileName)
            c = conn.cursor()
            with conn:
                c.execute("INSERT INTO users VALUES (:firstName, :lastName, :email, :password, :userType, :allowFlag)",
                        {'firstName': firstName, 'lastName': lastName, 'email': email, 'password': password, 'userType': userType, 'allowFlag': allowFlag})
            c.execute("SELECT rowid from users WHERE email = :email",{'email': email,})
            
            #save the rowid of the inserted row in the variable rowId
            for id in c.fetchone():
                self.rowId = id
        
        except sqlite3.Error as sqlite3Error:
            print("SQLite3 Error : -->",sqlite3Error)
        finally:
            conn.close()
        

    def __init__(self,firstName,lastName,email,password,userType):
        self.userDbFilePath = Path(User.dbFileName)
        #check if database file already exists
        if not self.userDbFilePath.is_file():
            conn = sqlite3.connect(User.dbFileName)
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
        return '{} {}'.format(self.firstName, self.lastName)

    def getEmail(self):
        return self.email

    def getRowId(self):
        return self.rowId

    def getUserType(self):
        return self.userType

    def deleteUser():
        pass

    @classmethod
    def changeDatabase(cls, newDbName):
        cls.dbFileName = newDbName

    @classmethod
    def editUser(cls,editEntryWithEmail,firstName,lastName,password):
        """Only first name, last name and password can be modified"""
        conn = sqlite3.connect(self.dbFileName)
        c = conn.cursor()
        try:
            with conn:
                c.execute("""UPDATE users SET firstName = :fname, lastName = :lname, password = :pass WHERE email = :email""",{'fname': firstName, 'lname': lastName, 'password': password, 'email': editEntryWithEmail})
        except sqlite3.Error as sqlite3Error:
            print("SQLite3 Error -->",sqlite3Error)
        finally:
            conn.close()
    

    @classmethod
    def emailExists(cls,email):
        conn = sqlite3.connect(cls.dbFileName)
        c = conn.cursor()
        c.execute("SELECT count(*) FROM users WHERE email = :email",{'email':email,})
        data=c.fetchone()[0]
        if data==0:
            return False
        else:
            return True
#    @classmethod
#    def displayEntry(cls,email):
#        conn = sqlite3.connect(cls.dbFileName)
#        c = conn.cursor()
#        c.execute("SELECT firstName, lastName, email,  from users WHERE email = :email",{'email': email,})
#        for column in c.fetchone():

    #take a mail id and password and return a user object
    @classmethod
    def checkPassword(cls,email,passHash):
        conn = sqlite3.connect(cls.dbFileName)
        c = conn.cursor()
        c.execute("SELECT rowid, firstName, lastName, email, password, userType, allowFlag FROM users WHERE email = :email AND password = :password",{'email': email, 'password': passHash})
        data = c.fetchone()
        print(data)
        if not data == None:
            cls.rowId = data[0]
            cls.firstName = data[1]
            cls.lastName = data[2]
            cls.email = data[3]
            cls.password = data[4]
            cls.userType = data[5]
            cls.allowFlag = data[6]
            return True, cls.rowId, cls.firstName, cls.userType, cls.allowFlag 
        else:
            return False, '', '', '', ''
            







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
        conn = sqlite3.connect(User.dbFileName)
        c = conn.cursor()
        c.execute("SELECT rowid,firstName, lastName, email, userType, allowFlag FROM users")
        output = c.fetchall()
        for entry in output:
            print(entry,end='\n')
        conn.close()

    def blockUser(rowid):
        conn = sqlite3.connect(User.dbFileName)
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
