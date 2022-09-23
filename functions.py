import sys
import user as us

class core():

    #create a user dictiuonary

    

    amount =0
   
    def __init__(self,name,balance = 0,) :
        self.name = name
        self.balance = balance
        


    def deposit(self,amount):
        self.balance+= amount
        return self.balance

    def withdraw(self,amount):
        if amount > self.balance:
            print("insufficent funds:")
        else:
            self.balance-= amount
        return self.balance

    def availbal(self,balance):
        return self.balance

    def show_acc_details():
        print()





             

        