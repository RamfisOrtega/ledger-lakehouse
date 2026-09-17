
import pytest
from ledger.mini_ledger.validator import TransactionValidator
from ledger.mini_ledger.models import Transaction, DeadLetterRecord, ReasonCode, ReasonCodeDetails

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
    assert len(result) == 1
    assert result[0].reason_code == ReasonCode.MISSING_TXN_ID

def test_missing_account_id_is_rejected(validator: TransactionValidator, valid_raw_record:dict):
    valid_raw_record["account_id"] = ""
    result = validator.validate(valid_raw_record)
    assert len(result) == 1
    assert result[0].reason_code == ReasonCode.MISSING_ACCOUNT_ID

def test_record_collects_multiple_failures(validator, valid_raw_record):
    valid_raw_record["txn_id"] = ""
    valid_raw_record["account_id"] = ""

    result = validator.validate(valid_raw_record)

    codes = [d.reason_code for d in result]
    assert codes == [ReasonCode.MISSING_TXN_ID, ReasonCode.MISSING_ACCOUNT_ID]
