#-------------------------------------------------------------------------------
# Purpose: more variables and printing
#
# Author:      Olivier Laflamme
#
# Created:     02-10-2019
# Copyright:   (c) Boschko 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

my_name = 'olivier laflamme'
my_age = 20
my_height = 6
my_weight = 183
my_eyes = 'brown'
my_teeth = 'white'
my_hair = 'short brown'

#study drill turn ft into inches
my_height_inches = my_height * 12
print(f"my height in ft is {my_height} \nbut in inches it is {my_height_inches}\n")

#study drill turn lbs into kg's
my_weight_kg = (round(my_weight * 0.454,2))
print (f"my weight lbs is {my_weight} \nbut in Kg it's {my_weight_kg}\n")

print (f"let's takl about {my_name}")
print (f"my height is {my_height} ft tall")
print(f"my bodyweight is {my_weight} lbs")
print(f"i have {my_eyes} eyes and {my_hair} hair")
print(f"my teeth are {my_teeth}")

total = my_age + my_height + my_weight
print(f"if i add {my_age} {my_height} {my_weight} and I get {total}")