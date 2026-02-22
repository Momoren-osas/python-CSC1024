first10gbRateperGB = 15.0
nextgbRate = 30.0

montlyDataUsage = float(input("Enter your montly data usage in GB : "))
if montlyDataUsage <= 10 :
    totalCharges = montlyDataUsage * first10gbRateperGB
else :
    totalCharges = (10 * first10gbRateperGB) + ((montlyDataUsage - 10) * nextgbRate)
    
print("Your total amount comes up to : Rm", f'{totalCharges:.2f}')