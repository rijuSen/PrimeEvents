#class for user in prime events

class User:

    def __init__(self,firstName,lastName,email,password):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password


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


    #OBJECT_INSTANCE = User('FIRSTNAME', 'LASTNAME', 'EMAILID', 'PASSWORD')
    #to call use User.fullName(OBJECT_INSTANCE)

