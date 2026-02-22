print("Temperature COnversion Programme. \n[1] Convert Celsius to Fahrenheit. \n[2] Convert Fahrenheit to Celsius.")
choice = int(input("Enter your selection, 1 or 2: "))

run = True

while run:
    if choice == 1:
        print("Celsius (C) to Fahrenheit (F) conversion conversion.")
        minCelsius = int(input("Enter temperature in integr values only.\nEnter minimum temperature: "))
        maxCelsius = int(input("Enter maximum temperature: "))
        if minCelsius >= maxCelsius:
            print("Minimum temperature must be less than maximum temperature.")
        else:
            for celsius in range(minCelsius, maxCelsius + 1):
                fahrenheit = (celsius * 9/5) + 32
                print(f"{celsius}C = {fahrenheit}F")
            print("Conversion Done!")
    elif choice == 2:
        print("Fahrenheit (F) to Celsius (C) conversion conversion.")
        minFahrenheit = int(input("Enter temperature in integr values only.\nEnter minimum temperature: "))
        maxFahrenheit = int(input("Enter maximum temperature: "))
        if minFahrenheit >= maxFahrenheit:
            print("Minimum temperature must be less than maximum temperature.")
        else:
            for fahrenheit in range(minFahrenheit, maxFahrenheit + 1):
                celsius = (fahrenheit - 32) * 5/9
                print(f"{fahrenheit}F = {celsius}C")
    else:
        print("Invalid choice. Please select 1 or 2.")

    again = input("Do you want to run the program again? (y/n): ").strip().lower()
    if again != 'y':
        run = False
    else:
        choice = int(input("Enter your selection, 1 or 2: "))