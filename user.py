



class user():

    
    def __init__(self, name,age,balance=0):
        self.name = name
        self.age = age
        self.balance = balance
        
        
        
def create_acc():
    print("Enter your details below:")
    name = input("Enter the name:")
    balance = int(input("Enter the starting balance:₹"))
    age = input("Enter your age:")
    cust = user(name,age,balance)
    print(cust)
    return cust


def show_user_details(self):
    print("Account holder details")
    print("Name",self.name)
    print("Age",self.age)
    print("balance",self.balance)



    




#print(user1.show_user_details())



