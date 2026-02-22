a = 0
b = 0

try:
    a = int(input("Enter the first integer (a): "))
    b = int(input("Enter the second integer (b): "))
except ValueError:
    print("Invalid input. Please enter valid integers.")
    exit(1)

power = 1
count = b
if count >= 0:
    while count > 0:
        power = power * a
        count -= 1
    print(f"{a} to the power of {b} is: {power}")
else:
    print("This program does not handle negative exponents.")