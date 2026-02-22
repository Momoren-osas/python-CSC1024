import random

secret_number = 50
guess_num = random.randint(1, 200)
count = 1
playing = 'yes'
while playing:
    while guess_num != secret_number:
        if guess_num < secret_number:
            print(f"Guess {count}: {guess_num} is too low.")
        else:
            print(f"Guess {count}: {guess_num} is too high.")
        guess_num = random.randint(1, 200)
        count += 1
    print(f"Guess {count}: {guess_num} is correct! The secret number is {secret_number}.")
    playing = input("Do you want to play again? (yes/no): ").strip().lower() == 'yes'
