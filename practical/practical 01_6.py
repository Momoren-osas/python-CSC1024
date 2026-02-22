radiusOfSphere = float(input("Enter the radius of a sphere in cm :"))
PI = 3.14
diameterOfSphere = radiusOfSphere * 2
circumferenceOfSphere = 2 * PI * radiusOfSphere
surfaceAreaOfSphere = 4 * PI * radiusOfSphere ** 2
volumeOfSphere = 4/3 * PI * radiusOfSphere ** 3

print("Diameter of sphere :", diameterOfSphere, "cm \nCircumference of sphere :", circumferenceOfSphere, "cm \nSurface Area of sphere :", surfaceAreaOfSphere, "cm^2 \nVolume of Sphere :", volumeOfSphere, "cm^3")