from datetime import datetime
from decimal import Decimal, InvalidOperation

from ledger.mini_ledger.models import DeadLetterRecord, Record, ReasonCode, Transaction, ReasonCodeDetails



class TransactionValidator:
    """Validates a raw CSV row. Returns None if valid, else a DeadLetterRecord."""

    def __init__(self):
        self.deadLetterRecordList = []

    def validate(self, raw: dict) -> DeadLetterRecord | Transaction:
        record = Record(**raw)
        failures: list[DeadLetterRecord] = []
        


        if not record.txn_id.strip():
            deadLetterRecordObj =  DeadLetterRecord(ReasonCode.MISSING_TXN_ID, record, ReasonCodeDetails.MISSING_TXN_ID)
            failures.append(deadLetterRecordObj)
            

        if not record.account_id.strip():
            deadLetterRecordObj =  DeadLetterRecord(ReasonCode.MISSING_ACCOUNT_ID, record, ReasonCodeDetails.MISSING_ACCOUNT_ID)
            failures.append(deadLetterRecordObj)

    
        if self._convert_amount(record.amount) is None:
            deadLetterRecordObj = DeadLetterRecord(
                ReasonCode.INVALID_AMOUNT, record, ReasonCodeDetails.INVALID_AMOUNT
            )
            failures.append(deadLetterRecordObj)



        if failures:
            return failures

    def _convert_amount(self, raw_amount: str) -> Decimal | None:
        try:
            amount = Decimal(raw_amount)
        except InvalidOperation:
            return None

        if not amount.is_finite():
            return None
        if amount <= 0:
            return None
        if -amount.as_tuple().exponent > 2:


            
            return None

        return amount
