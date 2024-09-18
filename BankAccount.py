#Created by Anthony Ramirez
class BankAccount:
    bank_title = "Bank of America"

    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        print("New Bank Account Created")

    def deposit(self, val):
        self.current_balance += val
        print("Deposit of " + str(val) + " was successful")

    def withdraw(self, val):
        if self.current_balance - val < self.minimum_balance:
            print("Cannot withdraw would be below minimum balance")
            return
        else:
            self.current_balance -= val
            print("Withdraw of " + str(val) + " was successful")

    def getBalance(self):
        return self.current_balance

    
    def print_customer_information(self):
        print("Welcome to " + BankAccount.bank_title)
        print("Customer: " + self.customer_name)
        print("Current Balance: " + str(self.current_balance))
        print("Minimum Balance: " + str(self.minimum_balance) + "\n")







#test out code with 2 instances
customerAccount1 = BankAccount("Anthony Ramirez", 25, 5)
#test deposit
customerAccount1.deposit(10)
#test withdraw
customerAccount1.withdraw(5)
#test withdraw over limit
customerAccount1.withdraw(45)
#test print customer info
customerAccount1.print_customer_information()

customerAccount2 = BankAccount("Robert Ramirez", 15, 10)
#test deposit
customerAccount2.deposit(15)
#test withdraw
customerAccount2.withdraw(10)
#test withdraw over limit
customerAccount2.withdraw(32)
#test print customer info
customerAccount2.print_customer_information()