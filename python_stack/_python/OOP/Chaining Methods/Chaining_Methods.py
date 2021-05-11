class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.balance=0
    
    def make_deposit(self,value):
        self.balance+=value
        return self
        
    def make_withdrawal(self, amount):
        self.balance-=amount
        return self
        
    def display_user_balance(self):
        print("User: {}, Balance: {}".format(self.name,self.balance))
        
        
    def transfer_money(self, other_user, amount):
        self.balance-=amount
        other_user.balance+=amount
        


monty=User("Monty","Monty@gmail.com")
michael=User("Michael","Michael11@yahoo.com")
john=User("John","John.Doe@aol.com")

monty.make_deposit(120).make_deposit(250).make_deposit(30).make_withdrawal(200).display_user_balance()

michael.make_deposit(150).make_deposit(20).make_withdrawal(100).make_withdrawal(50).display_user_balance()

john.make_deposit(180).make_withdrawal(80).make_withdrawal(50).make_withdrawal(50).display_user_balance()

monty.transfer_money(john, 100)
print(monty.display_user_balance())
print(john.display_user_balance())
