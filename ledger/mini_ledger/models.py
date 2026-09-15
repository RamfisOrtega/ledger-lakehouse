from dataclasses import dataclass
from datetime import datetime
from enum import Enum

@dataclass
class Transaction:
    txn_id: str
    account_id: str
    timestamp: datetime
    amount: float
    currency: str
    merchant: str
    category: str


class ReasonCode(Enum):
    MISSING_TXN_ID      = "MISSING_TXN_ID"
    MISSING_ACCOUNT_ID  = "MISSING_ACCOUNT_ID"
    INVALID_TIMESTAMP   = "INVALID_TIMESTAMP"
    INVALID_AMOUNT      = "INVALID_AMOUNT"
    INVALID_CURRENCY    = "INVALID_CURRENCY"
    MISSING_RATE        = "MISSING_RATE"