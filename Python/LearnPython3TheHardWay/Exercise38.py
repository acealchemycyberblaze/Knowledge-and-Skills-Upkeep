#-------------------------------------------------------------------------------
# Purpose: doing things to list
#
# Author:      Olivier (Boschko) Laflamme
# Created:     03/12/2019
# Copyright:   (c) Olivier (Boschko) Laflamme 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
ten_strings = "Apples Oranges Crows Telephone Light Sugar"

print("wait there are not 10 things in that list. Lets fix that.")

stuff = ten_strings.split(' ')
more_stuff= ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    print(f"There are {len(stuff)} items now")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # fancy
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))