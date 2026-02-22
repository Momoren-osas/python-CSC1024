chooseRectangleOrCircle = input("Choose rectangle or circle (r/c) : ").lower()
if chooseRectangleOrCircle == 'r' :
    length = float(input("Enter the length of the rectangle in cm: "))
    width = float(input("Enter the width of the rectangle in cm: "))
    area = length * width
    print("The area of the rectangle is : ", f'{area:.2f}'," cm^2")
elif chooseRectangleOrCircle == 'c' :
    radius = float(input("Enter the radius of the circle in cm: "))
    area = 3.14 * radius * radius
    print("The area of the circle is : ", f'{area:.2f}', " cm^2")
else :
    print("Invalid input!")