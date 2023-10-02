import time

class BalanceException(Exception):
    pass 


class Atm:

    #static/shared variable
    __counter = 1

    def __init__(self):
        # instance variable
        self.__pin = ""
        self.__balance = 0
        self.serial = Atm.__counter
        Atm.__counter = Atm.__counter + 1

        self.create_pin()

        user_input = input("Please enter your PIN : ")
        if user_input == self.__pin:
            self.__menu()
        else: 
            print("Wrong PIN")

    @staticmethod
    def get_counter():
        return Atm.__counter
    
    @staticmethod
    def set_counter(new):
        if type(new) == int:
            Atm.__counter = new
        else:
            print("Invalid Input") 

    def get_pin(self):
        return self.__pin
    
    def set_pin(self, new_pin):
        if type(new_pin) == str:
            self.__pin = new_pin
            print("pin changed successfully")
        else:
            print("invalid input")
        
    def __menu(self):

        user_input = int(input(""" please select below options
        1: check balance
        2. deposit
        3. withdraw
        4. exit
    """))
        
        if user_input == 1:
            self.check_balance()
        if user_input == 2:
            self.deposit()
        if user_input == 3:
            self.withdraw()
        if user_input == 4:
            self.exit()
        else:
            raise BalanceException("Invalid input")


    
    def create_pin(self):
        user_input = input("Please enter your pin to set: ")
        self.__pin = user_input
        print ("Pin is set successfully")
    
    def check_balance(self):
        print("Your account balance is: ", self.__balance)
        time.sleep(5)
        self.__menu()
  
    def deposit(self):
        given_amount = int(input("Please enter the amount: "))
        self.__balance = self.__balance + given_amount
        print("Amount has been deposited successfully")
        time.sleep(5)
        self.__menu()
    
    def withdraw(self):
        given_amount = int(input("Please enter the amount: "))
        if given_amount <= self.__balance:
            self.__balance = self.__balance - given_amount
            print("Amount has been withdrawn successfully")
        else:
            print("Insufficient fund")  
        time.sleep(5)
        self.__menu()
    
    def exit(self):
        print("Thank you")