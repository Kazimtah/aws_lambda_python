class User:
    def info(self, username, email):
        print(f"User: {username} has email {email}")

first_user = User()
first_user.username = 'bodan'
first_user.email = 'bodayan@gmail.com'
first_user.info('Bogdan12', 'bodayn@gmail.com')
print(first_user.__dict__)


class Comment:
    def __init__(self,text):
        self.text = text
        self.votes_qty = 0

    def upvote(self):
        self.votes_qty += 1

first_comment = Comment("Firs comment")
 
print(first_comment)