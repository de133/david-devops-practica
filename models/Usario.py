import uuid

class User:
    def __init__(self, name: str, email: str):
        self.uid = uuid.uuid4()
        self.name = name
        self.email = email
    
    def is_admin(self):
        return False
    
class Client(User):
    def __init__(self, name: str, email: str, address: str):
        super().__init__(name, email)
        self.address = address

class Admin(User):
    def __init__(self, name: str, email: str):
        super().__init__(name, email)

    def is_admin(self):
        return True