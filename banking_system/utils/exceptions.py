class InsufficientFundsError(Exception):
    def __init__(self, balance:int) -> None:
        super().__init__(f"잔액이 부족합니다. 현재 잔액은 {balance}원 입니다.")

class NegativeAmountError(Exception):
    def __init__(self) -> None:
        super().__init__(f"음수를 입력하지마세요")
        
class UserNotFoundError(Exception):
    def __init__(self, username:str) -> None:
        super().__init__(f"{username} 사용자를 찾을 수 없습니다.")