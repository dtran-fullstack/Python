class BankAccount:
    def __init__(self, int_rate=0.02, balance=0):
        self.int_rate = int_rate
        self.balance = balance  
    def deposit(self, amount):
        self.balance += amount
        return self    
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            self.balance -= 35
        return self
    def yield_interest(self):
        self.balance *= (1 + self.int_rate) 
        return self
