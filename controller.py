from user.user import *
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import time
import getpass
import os


def displayTableFormat(output,startIndex):
    print("{0:^5}{1:^10}{2:^10}{3:^10}{4:^10}".format('ID','Hall-Name','Hall-Type','Hall-Addr','Hall-Capacity'))
    for row in output[startIndex:startIndex + 4:1]:
        print("{0:^5}{1:^10}{2:^10}{3:^10}{4:^10}".format(row[0],row[1],row[3],row[4],row[5]))


class Session:
    '''class to maintain a session'''
    def __init__(self, userObj):
        self.userObj = userObj

    def getSessionId(self):
        return self.userObj.getRowId()

    def getUserType(self):
        return self.userObj.getUserType()

    def getFirstName(self):
        return self.userObj.getFirstName()


