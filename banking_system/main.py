# 241127 폴더에서 python -m banking_system.main 으로 실행

from banking_system.services.banking_service import BankingService

def main() -> None :
    service = BankingService()
    
    while True:
        choice = input("작업을 입력하세요(1:사용자추가, 2:사용자찾기, 3:종료) : ")
        
        if choice == '1':
            name = input("추가할 사용자 이름을 입력해주세요 : ")
            service.add_user(name)

        elif choice == '2':
            name = input("사용자 이름을 입력해주세요 : ")
            service.user_menu(name)
    
        elif choice == '3':
            break 
        
        else:
            print("번호를 잘못 입력했습니다. 다시 입력해주세요") 
main()