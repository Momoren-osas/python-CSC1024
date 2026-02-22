count = 1
my_list = []

while count <= 5:
    data = input("Enter a data: ")
    my_list.append(data)
    count += 1

print(f'my_list = {my_list}')

while len(my_list) > 0:
    del(my_list[-1])
    print(f'my_list = {my_list}')