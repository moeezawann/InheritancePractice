import BankAccount

class Checkings(BankAccount):
   def __init__(self, customer_name, current_balance, minimum_balance, routing_num, account_num):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.__routing_num = routing_num
        self.__account_num = account_num
