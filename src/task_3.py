class BankAccount:
    def __init__(self,acc_num, balance):

        self.acc_num= acc_num
        self.balance= balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        self.balance -= amount
        
class SavingsAccount(BankAccount):
    def __init__(self,acc_num, balance, interest_rate):
        super(SavingsAccount, self).__init__(acc_num, balance)
        self.interest_rate= interest_rate
        

    def next_month(self):
        self.balance += self.balance * self.interest_rate

    def __str__(self):
        return f"number: {self.acc_num}\tbalance:{self.balance}\trate:{self.interest_rate}"

class CheckingAccount(BankAccount):
    
    def __init__(self,acc_num, balance, no_transaction):
        super().__init__(acc_num, balance)
        self.no_transaction= no_transaction
        self.transaction_count = 0 

    def deposit(self, amount):
        if self.no_transaction > self.transaction_count:
            super().deposit(amount)
            self.transaction_count += 1
        else:
            print("No more transactions available")
        
    def withdraw(self, amount):
        if self.no_transaction > self.transaction_count:
            super().withdraw(amount)
            self.transaction_count += 1
        else:
            print("No more transactions available")

    def next_month(self):
        self.transaction_count = 0 

    def __str__(self):
        return f"number: {self.acc_num}\tbalance:{self.balance}\trate:{self.no_transaction}"