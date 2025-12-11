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

forum = Forum()
first_form = forum.register_user("booba","boba@gmail.com")
second_form = forum.create_post("my title", "love", first_form)
print(forum.users)
print(forum.users[0].username)
print(forum.posts[0].title)