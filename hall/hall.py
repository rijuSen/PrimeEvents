#class for hall in prime events
import sqlite3
from pathlib import Path

class Hall:
    '''docstring'''

    #class variable to define the path to the DB file
    dbFileName = "databaseFiles/primeEventsDb.db"
    def insertIntoHallDb(self,hallName,ownerId,hallType,hallAddr,hallCapacity):
        try:
            conn = sqlite3.connect(Hall.dbFileName)
            c = conn.cursor()
            with conn:
                c.execute("INSERT INTO halls VALUES (:hallName, :ownerId, :hallType, :hallAddr, :hallCapacity)",
                        {'hallName': hallName, 'ownerId': ownerId, 'hallType': hallType, 'hallAddr': hallAddr, 'hallCapacity': hallCapacity})

            c.execute("SELECT rowid from halls WHERE hallName = :hallName AND ownerId = :ownerId",{'hallName': hallName,'ownerId': ownerId})
            #save the rowid of the inserted row in the variable rowId
            for id in c.fetchone():
                self.rowId = id

        except sqlite3.Error as sqlite3Error:
            print("SQLite3 Error : -->",sqlite3Error)
        finally:
            conn.close()


    def __init__(self,hallInfo):
        self.hallName = hallInfo['hallName']
        self.ownerId = hallInfo['ownerId']
        self.hallType = hallInfo['hallType']
        self.hallAddr = hallInfo['hallAddr']
        self.hallCapacity = hallInfo['hallCapacity']
        self.dbFilePath = Path(Hall.dbFileName)
        #check if database file already exists
        if not self.dbFilePath.is_file():
            print('Database file not created, run User class to create database files')
        else:
            conn = sqlite3.connect(Hall.dbFileName)
            c = conn.cursor()
            #check if table halls exists in the database
            c.execute('select name from sqlite_master where type = "table"')
            temp = c.fetchall()
            tablePresentFlag = False
            for tup in temp:
                for val in tup:
                    if 'halls' in val:
                        tablePresentFlag = True

            #if doesn't exist create table else insert into existing table
            if not tablePresentFlag:
                c.execute("""CREATE TABLE halls (
                            hallName text NOT NULL,
                            ownerId int,
                            hallType text NOT NULL,
                            hallAddr text NOT NULL,
                            hallCapacity int NOT NULL,
                            UNIQUE(hallName,ownerId),
                            FOREIGN KEY(ownerId) REFERENCES users(rowid))
                            """)
            else:
                self.insertIntoHallDb(self.hallName,self.ownerId,self.hallType,self.hallAddr,self.hallCapacity)
            conn.close()

    @classmethod
    def editHall(cls,editHallOfOwnerId,editHallName,hallName,hallType,hallAddr,hallCapacity):
        """Except ownerId rest all attributes can be modified"""
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

    def getHallAddrs():
        return self.hallAddr

    def getHallCapacity():
        return hallCapacity


    @classmethod
    def viewAllHalls(cls):
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
        conn = sqlite3.connect(Hall.dbFileName)
        c = conn.cursor()
        ownerId = userObj.getRowId()
        c.execute("SELECT rowid,* from halls WHERE ownerId = :ownerId",{'ownerId': ownerId,})
        output = c.fetchall()
        conn.close()
        return output

    @classmethod
    def viewHallDetails(cls,rowId):
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
        conn = sqlite3.connect(Hall.dbFileName)
        c = conn.cursor()
        ownerId = userObj.getRowId()
        c.execute("SELECT count(*) FROM halls WHERE ownerId = :ownerId AND hallName = :hallName",{'ownerId': ownerId, 'hallName': hallName})
        data = c.fetchone()[0]
        if data == 0:
            return False
        else:
            return True
