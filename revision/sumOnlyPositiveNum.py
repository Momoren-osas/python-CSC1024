sum = 0
for i in range(10):
    num = int(input("Enter a number: "))
    if num > 0:
        sum += num

print(f'Sum of positive numbers = {sum}')