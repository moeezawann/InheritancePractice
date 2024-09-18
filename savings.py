from BankAccount import *

class savings(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, routingNum, accountNum):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.__routingNum = routingNum
        self.__accountNum = accountNum

    def addInterest(self):
        #add 5 percent interest
        self.deposit(self.getBalance() * .05)


    def printTest():
        print("test")

