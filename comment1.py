class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qtn = 0
    
    def upvote(self):
        self.votes_qtn +=1
    
    def __add__(self, other):
        return(
            f"{self.text}{other.text}",
            self.votes_qtn + other.votes_qtn)
        
first_comment = Comment("First comment")
first_comment.upvote()
second_comment = Comment("Second Comment")
second_comment.upvote()

print(first_comment + second_comment,Comment.upvote())