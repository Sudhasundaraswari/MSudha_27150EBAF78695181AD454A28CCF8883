class BankAccount:
 def 
  init(self,account_number,account_hold  er_name,
initial_balance=0.0):
   self.__account_number=account_number   
self.__account_holder_name=account_holder_name
       self._account_balance=initial_balance

       def deposit(self,amount):
         if amount > 0:
           self._account_balance +=
amount
      print( "Deposited ₹{}.Newbalance:₹{}".format(amount,self.__account_balance))
      else:
        print("invalid deposit amount.please deposite a positive amount")


 def withdraw(self,amount):
  if amount > 0 and amount <=
self._amount_balance:
   self._account_balance-=
amount
     print("withdraw₹{}.New
balance:₹{}".format(amount,
self._account_balance))
    else:
     print("invalid withdrawal
amount or insufficient balance.")

  def display_balance(self):
     print("Account balance for {}
  (Account#{}):₹{}".format(
     self._account_holder_name,
  self._account_number,
  self._account_balance))

 account=BankAccount(account_number="123456789",  account_holder_name="jawajami",initial_balance=5000.0)
account.display_balance();
account.deposit(500.0)
  
     
   