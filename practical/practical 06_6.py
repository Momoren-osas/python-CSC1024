count = 1
my_list = []

while count <= 5:
    data = input("Enter a data: ")
    my_list.append(data)
    count += 1

print(f'my_list = {my_list}')

for idx in range(len(my_list) - 1, -1, -1):
    if idx % 2 == 0:
        del my_list[idx]
        print(f'my_list = {my_list}')