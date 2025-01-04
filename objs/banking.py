from accounts import Account

class Banking:

    current_account : Account = None

    def __init__(self):
        return

    @property
    def logged_in(self) -> bool:
        return self.current_account is not None

    def CreateAccount(self, name: str, password: str) -> bool:
        return Account.CreateAccount(name, password)

    def Login(self, account_number: str, password: str) -> bool:
        acc = Account ()
        if acc.Login(account_number, password) == True:
            self.current_account = acc
            return True
        else:
            return False
        
    def Logout(self):
        self.current_account.Logout()
        self.current_account = None
        return True
    
    def Deposit(self, amount: float) -> bool:
        if self.current_account is not None:
            return self.current_account.Deposit(amount)
            
    def Withdraw(self, amount: float) -> bool:
        if self.current_account is not None:
            return self.current_account.Withdraw(amount)