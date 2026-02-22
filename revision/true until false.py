state = True
count = 0
while state:
    proceed = input("Do you want to continue? (y/n): ").lower()
    if proceed == 'n':
        state = False
    elif proceed == 'y':
        count += 1
        print(f"Iteration count: {count}")
    else:
        print("Invalid input, please enter 'y' or 'n'.")# This code continues to prompt the user until they enter 'n', counting the iterations.
