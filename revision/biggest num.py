num1 = int(input("enter first integer number : "))
num2 = int(input("enter second integer number : "))
num3 = int(input("enter third integer number : "))


if num1 > num2 and num1 > num3:
    print(f"biggest number is {num1}")
elif num2 > num3 and num2 > num1:
    print(f"biggest number is {num2}")
elif num3 > num1 and num3 > num2:
    print(f"biggest number is {num3}")
else:
    print("there are two more numbers that are the same")


if num1 > num2:
    if num1 > num3:
        print(f"biggest number is {num1}")
    elif num3 > num1:
        print(f"biggest number is {num3}")
    else:
        print(f"biggest number is {num1} and {num3}")
elif num2 > num1:
    if num2 > num3:
        print(f"biggest number is {num2}")
    elif num3 > num2:
        print(f"biggest number is {num3}")
    else:
        print(f"biggest number is {num2} and {num3}")
else:
    if num1 > num3:
        print(f"biggest number is {num1} and {num2}")
    elif num3 > num1:
        print(f"biggest number is {num3}")
    else:
        print(f"all numbers are the same")