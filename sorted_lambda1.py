"""
This is function is used to sorted a list of dictionary using the lambda function 
"""
students = [
{'name': 'Jhon', 'score': 40},
{'name': 'Ahmad', 'score': 50},
{'nmae': 'Abdul', 'score':20}
]

students.sort(key= lambda student: student['score'], reverse=True)
print(students)