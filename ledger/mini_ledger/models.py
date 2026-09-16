from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from enum import Enum

@dataclass
class Transaction:
    txn_id: str
    account_id: str
    timestamp: datetime
    amount: Decimal
    currency: str

@dataclass
class Record:
    txn_id: str
    account_id: str
    timestamp: str
    amount: str
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

@dataclass
class DeadLetterRecord:
    reason_code: ReasonCode
    record : Record
    detail: str | None = None


