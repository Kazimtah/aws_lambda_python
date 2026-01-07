
class User:
    user_qty = 0
 
    def __init__(self, username, email):
       # global user_qty
        self.username = username
        self.email = email 
        User.user_qty +=1

first_user = User("boob", "boob@gmail.com")
second_user = User("Second_user", "second_user@gmail.com")
third_use = User("third_suer", "third_user@gmail.com")
print(User.user_qty)
print(second_user.__dict__)
