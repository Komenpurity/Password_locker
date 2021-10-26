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
    