from bank_account import BankAccount

class User:
    def __init__ (self, name, email):
        self.name = name
        self.email = email
        self.account = []

    def add_account(self):
        self.account.append(BankAccount())

    def make_deposit(self, index, amount):
        self.account[index].deposit(amount)
        print(f"{self.name} deposit {amount}")
        return self

    def make_withdraw(self, index, amount):
        if self.account[index].balance > amount:
            self.account[index].withdraw(amount)
            print(f"{self.name} withdraw {amount}")
        else:
            self.account[index].balance -= 35
            print("Insufficient Funds - Charging $35")
        return self

    def add_interest(self, index):
        self.account[index].yield_interest()
        return self

    def display_user_balance(self, index):
        print(f"{self.name}'s Balance: {self.account[index].balance}")
        return self

    def transfer_money(self, index, recipient, index2, amount):
        if recipient.account[index2] & self.account[index]:
            self.account[index].balance -= amount
            recipient.account[index2].balance += amount
            print(self.name + " transfer: ",amount," to " + recipient.name)
        else:
            print("Invalid Account")
        
        return self


duy = User("Duy","d@gmail.com")
giao = User("Giao","g@gmail.com")

duy.add_account()
duy.make_deposit(0,500).make_deposit(0,200).make_deposit(0,300).make_withdraw(0,450).add_interest(0).display_user_balance(0)

duy.add_account()
duy.make_deposit(1,5000).make_withdraw(1,2000).make_deposit(0,2000).display_user_balance(0).display_user_balance(1)
# giao.make_deposit(500).make_deposit(1000).make_withdraw(100).make_withdraw(300).make_withdraw(450).add_interest().display_user_balance()