class InsufficientFundsError(Exception):
    def __init__(self, message = "The balance is insufficient") -> None:
        super().__init__(message)

class BankAccount():

    transaction_logs = []

    def __init__(self,account_number:str,owner_name:str,balance:float) -> None:
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance 
        self.currency = "USD"

    @staticmethod
    def check_balance(func):
        def wrapper(self,*args,**kwargs):
            if self.balance >= args[0]:
                func(self,*args,**kwargs)
            else:
                raise InsufficientFundsError()
        return wrapper
    
    @staticmethod
    def log_transactions(func):
        def wrapper(self,*args):

            def safe_args_index(args):
                if len(args) > 1:
                    return args
                return [args[0],None]
            
            func(self,*args)
            
            args = safe_args_index(args)

            BankAccount.transaction_logs.append(f"transaction: {func.__name__}, amount: {args[0]}, another_account: {args[1]},new_balance: {self.balance}")
        return wrapper
    
    @log_transactions
    def deposit(self,amount):
        self.balance += amount

    @log_transactions
    @check_balance
    def withdraw(self,amount):
        self.balance -= amount

    @log_transactions  
    @check_balance
    def transfer(self,amount,other_account):
        self.withdraw(amount)
        other_account.deposit(amount)
    
    @property
    def balance(self):
        return self.balance_
    
    @balance.setter
    def balance(self,value):
        if value >= 0:
            self.balance_ = value
        else:
            print("The 'balance' cannot be set to a negative value.")
    
    @property
    def account_number(self):
        return self.account_number_
    
    @account_number.setter
    def account_number(self,value):
        if len(value) == 10 and value.isdigit():
            self.account_number_ = value
        else:
            raise ValueError("The 'account_number' should be a string of 10 digits")    

    @property
    def owner_name(self):
        return self.owner_name_ 
    
    @owner_name.setter
    def owner_name(self,value):
        if len(value) >= 3:
            self.owner_name_ = value
        else:
            raise ValueError("The 'owner_name' should be at least 3 characters long")  

    @staticmethod
    def calculate_interest(balance,rate,time):
        return balance*rate*time
    
    def change_base_currency(self,currency):
        currencies = {"USD":1,"EUR":0.97,"PLN":0.47}
        
        if currency in currencies:
            back_to_usd = currencies["USD"]/currencies[currency]
            self.currency = currency
            self.balance = back_to_usd*self.balance*currencies[currency]
        else:
            print("Invalid currency was given, avaible currencies are: USD, EUR, PLN")    





    
             



        

