def display_menu():
    print("[1] Create a new file.")
    print("[2] Display the file.")
    print("[3] Add a new item to the file.")
    choice = input("Enter 1, 2, or 3: ")
    return choice

def create_file():
    subject = input("Enter the subject: ")
    with open("Subject.txt", "w") as file:
        file.write(subject)
    print("File created successfully.")

def display_file():
    try:
        with open("Subject.txt", "r") as file:
            contents = file.read()
            print("Contents of Subject.txt:")
            print(contents)
    except FileNotFoundError:
        print("Subject.txt does not exist.")

def add_to_file():
    subject = input("Enter a new subject: ")
    with open("Subject.txt", "a") as file:
        file.write("\n" + subject)
    display_file()

def main():
    while True:
        choice = display_menu()
        if choice == '1':
            create_file()
        elif choice == '2':
            display_file()
        elif choice == '3':
            add_to_file()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()