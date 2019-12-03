#-------------------------------------------------------------------------------
# Purpose: modules, classes and objects
#
# Author:      Olivier (Boschko) Laflamme
# Created:     03/12/2019
# Copyright:   (c) Olivier (Boschko) Laflamme 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#import mystuff
#mystuff.apple()

def apple():
    print("I AM APPLES!")
#this is just a variable
tangerine =  "living reflections of a dreams"

import mystuff
mystuff.apple()
print(mystuff.tangerine)

mystuff['apple']
mystuff.apple()
mystuff.tangerine

class MyStuff(object):

    def __init__(self):
        self.tangerine="and now a thousand years between"
    def apple(self):
        print("I AM CLASSY APPLE")

