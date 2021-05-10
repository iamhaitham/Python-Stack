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
      
      
John=BankAccount(0.01)
Doe=BankAccount(0.01)

John.deposit(1500).deposit(200).deposit(300).withdraw(900).yield_interest()
John.display_account_info()


Doe.deposit(3200).deposit(200).withdraw(1200).withdraw(2000).withdraw(50).withdraw(140).yield_interest()
Doe.display_account_info()


