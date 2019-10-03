#-------------------------------------------------------------------------------
# Purpose:what if
#
# Author:      Olivier Laflamme
#
# Created:     03-10-2019
# Copyright:   (c) Boschko 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

people =20
cats =30
dogs=15

if people < cats:
    print("too many cats! the words is doomed")
if people > cats:
    print("not many cats! the world is saved")

if people < dogs:
    print("the world is drooled on!")
if people > dogs:
    print("the world is dry")

dogs+=5

if people>=dogs:
    print("people are greater than the or equal to dogs")
if people<=dogs:
    print("people are less than equal to dogs")
if people==dogs:
    print("people are dogs")