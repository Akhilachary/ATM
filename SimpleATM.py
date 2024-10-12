class BankAccount:
    def __init__(self,name,balanc=0):
        self.account_holder_name=name
        self.balance=balanc
    def deposit(self,amount):
        self.balance=self.balance+ amount
        print(f"Deposited {amount} successfully!.")
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -=amount
            print("Withdrawal successful. Please take your cash!")
    def show_balance(self):
        return f"Account holder name:{self.account_holder_name}\nBalance:{self.balance}"
    def options(self):
        print("1.Deposit")
        print("2.Withdraw")
        print("3.Show Balance")
        print("4.Exit")
        chc = int(input("Enter your Choice(1-4): "))
        return chc
choicee=True
customer=BankAccount("Akhila chary",1000)
while(choicee):
    print("********************************************")
    print("Welcome to the Python based ATM!!..")
    print("********************************************")
    custmr_choice=customer.options()
    if custmr_choice==1:
        amount=int(input("Enter Amount you want to deposit: "))
        customer.deposit(amount)
    elif custmr_choice==2:
        amount = int(input("Enter Amount you want to withdraw: "))
        customer.withdraw(amount)
    elif custmr_choice==3:
        print(customer.show_balance())
    elif custmr_choice==4:
        print("Thank you! visit again.")
        choicee=False
    else:
        print("Invalid choice!.")



