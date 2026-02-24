def print_fruits_info(person_name, fruits):
    """
    Docstring for print_fruits_info
    
    :param person_name: is a (string) data type, name of a person
    :param fruits: it should be a list of string which include favorite fruits of the person
    """
    fruits_copy = fruits.copy()
    person_name = 'Alice'
    print(id(person_name))
    fruits.pop()
    for fruit in fruits:
        print(f"{person_name} likes {fruits}")

my_name = "bogdan"
my_favorite_fruits = ['orange','apple','banana']

print_fruits_info(my_name,my_favorite_fruits)
print(id(my_name))
print(my_name)