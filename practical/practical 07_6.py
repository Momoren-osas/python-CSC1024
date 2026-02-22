# Initialize an empty list to store the numbers
numbers = []

# Read ten numbers from the user
for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Initialize max and min with the first element of the list
max_num = numbers[0]
min_num = numbers[0]

# Traverse the list to find the maximum and minimum numbers
for number in numbers:
    if number > max_num:
        max_num = number
    if number < min_num:
        min_num = number

# Output the results
print(f'my_list = {numbers}')
print(f"The maximum number is: {max_num}")
print(f"The minimum number is: {min_num}")