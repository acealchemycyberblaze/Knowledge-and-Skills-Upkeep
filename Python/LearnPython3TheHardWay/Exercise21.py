#-------------------------------------------------------------------------------
# Purpose:functions can return something
#
# Author:      Olivier Laflamme
#
# Created:     02-10-2019
# Copyright:   (c) Boschko 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

def add(a,b):
    print(f"adding {a}+{b}")
    return a+b
def subtract(a,b):
    print(f"substracting {a}-{b}")
    return a-b
def multiply(a,b):
    print(f"multiply {a}*{b}")
    return a*b
def divide(a,b):
    print(f"deviding {a}/{b}")
    return a/b

print("lets do some math with just functions")

age=add(30,5)
height=subtract(78,4)
weight=multiply(90,2)
iq=divide(400,2)
print(f"age: {age}, height: {height}, weight: {weight}, IQ: {iq}")
#the puzzle is below
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("easy mental math for me here was the answer ", what, "EZ")