class BankAccount:

  def __init__(self,account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance


  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      # self.__account_balance = self.__account_balance+amount
      print("deposited ₹{}. new balance: ₹{}". format(amount,self.__account_balance))

    else:
      print("invalid deposit amount.")

    
  def withdraw(self, amount):  
    if amount>0and amount<= self.__account_balance:
      self.__account_balance-=amount 
      print("withdraw ₹{}.New balance: ₹{}".
       format(amount,self.__account_balance))
    
    else:
      print("invalid withdrawal amount or insufficient balance.")
        
  def display_balance(self):
     print("Account balance for {}(Account #{}):₹  {}".format(     
     self._account_holder_name,self.account_number, self._account_balance))
  def display_balance(self):
    print("Account balance for {} (account #{}: ₹{}".format(self.__account_holder_name, self.__account_number, self.__account_balance))


#create an instance of the background class
account = BankAccount(account_number="123456789", account_holder_name='thilaga',initial_balance=5000.0)


# test deposit and withdrawl functionality
account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.display_balance()
