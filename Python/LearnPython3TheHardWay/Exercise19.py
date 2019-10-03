#-------------------------------------------------------------------------------
# Purpose:functions and variables
#
# Author:      Olivier Laflamme
#
# Created:     02-10-2019
# Copyright:   (c) Boschko 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"you have {cheese_count} cheeses!")
    print(f"you have {boxes_of_crackers} boxes of crackers!")
    print("man thats enough for a party")
    print("get a blanket!\n")
print("we can just give the dunciton numbers directly")
cheese_and_crackers(20,30)

print("OR we can use variables from our script")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("we can even do the math inside too:")
cheese_and_crackers(10+20,6+5)

print("and we can combine two variables and math")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)