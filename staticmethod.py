class Comment:
    def __init__(self,text):
        self.text = text
    @staticmethod
    def merge_commets(first, second):
        return f"{first}, {second}"
my_comment = Comment("First comment")
print(my_comment.text)
print(my_comment.merge_commets("First comment", "Second comment"))

my_second_Comment = Comment("Second comment")
print(my_second_Comment.merge_commets("First comment from the second object instation", "Second comment from the second instatiation of the clas"))

print(dir(Comment))