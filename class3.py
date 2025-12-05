class Comment:
    def __init__(self,text):
        self.text = text
        self.votes_qty = 0

    def upvote(self):
        self.votes_qty +=1

firstcomment = Comment("First Comment from python")
print(firstcomment.text)
print(firstcomment.votes_qty)
firstcomment.upvote()
print(firstcomment.votes_qty)
firstcomment.upvote()
print(firstcomment.votes_qty)
firstcomment.upvote()
print(firstcomment.votes_qty)