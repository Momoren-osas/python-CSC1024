secret_num = 50
count = 0

while True:
    try:
        guess = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue
    count += 1
    if guess < secret_num:
        print("Too low. Try again.")
    elif guess > secret_num:
        print("Too high. Try again.")
    else:
        print(f"Well done, you took {count} attempts")
        break