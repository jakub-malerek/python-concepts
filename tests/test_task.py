import pytest
from source.task import BankAccount, InsufficientFundsError

# Fixture for Account Creation
@pytest.fixture
def new_account():
    """Create a new BankAccount object."""
    return BankAccount("1234567890", "John Doe", 100.0)

# Parameterized Test for Deposits
@pytest.mark.parametrize("initial_balance,deposit_amount,expected_balance", [
    (100, 50, 150),
    (200, 75, 275),
    (50, 25, 75),
])
def test_deposit(new_account, initial_balance, deposit_amount, expected_balance):
    new_account.balance = initial_balance  # Set initial balance
    new_account.deposit(deposit_amount)
    assert new_account.balance == expected_balance

# Parameterized Test for Withdrawals
@pytest.mark.parametrize("initial_balance,withdraw_amount,expected_balance", [
    (100, 50, 50),
    (200, 20, 180),
    (300, 70, 230),
])
def test_withdrawal_sufficient_funds(new_account, initial_balance, withdraw_amount, expected_balance):
    new_account.balance = initial_balance  # Set initial balance
    new_account.withdraw(withdraw_amount)
    assert new_account.balance == expected_balance

# Test Withdrawal with Insufficient Funds using the same fixture
def test_withdrawal_insufficient_funds(new_account):
    new_account.balance = 50  # Ensure the account has a specific balance
    with pytest.raises(InsufficientFundsError):
        new_account.withdraw(100)

# Fixture for Clearing Transaction Logs
@pytest.fixture(autouse=True)
def clear_transaction_logs():
    """Clear the transaction logs before each test."""
    BankAccount.transaction_logs = []
    yield  # Provide a setup and teardown mechanism

# Test Transfer with Parameterization
@pytest.mark.parametrize("transfer_amount,expected_balances", [
    (30, (70, 130)),
    (50, (50, 150)),
    (10, (90, 110)),
])
def test_transfer_sufficient_funds(new_account, transfer_amount, expected_balances):
    other_account = BankAccount("0987654321", "Jane Doe", 100.0)
    new_account.transfer(transfer_amount, other_account)
    assert new_account.balance == expected_balances[0]
    assert other_account.balance == expected_balances[1]

# Continue with more advanced tests as needed...

