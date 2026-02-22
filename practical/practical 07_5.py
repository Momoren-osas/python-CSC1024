import random

score = 0
while True:
    for i in range(5):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(['+', '-', '*'])
        
        if operation == '+':
            correct_answer = num1 + num2
        elif operation == '-':
            correct_answer = num1 - num2
        else:
            correct_answer = num1 * num2
        
        question = f"Question {i + 1}: {num1} {operation} {num2} = "
        user_answer = int(input(question))
        
        if user_answer == correct_answer:
            score += 1
            print("Correct!\n")
        else:
            print(f"Incorrect. The answer is {correct_answer}\n")

    print(f"You got {score} out of 5 correct!")
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        break
    score = 0