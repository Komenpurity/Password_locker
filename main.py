from credential import Credentials
from user import User

def main():
    while True:
        user_choice = input().lower()
        print(user_choice)
        if user_choice == 'sign':
            print("welcome")
        elif user_choice == 'x':
            print("bye")
            break
            

if __name__ == '__main__':
    main()
