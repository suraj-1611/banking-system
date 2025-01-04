from pathlib import Path

ACCOUNT_FILE = Path(__file__).parent.parent / "files" / "accounts.txt"
TRX_FILE     = Path(__file__).parent.parent / "files" / "transcations.txt"

LOGIN    = 1
CREATE   = 2
EXIT     = 3

DEPOSIT  = 1
WITHDRAW = 2
LOGOUT   = 3