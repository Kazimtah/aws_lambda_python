def print_fruits_info(person_name, fruits):
    for fruit in fruits:
        print(f'{person_name} likes {fruit}')


myname = "bogdan"
favorites_fruits = ["orange", "apples", "bananas"]

print_fruits_info(myname, favorites_fruits)