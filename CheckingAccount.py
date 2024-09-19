from BankAccount import *

class Checkings(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, routing_num, account_num):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.__routing_num = routing_num
        self.__account_num = account_num
    
    def transfer_lim(self,amount):
       # will only lets user to transfer 50% of currrent balance
       limit = self.getBalance() * .50

       if amount <= limit:
           self.getBalance -= amount
           print(f"${limit:.2f} being transferred")
       else:
           print("Please withdraw a lower amount")
           

       
