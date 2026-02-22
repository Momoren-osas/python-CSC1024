sum = 0
num = int(input("Enter number (Press 0 to end) :"))

while num != 0:
    sum += num
    num = int(input("Enter number (Press 0 to end) :"))
print(f'Total = {sum}')