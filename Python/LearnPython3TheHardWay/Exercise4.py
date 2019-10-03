#-------------------------------------------------------------------------------
# Purpose: variables and names
#
# Author:      Olivier Laflamme
#
# Created:     02-10-2019
# Copyright:   (c) Boschko 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

cars=100
spaceInCar=4.0
drivers=30
passengers=90
carsNotDriven=cars-drivers
carsDriven=drivers
carpoolCap = carsDriven*spaceInCar
averagePassengerPerCar= passengers/carsDriven

print ("there are", cars, "cars avail")
print("There are only", drivers, "drivers available.")
print("There will be", carsNotDriven, "empty cars today.")
print("We can transport", carpoolCap, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", averagePassengerPerCar,"in each car.")

