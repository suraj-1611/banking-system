import hashlib
import config
from trx import Transaction

CurrentAccountID = 1001 + len (open (config.ACCOUNT_FILE, "r").readlines())
ZERO_BYTES = 0

class Account:

    name     : str
    balance  : float
    account_number : str

    def __init__(self):
        self.name = None
        self.balance = 0
        self.account_number = None

    def Login(self, account_number: str, password: str) -> bool:
        with open (config.ACCOUNT_FILE, "r") as acc_file:

            accounts = acc_file.readlines()

            if len (accounts) == 0:
                print ("No accounts found")
                return False
            
            hashed_password = hashlib.md5(password.encode()).hexdigest()
            
            for line in accounts:
                acc_number, acc_name, acc_password, acc_balance = line.split(",")
                if acc_number == account_number and hashed_password == acc_password:
                    self.account_number = acc_number
                    self.name    = acc_name
                    self.balance = float(acc_balance)
                    return True
        return False
    
    def Logout(self):
        with open(config.ACCOUNT_FILE, "r") as accounts:
            accounts_list = accounts.readlines()
        
        # Open file in write mode to update content
        with open(config.ACCOUNT_FILE, "w") as accounts:
            for line in accounts_list:
                acc_number, acc_name, acc_password, acc_balance = line.split(",")
                if acc_number == self.account_number:
                    # Update balance only for matching account
                    accounts.write(f"{acc_number},{acc_name},{acc_password},{float(self.balance):.2f}\n")
                else:
                    # Keep other accounts unchanged
                    accounts.write(line)
        
        self.name = None
        self.balance = 0
        self.account_number = None
    
    @staticmethod 
    def CreateAccount(name: str, password: str) -> 'Account' :
        global CurrentAccountID
        
        acc = Account ()
        
        acc.name     = name
        acc.balance  = 0
        acc.account_number = str(CurrentAccountID)

        with open (config.ACCOUNT_FILE, "a") as f:
            hashed_password = hashlib.md5(password.encode()).hexdigest()
            entry_str = f"{acc.account_number},{acc.name},{hashed_password},{acc.balance}\n"
            if f.write(entry_str) == ZERO_BYTES:
                print ("Error creating account")
            else:
                CurrentAccountID += 1

        return acc

    def Withdraw(self, amount: float) -> bool:
        if (self.balance > amount):
            if Transaction.RecordTrx(False, self.account_number, self.name, amount) == True:
                self.balance -= amount
                return True
            else: return False
        
        else: return False

    def Deposit(self, amount: float) -> bool:
        if Transaction.RecordTrx(True, self.account_number, self.name, amount) == True:
            self.balance += amount
            return True
        else: return False

    def __str__(self):
        return f'{self.name}: {self.account_number}'