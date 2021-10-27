from credential import Credentials
from user import User

def create_user(name, password):
    """
    create a new user
    """
    new_user = User(username=name, password=password)
    return new_user

def save_user(user):
    """
    save user 
    """
    user.append_user()


def main():
    while True:
        print("sign => to login to app")
        print("x => to logout")
        user_choice = input().lower()
         
        if user_choice == 'sign':
            print("welcome")
            username = input("enter your username: ")
            password = input("enter your password: ")
            save_user(create_user (username, password))

            print("loading...")
            print(f"Congrats {username}, your account was logged")
        elif user_choice == 'x':
            print("bye")
            break


if __name__ == '__main__':
    main()
