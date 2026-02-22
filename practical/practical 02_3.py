totalIncome = float(input("Enter total anually income in Rm : "))
if totalIncome >= 50001 :
    tax = totalIncome * 0.25
elif totalIncome >= 10001 :
    tax = totalIncome * 0.15
elif totalIncome >= 2501 :
    tax = totalIncome * 0.05
else :
    tax = 0

print("The tax you need to pay is : Rm", f'{tax:.2f}')