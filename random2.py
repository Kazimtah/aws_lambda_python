import random 

print(random.uniform(10.5, 11.5))


print(dir(random))

#interger random selection 
print(random.randint(100, 2000))
# shuffle 

my_list = [1,2,3,4,5,6,7]
print(my_list)

print(random.shuffle(my_list))
print(my_list)
print(random.choice(my_list))

print(random.choices(my_list, k=2))
print(random.choices('abcderf', k=14))

print(random.choices('ABCDEFG0874875@!#$%^&*', k= 12))

#creating random password 

print(''.join(random.choices('abcdefeagaABCDEFG0874875@!#$%^&*', k= 18)))
print(''.join(random.sample('abcdefeagaABCDEFG0874875@!#$%^&*', k=12 )))

# sample method
print(random.sample([2,48,8,4,9,1,2,3], k= 4))