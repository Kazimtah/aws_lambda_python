class Post:
    def __init__(self,title):
        self.title = title
        self.any = any 
    
    def __add__(self, other):

        return f"{self.title} {other.title}"

    def __eq__(self, other):
        return self.title == other.title
    
first_comment = Post("First comment")
secon_comment = Post("Second comment")
first_comment_like_first = Post("First comment")
print(first_comment + secon_comment)
print(first_comment == secon_comment)
print(first_comment == first_comment_like_first)