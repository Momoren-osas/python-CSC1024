

multi = int(input("Which multiplaction table would you like to print? "))
length = int(input("How high would you like it to go? "))

for i in range(1, length + 1):
    result = multi * i
    print(f"{multi} times {i} = {result}")