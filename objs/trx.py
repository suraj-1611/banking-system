import config
from datetime import datetime

ZERO_BYTES = 0

class Transaction:

    @staticmethod
    def RecordTrx (deposit: bool, account_number: int, account_name: str, amount: float) -> bool :
        deposit_str = "Deposit" if deposit else "Withdraw"
        entry_str = f"{datetime.now().strftime('%Y-%m-%d')},{account_number},{deposit_str},{amount:.2f}\n"
        with open (config.TRX_FILE, "a") as f:
            return f.write(entry_str) != ZERO_BYTES