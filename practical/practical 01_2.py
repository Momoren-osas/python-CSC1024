myrCurrency = float(input("Please enter the amount of MYR you want to convert into SGD : "))

rateSGDMYR = 3.27

amountSDG = myrCurrency / rateSGDMYR

print("The total amount of money you converted into SDG is : $", round(amountSDG, 2))
print(f'SDG = {amountSDG:.2f}')