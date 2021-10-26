class User:
    """
    class that generates new instance of User
    """
    user_data = []

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def store_data(self):
        """
        method to save user in a list
        """
        User.user_data.append(self)  

x = User("James","@#$%")
x.store_data()
print(x.username)
print(x.password)