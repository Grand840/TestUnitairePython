from bank import Account

def test_account_creation():
    account_01 = Account(identifier="000", balance=100)
    account_02 = Account(identifier="000", balance=-100)
    assert account_01.balance == 100 
    assert account_02.balance == -100