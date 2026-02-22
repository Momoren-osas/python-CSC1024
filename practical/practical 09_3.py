
while True:
    print("Student Grade Manager")
    print("[1] Add new student grades")
    print("[2] View all grades")
    print("[3] Calculate class average")
    print("[4] Exit")
    
    choice = input("Select an option: ")
    
    if choice == '1':
        name = input("Enter student name: ")
        grade = float(input("Enter student grade (0-100): "))
        if 0 <= grade <= 100:
            with open("grades.txt", "a") as file:
                file.write(f"{name}: {grade}\n")
        else:
            print("Invalid grade. Please enter a value between 0 and 100.")
    
    elif choice == '2':
        try:
            with open("grades.txt", "r") as file:
                grades = file.readlines()
                for line in grades:
                    print(line.strip())
        except FileNotFoundError:
            print("No grades found. Please add grades first.")
    
    elif choice == '3':
        try:
            with open("grades.txt", "r") as file:
                grades = []
                for line in file.readlines():
                    parts = line.split(": ")
                    if len(parts) == 2:
                        try:
                            grades.append(float(parts[1]))
                        except ValueError:
                            pass
                if grades:
                    average = sum(grades) / len(grades)
                    print(f"Class average: {average:.2f}")
                else:
                    print("No grades available to calculate average.")
        except FileNotFoundError:
            print("No grades found. Please add grades first.")
    
    elif choice == '4':
        print("Exiting the program.")
        break
    
    else:
        print("Invalid option. Please select a valid option.")