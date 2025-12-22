import json 
my_nums = [10,100,200,400]
my_num_json = json.dumps(my_nums)
print(my_num_json)
print(type(my_num_json))

my_post = {
    'title': "My post",
    'content': "Post content",
    'liks_qnty': 24,
    'author': {
        'username': "zaman1234",
        'email': 'zaan@zaman.com'
    },
    'metadata': (5,7,20)
}
my_json_post = json.dumps(my_post)
print(my_json_post)



def sum (a,b):
    return a + b

my_math = {
    'title': "Math dict",
    'sum': 48
}

my_math_json = json.dumps(my_math, indent=2)
#print(my_math_json)

file  = open('text.txt', 'w')
file.write(my_math_json)


