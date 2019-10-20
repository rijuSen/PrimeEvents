#class for hall in prime events
import sqlite3
from pathlib import Path

class Hall:
    """This class is the entity class of hall object
        Attributes:
            hallName
            ownerId
            dayTariff
            hallType
            hallAddr
            hallCapacity
            dbFilePath
    """
    #class variable to define the path to the DB file
    dbFileName = "databaseFiles/primeEventsDb.db"
    def insertIntoHallDb(self):
        """This method inserts into the database the attributes of hall
            Args:
            Raises:
            Returns:
        """
        try:
            conn = sqlite3.connect(Hall.dbFileName)
            c = conn.cursor()
            with conn:
                c.execute("INSERT INTO halls VALUES (:hallName, :ownerId, :dayTariff, :hallType, :hallAddr, :hallCapacity)",
                        {'hallName': self.hallName, 'ownerId': self.ownerId, 'dayTariff': self.dayTariff, 'hallType': self.hallType, 'hallAddr': self.hallAddr, 'hallCapacity': self.hallCapacity})

            c.execute("SELECT rowid from halls WHERE hallName = :hallName AND ownerId = :ownerId",{'hallName': self.hallName,'ownerId': self.ownerId})
            #save the rowid of the inserted row in the variable rowId
            for id in c.fetchone():
                self.rowId = id

        except sqlite3.Error as sqlite3Error:
            print("SQLite3 Error : -->",sqlite3Error)
        finally:
            conn.close()



    def __init__(self,hallInfo):
        """This is the constructor of the class hall
            Args: Dictionary of hall details
            Raises:
            Returns: Object of Hall type
        """
        if len(hallInfo) == 6:
            self.hallName = hallInfo['hallName']
            self.ownerId = hallInfo['ownerId']
            self.dayTariff = hallInfo['dayTariff']
            self.hallType = hallInfo['hallType']
            self.hallAddr = hallInfo['hallAddr']
            self.hallCapacity = hallInfo['hallCapacity']
            self.dbFilePath = Path(Hall.dbFileName)
            self.insertIntoHallDb(self.hallName,self.ownerId,self.hallType,self.hallAddr,self.hallCapacity, self.dayTariff)
        if len(hallInfo) == 1:
            self.rowId = hallInfo['hallId']
            row = Hall.viewHallDetails(self.rowId)
            self.hallName = row[1]
            self.ownerId = row[2]
            self.dayTariff = row[3]
            self.hallType = row[4]
            self.hallAddr = row[5]
            self.hallCapacity = row[6]


    @classmethod
    def editHall(cls,editHallOfOwnerId,editHallName,hallName,hallType,hallAddr,hallCapacity):
        """This is a class method to edit details of a hall
            Args:
            Raises:
            Returns:
        """
        conn = sqlite3.connect(self.dbFileName)
        c = conn.cursor()
        try:
            with conn:
                c.execute("""UPDATE halls SET hallName = :hname, hallType = :hType, hallAddr = :hAddr, hallCapacity = :hCapacity WHERE ownerId = :oId AND hallName = :hallName""",{'hname': hallName, 'hType': hallType, 'hAddr': hallAddr, 'hCapacity': hallCapacity, 'ownerId': editHallOfOwnerId, 'hallName': editHallName })
        except sqlite3.Error as sqlite3Error:
            print("SQLite3 Error -->",sqlite3Error)
        finally:
            conn.close()



    def getHallName(self):
        return self.hallName

    def getOwnerId(self):
        return self.ownerId

    def getHallType(self):
        return self.hallType

    def getHallAddrs(self):
        return self.hallAddr

    def getHallCapacity(self):
        return self.hallCapacity

    def getDayTariff(self):
        return self.dayTariff

    def getHallId(self):
        return self.rowId


    @classmethod
    def viewAllHalls(cls):
        """This method lists all halls in the database
            Args:
            Raises:
            Returns: list of tuples
        """
        conn = sqlite3.connect(Hall.dbFileName)
        c = conn.cursor()
        c.execute("SELECT rowid,* FROM halls")
        output = c.fetchall()
        #print(output)
        #print(type(output))
        conn.close()
        return output

    @classmethod
    def viewUserHalls(cls, userObj):
        """This is a class method returns list of owner halls
            Args: Object of User type
            Raises:
            Returns: list of tuples
        """
        conn = sqlite3.connect(Hall.dbFileName)
        c = conn.cursor()
        ownerId = userObj.getRowId()
        c.execute("SELECT rowid,* from halls WHERE ownerId = :ownerId",{'ownerId': ownerId,})
        output = c.fetchall()
        conn.close()
        return output

    @classmethod
    def viewHallDetails(cls,rowId):
        """This is a class method returns hall details
            Args: rowid
            Raises:
            Returns: tuples of hall details
        """
        conn = sqlite3.connect(Hall.dbFileName)
        c = conn.cursor()
        c.execute("""SELECT rowid, * FROM halls WHERE rowid = :rowId""",{'rowId' : rowId, })
        output = c.fetchone()
        #print(output)
        #print(type(output))
        conn.close()
        return output


    @classmethod
    def hallExists(cls, hallName, userObj):
        """This is a class method returns list of owner halls
            Args: Object of User type
            Raises:
            Returns: list of tuples
        """
        conn = sqlite3.connect(Hall.dbFileName)
        c = conn.cursor()
        ownerId = userObj.getRowId()
        c.execute("SELECT count(*) FROM halls WHERE ownerId = :ownerId AND hallName = :hallName",{'ownerId': ownerId, 'hallName': hallName})
        data = c.fetchone()[0]
        if data == 0:
            return False
        else:
            return True

    @classmethod
    def deletehall(cls,rowId):
        """This is a class method returns list of owner halls
            Args: Object of User type
            Raises:
            Returns: list of tuples
        """
        conn = sqlite3.connect(Hall.dbFileName)
        c = conn.cursor()
        with conn:
            c.execute("""DELETE FROM halls WHERE rowid = :rowId""",{'rowId' : rowId, })
        output = c.fetchone()
        #print(output)
        #print(type(output))
        conn.close()
        return output


    @classmethod
    def modifyhall(cls,rowId, hallInfo):
        """This is a class method returns list of owner halls
            Args: Object of User type
            Raises:
            Returns: list of tuples
        """
        conn = sqlite3.connect(Hall.dbFileName)
        c = conn.cursor()
        with conn:
            c.execute("""UPDATE halls SET hallName = :hallName, dayTariff = :dayTariff, hallType = :hallType, hallAddr = :hallAddr, hallCapacity = :hallCapacity WHERE rowid = :rowId""",
                    {'rowId' : rowId, 'hallName': hallInfo['hallName'], 'hallType': hallInfo['hallType'], 'hallAddr': hallInfo['hallAddr'], 'hallCapacity': hallInfo['hallCapacity'], 'dayTariff': hallInfo['dayTariff']})
        output = c.fetchone()
        #print(output)
        #print(type(output))
        conn.close()
        return output
