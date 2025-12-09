class Post:
    def __init__(self, title, content, author):
        self.title = title 
        self.conent = content 
        self.author = author
        self.likes_qty = 0

    def like(self):
        self.likes_qty +=1 

    @staticmethod
    def formate_post(title, content):
         return (
             f"Post_title: {title}\n"
             f"Post_content: {content}\n"
         )
formated_post = Post.formate_post("Some porst title", "Post_content")
print(formated_post)