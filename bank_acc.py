class BalanceException(Exception):
    pass    

class BankAccount:

    def __init__(self, amount, name) -> None:
        self.balance = amount
        self.name =  name 
        print(f"\nA new account is created. Account information is given below.\nAccount name = '{self.name}'. \nBalance = ${self.balance:.2f}")

    
    def check_balance(self):
        print(f"{self.name}'s account balance is: {self.balance:.2f}")
    
    def deposit(self, dep_amount):
        self.balance = self.balance + dep_amount
        print(f"The amount {dep_amount} has been deposited to {self.name}'s account.")
        self.check_balance()

    def viable_transaction(self, amount):
        if amount > self.balance:
            raise BalanceException(f"\n{self.name}'s account balance is ${self.balance}")
        else:
            return   

    
    def withdraw(self, withdraw_amount):
        try:
            self.viable_transaction(withdraw_amount)
            self.balance = self.balance - withdraw_amount
            print("Withdraw complete.")
            self.check_balance()
        except BalanceException as error:
            print(f"\nwithdraw interrupted: {error}")
            
    def money_transfer(self, amount, account):
        try:
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f"amount {amount} has been succesfully transferred to {account.name}'s account from {self.name}'s account")
        except BalanceException as error:
            print(f"\nTransfer interrupted!: {error}")   


#################......Calculate Interest........##########################
class interestReward(BankAccount):

    def deposit(self, dep_amount):
        self.balance = self.balance + (1.05 * dep_amount) 
        print("Deposit complete")
        self.check_balance()


###############...........Calculate Service Charge..........#############
class ServiceCharge(interestReward):

    def __init__(self, amount, name) -> None:
        super().__init__(amount, name)
        self.fee = 0 

    def withdraw(self, withdraw_amount):
        try:
            self.viable_transaction(withdraw_amount)
            if withdraw_amount >= 1000: 
                self.fee = self.fee + ((withdraw_amount // 1000) * 5)
            self.balance = self.balance - (withdraw_amount + self.fee)
            print("Withdraw complete")
            self.check_balance()
        except BalanceException as error:
            print(f"\nTransfer interrupted!: {error}")   
    