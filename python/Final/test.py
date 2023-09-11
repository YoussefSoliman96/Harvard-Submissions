from datetime import datetime
from enum import StrEnum, auto

class TransactionType(enum):
    Deposit = auto()
    Withdraw = auto()


Transaction = tuple [TransactionType, datetime, int]