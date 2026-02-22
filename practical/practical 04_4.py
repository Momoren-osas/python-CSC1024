# practical 04_4.py
# Sum numbers until the user types 'DONE'


total = 0.0
while True:
    s = input("Enter a number (or 'DONE' to finish): ").strip()
    if s.upper() == 'DONE':
        break
    try:
        num = float(s)
    except ValueError:
        print("Invalid input. Please enter a number or 'DONE'.")
        continue
    total += num

print (f"The total sum is: {total}")
