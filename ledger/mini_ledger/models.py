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

class ReasonCodeDetails(Enum):
    MISSING_TXN_ID      = "Transaction ID is missing or empty."
    MISSING_ACCOUNT_ID  = "Account ID is missing or empty."
    INVALID_TIMESTAMP   = "Timestamp format is invalid or cannot be parsed."
    INVALID_AMOUNT      = "Amount is not a valid decimal number."
    INVALID_CURRENCY    = "Currency code is invalid or unsupported."
    MISSING_RATE        = "Exchange rate for the given currency is missing."

class AllowedCurrency(Enum):
    USD = "USD"
    CHF = "CHF"
    EUR = "EUR"
    GBP = "GBP"

@dataclass
class DeadLetterRecord:
    reason_code: ReasonCode
    record: Record
    detail: ReasonCodeDetails | None = None


