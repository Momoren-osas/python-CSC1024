speedOfLightMetersPerSecond = 3 * 10 ** 8
oneYearinSeconds = 365.25 * 24 * 60 * 60
oneLightYearDistance = speedOfLightMetersPerSecond * oneYearinSeconds

rateKMtoM = 1000
print("One light year travels", f'{oneLightYearDistance:.2e}', "meters or", "{:e}".format(oneLightYearDistance / rateKMtoM) ,"kilometers")