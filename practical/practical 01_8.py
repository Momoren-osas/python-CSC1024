hourlyWage = float(input("Enter your hourly wage :"))
totalRegularHours = int(input("Enter the total amount of hours worked in a week :"))
totalOvertimeHours = int(input("Enter the total amount of overtime hours worked in a week :"))

#ScenarioA
totalPay = hourlyWage * (totalOvertimeHours + totalRegularHours)
print("your total pay for scenario A is : Rm", round(totalPay, 2))

#ScenarioB
totalPay = hourlyWage * totalRegularHours + hourlyWage * 1.5 * totalOvertimeHours
print("your total pay for scenario B is : Rm", round(totalPay, 2))