import math

print(math.e)
print(math.pi)


print(math.sqrt(225))

print(math.factorial(10))

print(math.log(100))

print(math.log2(8))

print(math.floor(10.7))
print("************************")
def calc_factorial(num: int):
    if type(num) is not int:
        raise TypeError("Number must be integer")
    if num<=0:
        raise ValueError("Number should be Postitive")
    if num == 1 :
        return 1
    else:
        result = math.factorial(num)
    return result 

first_factorial = calc_factorial(10)
print(first_factorial)
second_factorial = calc_factorial(3)
print(second_factorial)
third_factorial = calc_factorial(-3)
print(third_factorial)

print("*****second function******")

def calc2_factorial(num: int):
    if type(num) is not int:
        raise TypeError("Number must be integer")
    if num<=0:
        raise ValueError("Number should be Postitive")
    if num == 1 :
        return 1
    return calc2_factorial(num -1) * num 

factorial1 = calc2_factorial(10)

print(factorial1)

factorial2 = calc2_factorial(6)
print(factorial2)

factorial3 = calc2_factorial(-3)

print(factorial3)