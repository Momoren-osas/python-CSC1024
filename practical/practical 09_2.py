number = int(input("Display multiplication table of? "))
with open("TT2TXT.txt", "w") as file:
    file.write(f"A multiplication table of {number} times 1 to 12.\n")
    for i in range(1, 13):
        result = number * i
        file.write(f"{number} x {i} = {result}\n")
    
with open("TT2TXT.txt", "r") as file:
    contents = file.read()
    print(contents)