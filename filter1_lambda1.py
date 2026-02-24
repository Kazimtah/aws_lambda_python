my_nums = [3,4,10,15,20,21]

filtered_my_nums = filter(lambda num: num%2 ==0, my_nums)
print(list(filtered_my_nums))

filtered_by_odd_nums = filter(lambda num: num%2 != 0, my_nums)
print(list(filtered_by_odd_nums))


map()