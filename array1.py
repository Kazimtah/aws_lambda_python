
from array import array


my_int_array = array("i", [10,4,3,9,7,15])
print(my_int_array)
print(type(my_int_array))
print(dir(my_int_array))

print(my_int_array[2])

my_int_array.append(20)
print(my_int_array)
my_int_array.append(10.5)
print(my_int_array)
my_int_array.append(True)
print(my_int_array)