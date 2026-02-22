up_down = int(input("[1] Count Up\n[2] Count Down\nChoose an option (1 or 2): "))

if up_down == 1:
    limit = int(input("Enter a number above 1: "))
    for i in range(1, limit + 1):
        print(i)
elif up_down == 2:
    limit = int(input("Enter a number below 20: "))
    for i in range(20, limit - 1, -1):
        print(i)
else:
    print("I don't understand")