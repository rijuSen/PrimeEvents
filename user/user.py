# class for user in prime events
import sqlite3
from pathlib import Path


class User:
    """This class is the entity class for all users of the system
        Args:
        Raises:
        Returns:
    """
    # class variable to define the path to the DB file
    dbFileName = "databaseFiles/primeEventsDb.db"

    def insertIntoUserDb(self):
        """This method inserts into the database the attributes of user
            Args:
            Raises:
            Returns:
        """
        self.userDbFilePath = Path(User.dbFileName)
        # insert entry into database
        try:
            conn = sqlite3.connect(User.dbFileName)
            c = conn.cursor()
            with conn:
                c.execute("INSERT INTO users VALUES (:firstName, :lastName, :email, :password, :userType, :allowFlag)",
                          {'firstName': self.firstName, 'lastName': self.lastName, 'email': self.email, 'password': self.password,
                           'userType': self.userType, 'allowFlag': self.allowFlag})
            c.execute("SELECT rowid from users WHERE email = :email", {'email': self.email, })
            # save the rowid of the inserted row in the variable rowId
            for id in c.fetchone():
                self.rowId = id

        except sqlite3.Error as sqlite3Error:
            print("SQLite3 Error : -->", sqlite3Error)
        finally:
            conn.close()

    def checkPassword(self, userInfo):
        """This method contains all functionality related to the customer along with the flow
            Args:
                - userInfo -- Dictionary of user email and password hash
            Raises:
            Returns: user entry
        """
        email = userInfo['email']
        password = userInfo['password']
        conn = sqlite3.connect(self.dbFileName)
        c = conn.cursor()
        c.execute(
            "SELECT rowid, firstName, lastName, email, password, userType, allowFlag FROM users WHERE email = :email AND password = :password",
            {'email': email, 'password': password})
        row = c.fetchone()
        return row

    # def __init__(self,firstName,lastName,email,password,userType):

    def __init__(self, userInfo):
        """This is the constructor method of class User
            Args:
                - userInfo -- Dictionary of user details
            Raises:
            Returns: object of type User
        """
        # create a new entry in the DB
        if len(userInfo) == 5:
            self.firstName = userInfo['firstName']
            self.lastName = userInfo['lastName']
            self.email = userInfo['email']
            self.password = userInfo['password']
            self.userType = userInfo['userType']
            self.allowFlag = 0
            self.insertIntoUserDb()
            self.success = True
        # create an object of an existing entry
        if len(userInfo) == 2:
            row = self.checkPassword(userInfo)
            if not row == None:
                self.rowId = row[0]
                self.firstName = row[1]
                self.lastName = row[2]
                self.email = row[3]
                self.password = row[4]
                self.userType = row[5]
                self.allowFlag = row[6]
                self.success = True
            else:
                self.success = False

    def getSuccess(self):
        return self.success

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

    def getAllowFlag(self):
        return self.allowFlag

    def deleteUser():
        pass

    @classmethod
    def changeDatabase(cls, newDbName):
        cls.dbFileName = newDbName

    @classmethod
    def editUser(cls, editEntryWithEmail, firstName, lastName, password):
        """This class method modifies user details
            Args:
                - editEntryWithEmail - email address of the entry to be modified
                - firstName - new first name
                - lastName - new last name
                - password - new password hash
            Raises:
            Returns:
        """
        conn = sqlite3.connect(self.dbFileName)
        c = conn.cursor()
        try:
            with conn:
                c.execute(
                    """UPDATE users SET firstName = :fname, lastName = :lname, password = :pass WHERE email = :email""",
                    {'fname': firstName, 'lname': lastName, 'password': password, 'email': editEntryWithEmail})
        except sqlite3.Error as sqlite3Error:
            print("SQLite3 Error -->", sqlite3Error)
        finally:
            conn.close()

    @classmethod
    def emailExists(cls, email):
        """This class method checks if a email address is already registered on the platform
            Args:
                - email - email address
            Raises:
            Returns: Boolean
        """
        conn = sqlite3.connect(cls.dbFileName)
        c = conn.cursor()
        c.execute("SELECT count(*) FROM users WHERE email = :email", {'email': email, })
        data = c.fetchone()[0]
        if data == 0:
            return False
        else:
            return True

class Owner(User):
    '''Owner class extending User'''

    def __init__(self, userInfo):
        userInfo['userType'] = "Owner"
        super().__init__(userInfo)

    def getOwnerHalls(userId):
        pass

    def listOwnerQuotationRequests(userId):
        pass

    def listOwnerBookings(userId):
        pass


class Customer(User):
    '''Customer class extending User'''

    def __init__(self, userInfo):
        userInfo['userType'] = "Customer"
        super().__init__(userInfo)

    def getCustomerBookingHistory(userId):
        pass

    def getCustomerQuotationRequestHistory(userId):
        pass


class Admin(User):
    '''Admin class extending User'''

    def __init__(self, userInfo):
        self.userType = "Admin"
        # create a new entry in the DB
        userInfo['userType'] = self.userType
        super().__init__(userInfo)

    def viewAllUsers(self):
        conn = sqlite3.connect(User.dbFileName)
        c = conn.cursor()
        c.execute("SELECT rowid,firstName, lastName, email, userType, allowFlag FROM users")
        output = c.fetchall()
        for entry in output:
            print(entry)
        conn.close()

    def blockUser(self, rowid):
        conn = sqlite3.connect(User.dbFileName)
        c = conn.cursor()
        try:
            with conn:
                c.execute("""UPDATE users SET allowFlag = :allowFlag WHERE rowid = :rowid""",
                          {'allowFlag': 1, 'rowid': rowid})
        except sqlite3.Error as sqlite3Error:
            print("SQLite3 Error -->", sqlite3Error)
        finally:
            conn.close()

    def unblockUser(self, rowid):
        conn = sqlite3.connect(User.dbFileName)
        c = conn.cursor()
        try:
            with conn:
                c.execute("""UPDATE users SET allowFlag = :allowFlag WHERE rowid = :rowid""",
                          {'allowFlag': 0, 'rowid': rowid})
        except sqlite3.Error as sqlite3Error:
            print("SQLite3 Error -->", sqlite3Error)
        finally:
            conn.close()

    def viewAllBookings(self):
        pass
