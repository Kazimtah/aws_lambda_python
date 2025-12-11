class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email 

class Admin(User):
    def __init__(self, username, email, role):
        super().__init__(username, email)
        self.role = role
        self.is_admin = True 

my_admin  = Admin("bobo33","bobo33@gmail.com","Adminstrator")
print(my_admin.role, my_admin.username, my_admin.is_admin,my_admin.email)
