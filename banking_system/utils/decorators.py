from typing import Callable
from banking_system.utils.exceptions import NegativeAmountError

def validate_transaction(func: Callable) -> Callable:
    def wrapper(self, amount: int) -> None:
        if amount <= 0:
            raise NegativeAmountError()
        return func(self, amount)
    return wrapper