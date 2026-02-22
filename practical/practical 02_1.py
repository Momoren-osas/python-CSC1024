new = 3.00
oldies = 2.00

numNew = int(input("enter the total number of new videos rented : "))
numOld = int(input("enter the total number of old videos rented : "))

totalCharges = numNew * new + numOld * oldies
3
print("Your total amount comes up to : ", f'{totalCharges:.2f}')