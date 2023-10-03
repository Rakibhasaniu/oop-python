class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw=100
        self.max_withdraw=10000 
    def get_balance(self):
        return self.balance
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(self.balance)
            
    def withdraw(self,amount):
        if amount < self.min_withdraw:
            print (f"you can't")
        elif amount > self.max_withdraw:
            print (f'bank fokir hye jabe')
        else :
            self.balance -= amount
            print (f'here is your money{amount}')
dbbl= Bank(15000)
dbbl.deposit(1000)
dbbl.withdraw(200)
result = dbbl.get_balance()
print(result)