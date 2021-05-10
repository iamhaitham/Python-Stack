class BankAccount:
  def __init__(self,interest_rate,balance=0):
    self.interest_rate=interest_rate
    self.balance=balance
      
  def deposit(self, amount):
    self.balance+=amount
    return self
    
  def withdraw(self, amount):
    if self.balance-amount>0:
      self.balance-=amount
      return self
    else:
      print("Insufficient funds: Charging a $5 fee")
      self.balance=self.balance-amount-5
      
  def display_account_info(self):
    print("Balance: ${}".format(self.balance))
    
  def yield_interest(self):
    if self.balance>0:
      self.balance=self.balance+(self.balance*self.interest_rate)
      return self
    else:
      return False
      
class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.account=BankAccount(0.01)   #balance is 0 by default as definer. However, interest rate must be defined by the user as defined. 
    
    def make_deposit(self,amount):
        self.account.deposit(amount)
        
    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
    
    def display_user_balance(self):
        self.account.display_account_info()
      
Haitham=User("Haitham","H@gmail.com")
Omar=User("Omar","O@gmail.com")

Haitham.make_deposit(100)
Haitham.make_withdrawal(20)
Haitham.display_user_balance()