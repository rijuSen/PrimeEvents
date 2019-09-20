#class for payment in prime events

class Payment:
    #payment id to be generated
    paymentId = 0
    #number of payment objects created
    numOfPaymentObjects = 0

        
    def __init__(self, paymentType, paymentBank):
        self.paymentType = paymentType
        self.paymentBank = paymentBank
        Payment.numOfPaymentObjects += 1

    def getPaymentType(self):
        return self.paymentType

    def getPaymentBank(self):
        return self.paymentBank

    def deletePayment():
        #delete in database
        pass

    def editPayment(pType,pBank):
        self.paymentType = pType
        self.paymentBank = pBank
        #update in database statement
        
    def getPaymentId():
        #get payment id from database
        pass

    def generatePaymentId():
        #fetch the next available payment id from the database
        pass
    
    #use this method as Payment.selectPaymentMethod to view and select the type of payment methods available
    @classmethod
    def availablePaymentMethod(cls):
        #select from payment method from available methods for Payments
        pass



