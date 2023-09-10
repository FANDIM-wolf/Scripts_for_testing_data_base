
class Client:
    def __init__(self, user_id, FSS, phone, address, email):
        self.user_id = user_id
        self.FSS = FSS
        self.phone = phone
        self.address = address
        self.email = email

    def __str__(self):
        return f"User ID: {self.user_id}, FSS: {self.FSS}, Phone: {self.phone}, Address: {self.address}, Email: {self.email}"

class PrivateData:
    def __init__(self, user_id, password,login):
    
        self.user_id = user_id
        self.password = password
        self.login = login

    def __str__(self):
        return f"ID: {self.id}, User ID: {self.user_id}, Password: {self.password} , Login: {self.login}"
    


class INN_private_data:
    def __init__(self, user_id, inn):
        
        self.user_id = user_id
        self.inn = inn
       

    def __str__(self):
        return f" User ID: {self.user_id}, INN: {self.inn}"