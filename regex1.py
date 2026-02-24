import re

my_string = "MY name is Bogdan"

res = re.search('Bogdan', my_string)
print(res)
print(type(res))