#-------------------------------------------------------------------------------
# Purpose/Question:
#    Write a program that accepts a sentence and calculate the number of letters and digits.
#
#    Suppose the following input is supplied to the program:
#
#    hello world! 123
#    Then, the output should be:
#
#    LETTERS 10
#    DIGITS 3
#
# Author:      Olivier Laflamme
#
# Created:     08-10-2019
# Copyright:   (c) Boschko 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

word = input()
letter,digit = 0,0

for i in word:
    letter+=i.isalpha()         # returns True if alphabet
    digit+=i.isnumeric()        # returns True if numeric

print("LETTERS %d\nDIGITS %d"%(letter,digit))