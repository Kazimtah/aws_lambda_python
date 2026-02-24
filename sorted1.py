students = [{'name': "alice", 'score': 20}, {'name': 'Jhon', 'score': 22}, {'name': 'bodgan', 'score': 10}
            ]

def sorted_by_score(x):
    return x['score']

students.sort(key=sorted_by_score)
print(students)