import sys

class bank(object):
    #bank related transactions#####

    #initialize the self paramters

    def __init__(self,name ,balance):
        self.name = name
        self.balance = balance


    # to deposit the money
    def deposit(self,amount):
        self.balance+= amount
        return self.balance

    #to withdraw money from balance
    def withdraw(self,amount):
        if amount > self.balance:
            print("insufficient funds:")
        else:
            self.balance -= amount
        return self.balance
    #to show the available balance
    def display(self,balance):
        return self.balance

#creating an object or an account with the bank class
def create_user():
    print("Please enter your details below:")
    NAME = input("enter the name of the acount holder:")
    BAL = int(input("enter the starting balance:"))
    
    
b = bank(NAME,BAL)
while(True):
    print("1 - Deposit Money \n 2 - Withdraw money \n 3 - Show balance  \n -4 Create  User    \n 5 - exit")
    choice = int(input("enter your option"))

    if choice == 5:
        sys.exit()
    elif choice == 1:
        amt = float(input("Enter the amount:"))
        print("balance after Deposit:",b.deposit(amt))
    elif choice == 2:
        amt = float(input("Enter the amount:"))
        print("balance after withdraw:",b.withdraw(amt))
    elif choice == 3:
        print("the available balance is:",b.display(balance=0))
    elif choice == 4:
        create_user()
        print("Account has been created:")

    else:
        print("Choose any of the above options")