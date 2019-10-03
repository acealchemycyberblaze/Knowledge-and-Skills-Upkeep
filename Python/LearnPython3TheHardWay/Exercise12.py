#-------------------------------------------------------------------------------
# Purpose:prompting people
#
# Author:      Olivier Laflamme
#
# Created:     02-10-2019
# Copyright:   (c) Boschko 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

age=input("how old are you ")
height=input("how tall are you ")
weight=input("how much do you weigh ")

testing=print("this shouldnt store the value",input())

print(f"so, you are {age} old {height} tall and {weight} heavy")
print(f"{testing}") # testing to see if value stored