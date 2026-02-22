# Using a while loop to print numbers from 1 to 10
count = 1
while count <= 10 :
    print(count)
    count += 1

# Using a for loop to print numbers from 1 to 10
for i in range(1, 11) :
    print(i)

# Using a for loop to iterate over a list of fruits
fruits = ["apple", "banana", "cherry"]
for fruit in fruits :
    print(fruit)

# Using a for loop with break and continue statements
for number in range(1, 11) :
    if number == 5 :
        continue  # Skip the number 5
    if number == 8 :
        break  # Stop the loop when number is 8
    print(number)

# Using nested loops to print a multiplication table
for i in range(1, 6) :
    for j in range(1, 6) :
        print(f"{i} x {j} = {i * j}")
    print()  # Print a newline after each row

# Using a for loop with else clause
for num in range(1, 6) :
    print(num)
else :
    print("Loop completed successfully!")

# Using a while loop with else clause
count = 1
while count <= 5 :
    print(count)
    count += 1
else :
    print("While loop completed successfully!")

# Using range() with different step values
for num in range(0, 21, 5) :  # Step of 5
    print(num)

for num in range(10, 0, -2) :  # Step of -2
    print(num)

# Using enumerate() to get index and value from a list
colors = ["red", "green", "blue"]
for index, color in enumerate(colors) :
    print(f"Index: {index}, Color: {color}")
    