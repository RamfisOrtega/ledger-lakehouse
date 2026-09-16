from datetime import datetime
from decimal import Decimal, InvalidOperation

from ledger.mini_ledger.models import DeadLetterRecord, Record, ReasonCode, Transaction

ALLOWED_CURRENCIES = {"USD", "CHF", "EUR", "GBP"}


class TransactionValidator:
    """Validates a raw CSV row. Returns None if valid, else a DeadLetterRecord."""

    def validate(self, raw: dict) -> DeadLetterRecord | Transaction:
        record = Record(**raw)

        if not record.txn_id.strip():
            return DeadLetterRecord(ReasonCode.MISSING_TXN_ID, record, "txn_id is empty")

        if not record.account_id.strip():
            return DeadLetterRecord(ReasonCode.MISSING_ACCOUNT_ID, record, "account_id is empty")

        