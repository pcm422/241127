class Transaction:
    def __init__(self, transaction_type:str, amount:int, balance:int) -> None:
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance = balance
        
    def __str__(self) -> str:
        return f"{self.amount}원을 {self.transaction_type}하여 잔액은 {self.balance}원입니다"
    
    def to_tuple(self) -> tuple:
        return self.transaction_type, self.amount, self.balance