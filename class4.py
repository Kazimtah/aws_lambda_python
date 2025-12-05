class Post:
    def __init__(self,title, content, author):
        self.title = title
        self.content = content 
        self.auth   = author 
        self.likequantity = 0 
    def like(self):
        self.likequantity += 1 
        
my_post = Post("My first post", "some post content", "kazim")
print(my_post)
print(my_post.auth, my_post.content, my_post.title)
my_post.like()
print(my_post.likequantity)
my_post.like()
print(my_post.likequantity)
my_post.like()
print(my_post.likequantity)


