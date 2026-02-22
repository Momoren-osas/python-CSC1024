i = 1
count = 1
while i <= 2:
    j = 1
    if i == 1:
        while j <= 4:
            print(str(count) + ' ', end='')
            count += 1
            j += 1
    else:
        while j <= 4:
            print(str(count) + ' ', end='')
            count += 1
            j += 1
    print()  # newline after each row
    i += 1
