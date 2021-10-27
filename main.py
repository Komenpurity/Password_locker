from credential import Credentials
from user import User

def main():
    while True:
        print("sign => to login to app")
        print("x => to logout")
        user_choice = input().lower()
         
        if user_choice == 'sign':
            print("welcome")
        elif user_choice == 'x':
            print("bye")
            break


if __name__ == '__main__':
    main()
