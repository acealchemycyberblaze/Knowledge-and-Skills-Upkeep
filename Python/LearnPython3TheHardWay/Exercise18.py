#-------------------------------------------------------------------------------
# Purpose:names, variables, code, functions
#
# Author:      Olivier Laflamme
#
# Created:     02-10-2019
# Copyright:   (c) Boschko 2019
# Licence:     MIT
#-------------------------------------------------------------------------------
## Functions do three things:
## 1. They name pieces of code the way variables name strings and numbers.
## 2. They take arguments the way your scripts take argv.
## 3. Using 1 and 2, they let you make your own ”mini-scripts” or ”tiny commands.”


#this is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#*args is pointless we can just do this
def print_two_again(arg1,arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#this prints nothing
def print_none():
    print("i got nothing")

print_two("olivier", "laflamme")
print_two_again("Olivier","Laflamme")
print_one("ONE!")
print_none()