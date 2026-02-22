count = 1
my_list = []

while count <= 5:
    num = float(input("Enter a number: "))
    my_list.append(num)
    count += 1

#Question 1
my_list.sort()
print(f'my_list = {my_list}')

#Question 2
'''
sum_of_numbers = sum(my_list)
print(f'Sum = {sum_of_numbers}')
average = sum_of_numbers / len(my_list)
print(f'Average = {average}')
'''

#Question 3
'''
print(f'Foward_list = {my_list}')
my_list.sort(reverse=True)
print(f'Reverse_list = {my_list}')
'''

#Question 4
while len(my_list) > 0:
    del(my_list[-1])
    print(f'my_list = {my_list}')
    