 import string
 import random
 
 class Credentials:
     """
     method of generating credentials
     """
     user_cred = []
 
def __init__(self,platform,username,password):
     self.platform = platform
     self.username = username
     self.password = password
    
def append_cred(self):
    """
    method to save credentials
    """
    Credentials.user_cred.append(self)

@classmethod
def generate_password(cls,length):
    characters = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits
    return "".join(random.choice(characters)for i in range(length))