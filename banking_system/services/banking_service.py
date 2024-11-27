from banking_system.models.user import User
from banking_system.utils.exceptions import UserNotFoundError
from banking_system.utils.exceptions import InsufficientFundsError
from banking_system.utils.exceptions import NegativeAmountError

class BankingService:
    def __init__(self) -> None:
        self.users = []
    
    def add_user(self, username:str) -> None:
        self.users.append(User(username))
        
    def find_user(self, username:str) -> User:
        for user in self.users:
            if user.username == username:
                return user
        raise UserNotFoundError(username)
    
    def user_menu(self, username:str) -> None:
        try:
            user = self.find_user(username)
        except UserNotFoundError as e:
            print(e)
            return
        
        while True:
            choice = input("작업번호를 입력하세요(1:입금, 2:출금, 3:잔액확인, 4:거래내역확인, 5:종료) : ")
            if choice == '5':
                break
            elif choice == '1':
                amount = int(input("입금할 금액을 입력해주세요 : "))
                try:
                    user.account.deposit(amount)
                except NegativeAmountError as e:
                    print(e)
            elif choice == '2':
                amount = int(input("출금할 금액을 입력해주세요 : "))
                try:
                    user.account.withdraw(amount)
                except InsufficientFundsError as e:
                    print(e)
                except NegativeAmountError as e:
                    print(e)
            elif choice == '3':
                print(f"현재 잔액은 {user.account.get_balance()}원 입니다")
            elif choice == '4':
                for transaction in user.account.get_transactions():
                    print(transaction)
            else:
                print("번호를 잘못 입력했습니다. 다시 입력해주세요") 