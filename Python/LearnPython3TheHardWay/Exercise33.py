#-------------------------------------------------------------------------------
# Purpose/Question:
#
# Author:      Olivier Laflamme
#
# Created:     03-10-2019
# Copyright:   (c) Boschko 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

i=0
numbers=[]

while (i <6):
    print(f"at the top i is {i}")
    numbers.append(i)
    i+=1
    print("Numbers now", numbers)
    print(f"at the bottom i is {i}")
print("the numbers: ")
for num in numbers:
    print(num)