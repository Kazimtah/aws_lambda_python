def greeting(greet):
    return lambda name: f"{greet}, {name}"

morning_greetig = greeting("Good morning")

print(morning_greetig('bogdan'))

square = lambda x: x*x
print(square(6))

numbers = [1,2,3,4,5]
squared = list(map(lambda x: x*x, numbers))
print(squared)

names = ["ali","ahmad","sara"]
uppercased_name = map(str.upper, names)
print(list(uppercased_name))

# using lambda with built-in function
numbers2 = [1,2,3,4,5]
even_number = list(filter(lambda x: x%2 ==0, numbers2))
print(even_number)

# lambdaa function with built-in function of sorted

words = ["apple", "banana", "cherry", "blueberry"]
sorted_word = list(sorted(words, key=lambda word: len(word)))
print(sorted_word)

def apply_operation(func,value):
    return func(value)

result = apply_operation(lambda x: x*3,5)
print(result)
