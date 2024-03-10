class InsufficientFundsError(Exception):
    def __init__(self, message = "The balance is insufficient") -> None:
        super().__init__(message)