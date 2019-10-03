#-------------------------------------------------------------------------------
# Purpose:Reading Files
#
# Author:      Olivier Laflamme
#
# Created:     02-10-2019
# Copyright:   (c) Boschko 2019
# Licence:     MIT
#-------------------------------------------------------------------------------
from sys import argv
script, filename=argv

txt=open(filename)

print (f"here is your file {filename}:")
print(txt.read())

print("type the filename again:")
file_again=input("> ")

txt_again=open(file_again)
print(txt_again.read())


#====================================
## here is your file ex15_sample.txt:
## This is stuff i typed into this file.
## This is really easy stuff but is a good
## refresher. lots and lots of fun
##
## type the filename again:
##> ex15_sample.txt
## This is stuff i typed into this file.
## This is really easy stuff but is a good
## refresher. lots and lots of fun