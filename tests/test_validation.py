
import pytest
from ledger.mini_ledger.validator import TransactionValidator
from ledger.mini_ledger.models import Transaction, DeadLetterRecord, ReasonCode

@pytest.fixture
def valid_raw_record() -> dict:
    return {
        "txn_id": "t1",
        "account_id": "A1",
        "timestamp": "2026-04-28T10:15:00Z",
        "amount": "100.00",
        "currency": "USD",
        "merchant": "Amazon",
        "category": "retail"
    }


@pytest.fixture
def validator() -> TransactionValidator:
    return TransactionValidator()

def test_missing_txn_id_is_rejected(validator: TransactionValidator, valid_raw_record: dict):
    valid_raw_record["txn_id"] = ""
    result = validator.validate(valid_raw_record)
    assert result.reason_code == ReasonCode.MISSING_TXN_ID

def test_missing_account_id_is_rejected(validator: TransactionValidator, valid_raw_record:dict):
    valid_raw_record["account_id"] = ""
    result = validator.validate(valid_raw_record)
    assert result.reason_code == ReasonCode.MISSING_ACCOUNT_ID

def test_from_record_to_transaction(validator: TransactionValidator, valid_raw_record: dict):
    result = validator.validate(valid_raw_record)
    assert isinstance(result, Transaction)