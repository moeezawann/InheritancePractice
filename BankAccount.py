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

    def setBalance(self, newBalance):
        self.current_balance = newBalance
    
    def print_customer_information(self):
        print("Welcome to " + BankAccount.bank_title)
        print("Customer: " + self.customer_name)
        print("Current Balance: " + str(self.current_balance))
        print("Minimum Balance: " + str(self.minimum_balance) + "\n")
