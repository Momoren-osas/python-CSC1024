option = int(input("Choose an option (1-12): "))

for i in range(1, 13, 1):
    result = option * i
    print(f"{option} x {i} = {result}")
