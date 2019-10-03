#-------------------------------------------------------------------------------
# Purpose/Question:
#
# Author:      Olivier Laflamme

##    Write a program that accepts sequence of lines as input and prints
##    the lines after making all characters in the sentence capitalized.
##
##    Suppose the following input is supplied to the program:
##
##    Hello world
##    Practice makes perfect
##    Then, the output should be:
##
##    HELLO WORLD
##    PRACTICE MAKES PERFECT

# Created:     03-10-2019
# Copyright:   (c) Boschko 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

lst = []

while True:
    x = input()
    if len(x)==0:
        break;
    lst.append(x)

for line in lst:
    print(line)