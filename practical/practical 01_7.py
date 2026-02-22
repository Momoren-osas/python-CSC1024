totalAmount = float(input("Enter total of the bill in RM :"))
totalFriends = int(input("Enter the head count of friends :"))
SERVICECHARGE = 0.10
GST = 0.06

finalAmount = totalAmount  * (1 + SERVICECHARGE) * (1 + GST) / totalFriends

print("Each person has to pay : Rm", round(finalAmount, 2))