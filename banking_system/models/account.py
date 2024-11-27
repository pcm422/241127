from banking_system.utils.decorators import validate_transaction
from banking_system.models.transaction import Transaction
from banking_system.utils.exceptions import InsufficientFundsError

class Account:
    bank_name = ''
    
    def __init__(self) -> None:
        self.__balance = 0
        self.transactions = []
    
    @validate_transaction
    def deposit(self, amount: int) -> None:
        self.__balance += amount
        transaction = Transaction("입금", amount, self.__balance)
        self.transactions.append(transaction)
        print(f"{amount}원이 입금 되었습니다.")
    
    @validate_transaction
    def withdraw(self, amount: int) -> None:
        if self.__balance >= amount:
            self.__balance -= amount
            transaction = Transaction("출금", amount, self.__balance)
            self.transactions.append(transaction)
            print(f"{amount}원이 출금 되었습니다.")
        else:
            raise InsufficientFundsError(self.__balance)
            
    def get_balance(self) -> int:
        return self.__balance
    
    def get_transactions(self) -> list:
        return self.transactions
    
    @classmethod
    def get_bank_name(cls) -> str:
        return cls.bank_name
    
    @classmethod
    def set_bank_name(cls, name:str) -> None:
        cls.bank_name = name