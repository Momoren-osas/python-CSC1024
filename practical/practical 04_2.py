# /d:/BSDACSC/pratical/practical 04_2.py
print("Starting")
n = -20
first = True
while n <= -2:
    if not first:
        print(" ", end="")
    print(n, end="")
    first = False
    n += 2
print()  # newline after the numbers
print("Done")