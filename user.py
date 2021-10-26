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

    @classmethod
    def display_data(cls):
        """
        method to display data in the list
        """
        return User.user_data

    @classmethod
    def single_instance(cls):
        """

        """
        list = cls.user_data
        for i in list:
            print(i.__dict__)


x = User("James","@#$%")
x.store_data()
print(x.username)
print(x.user_data)
x.single_instance()