#-------------------------------------------------------------------------------
# Purpose/Question:loops and lists
#
# Author:      Olivier Laflamme
#
# Created:     03-10-2019
# Copyright:   (c) Boschko 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

the_count=[1,2,3,4,5]
fruits=['apples','oranges','pears','apricots']
change=[1,'pennies',2,'dimes',3,'quarters']
# this first kind of for-loop goes through the list

for number in the_count:
    print(f"this is count {number}")
# same as above
for fruit in fruits:
    print(f"a fruit of type {fruit}")

# also we can go through mixed lists too
for i in change:
    print(f"i got {i}")

# we can also build lists, first start with a empty one
elements=[]

# then use the range function to do 0 to 5 counts
for i in range(0,6):
    print(f"adding {i} to the list")
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print(f"element was: {i}")