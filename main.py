from savings import *
from CheckingAccount import *


# #TEST CHECKING ACCOUNT
# #Have users create a checking account

# #have users withdraw from checking


# #have users deposit into checking

##have user try to withdraw more than they have in checking

#TEST SAVINGS ACCOUNT
#Have users create a savings account
savings1 = savings("Anthony Ramirez", 25, 5, 123456789, 987654321)
savings2 = savings("Robert Ramirez", 15, 10, 111111111, 999999999)

#have users deposit into savings
savings1.deposit(10)
savings2.deposit(15)

#have users withdraw from savings
savings1.withdraw(5)
savings2.withdraw(10)

#have user try to withdraw more than they have from savings
savings1.withdraw(45)
savings2.withdraw(32)

#test print customer info
savings1.print_customer_information()
savings2.print_customer_information()

#test add interest method to savings
savings1.addInterest()
savings2.addInterest()

savings1.print_customer_information()
savings2.print_customer_information()

#TEST Checking ACCOUNT
#Have users create a chekcing account
checking1 = Checkings("Anthony Ramirez", 25, 5, 123456789, 987654321)
checking2 = Checkings("Robert Ramirez", 15, 10, 111111111, 999999999)

#have users deposit into checking
checking1.deposit(4)
checking2.deposit(5)

#have user try to transfer more than they have from checking
checking1.transfer_lim(12)
checking2.transfer_lim(18)
