class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
        self.__interest_rate = 5.0
    def get_balance(self):
        return self.__balance
    
    def get_interest_rate(self):
        return self.__interest_rate

class HDFC(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)

    def AC_balance(self):
       print("Account Balance = ", self.get_balance())

    def Interest_Rate(self):
        print("Interest Rate = ", self.get_interest_rate()) 

hdfc = HDFC(5000)
hdfc.AC_balance()
hdfc.Interest_Rate()