import sys
import functions as fc
import user as us

#main _function

#free function banabo - run_app


#core runs it aall


while(True):
    print("1 -- Create Account \n2 -- Withdraw Money  \n3 -- Deposit Money  \n4 -- Showbalance     \n5 -- exit")
    choice = int(input("Enter the choice:"))

    if choice ==5:
        sys.exit()

    elif choice == 1:
        us.create_acc()
        print("Account has been created:")

    elif choice == 2:
        amt = int(input("Enter the amount you want to withdraw:"))
        print("The Balance after withdraw is:",fc.function.withdraw(amt))
    
    elif choice == 3:
        amt = int(input("Enter the amount you want to Deposit: "))
        print("The Balance after deposit is:",fc.function.deposit(amt))

    elif choice == 4:
        print("The vaibale balance is:",fc.function.availbal(balance=0))

    else:
        print("Enter a valid choice:")