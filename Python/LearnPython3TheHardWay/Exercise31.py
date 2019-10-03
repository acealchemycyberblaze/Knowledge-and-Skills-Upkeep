#-------------------------------------------------------------------------------
# Purpose/Question:making decision
#
# Author:      Olivier Laflamme
#
# Created:     03-10-2019
# Copyright:   (c) Boschko 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

print(""" you enter a dark room with two doors
Do you go through door #1 or door #2?""")

door = input("> ")

if door=='1':
    print("theres a giant bear here eating all the honey")
    print("what do you do")
    print("1. take the honey")
    print("2. scream at the bear")

    bear=input("> ")
    if bear =="1":
        print("the bear eats off your face, Good job!")
    elif bear=="2":
        print("the bear eats your leg off. Good job!")
    else:
        print(f"well, doing {bear} is probably better")
        print("bear runs away")

elif door =="2":
    print("you stare into the endless abyss at cthulhu's retina")
    print("1. blueberries")
    print("2. yello jacker clothspins")
    print("3. understaning revolvers yelling melodies")
    insanity=input("> ")
    if insanity=="1" or insanity=="2":
        print("your body survives powered by a mind of jello")
        print("good job")
    else:
        print("the insanity rots your eyes into a pool of muck")
        print("good job")
else:
    print("you stumbled arround and fall on a knife and die, Good Job!")

#====================================
##    python Exercise.31.py
##    you enter a dark room with two doors
##    Do you go through door #1 or door #2?
##    > 1
##    theres a giant bear here eating all the honey
##    what do you do
##    1. take the honey
##    2. scream at the bear
##    > 2
##    the bear eats your leg off. Good job!