import csv

with open('test.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['user_id','user_name',' comments_qtn'])
    writer.writerow([5434, 'bodan', 1300])
    writer.writerow([4499, 'alice', 830])
    writer.writerow([7247, 'bob', 970])

with open('test.csv','r') as csv_file:
    _csv_reader = csv.reader(csv_file)
    #for line in _csv_reader:
     #   print(line)
    for index ,element in enumerate(_csv_reader):
        print(index,element)
        if index == 0:
            header = element
        else:
           for index,value in enumerate(element):

    