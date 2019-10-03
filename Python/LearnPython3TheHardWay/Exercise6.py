#-------------------------------------------------------------------------------
# Purpose: Strings and Text
#
# Author:      Olivier Laflamme
#
# Created:     02-10-2019
# Copyright:   (c) Boschko 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

types_of_people = 10
x = f"there are {types_of_people} types of people"
print(x)

binary = "binary"
do_not = "don't"
y = f"Thoes who know {binary} and thoes who {do_not}"
print(y)

print (f"I said: {x}")
print(f"I also said: '{y}' ")

hilarious = True
joke_evaluation = "isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

w = "this is the left side of..."
e = "a string with a right side"
print (w+e)