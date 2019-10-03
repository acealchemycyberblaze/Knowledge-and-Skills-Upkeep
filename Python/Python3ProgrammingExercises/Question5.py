#-------------------------------------------------------------------------------
# Purpose/Question:
#
##Define a class which has at least two methods:
##
##getString: to get a string from console input
##printString: to print the string in upper case.
##Also please include simple test function to test the class methods.
# Author:      Olivier Laflamme
#
# Created:     03-10-2019
# Copyright:   (c) Boschko 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

class IOstring():
    def __init__(self):
        pass

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())

xx = IOstring()
xx.getString()
xx.printString()