class User:
    def __init__(self, username, email):
        self. username = username 
        self.email = email

class Post:
    def __init__(self,title, content, author):
        self. title = title
        self.content = content 
        self.author = author


class Forum:
    def __init__(self):
        self.users = []
        self.posts = []
    
    def register_user(self, username, email):
        user = User(username, email)
        self.users.append(user)
        return user 
    
    def create_post(self,title, content, author):
        post = Post(title, content,author)
        self.posts.append(post)
        return post 
    # find the user by the username
    def find_post_username(self, username):
        for username in self.users:
            if self.usersname == username:
                return username

# defining function by emmail
    def find_post_email(self, email):
        for email in self.users:
            if self.users == email:
                return email 

#find the by post
    def find_post(self,author):
        for autheor in self.author:
            if autheor == self.author:
                return autheor

forum = Forum()
first_form = forum.register_user("booba","boba@gmail.com")
second_form = forum.create_post("my title", "love", first_form)
print(forum.users)
print(forum.users[0].username)
print(forum.posts[0].title)
print(first_form.find_post("booba"))