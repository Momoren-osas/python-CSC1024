mass = float(input("Input object mass in KG : "))
velocity = float(input("Input the velocity of the object in (m/s) : "))

momentum = mass * velocity
kineticEnergy = 1/2 * mass * velocity ** 2

print("The momentum is :", round(momentum,2) , "kg m s^-1 \nThe Kinetic Energy is :", round(kineticEnergy,2), "j")