#-------------------------------------------------------------------------------
# Purpose:more files
#
# Author:      Olivier Laflamme
#
# Created:     02-10-2019
# Copyright:   (c) Boschko 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"copying from {from_file} to {to_file}")

in_file=open(from_file)
indata=in_file.read()
# do that on one line ==> indata=open(from_file).read()

print(f"the input is {len(indata)} bytes long")
print("ready, hit RETURN to continue, CTRL-C to about")
input()

out_file=open(to_file, 'w')
out_file.write(indata)
# do that on one line ==> out_file=open(to_file, 'w').write(indata)

out_file.close()
in_file.close()

#=========================
# copy source to destination
# python Exercise17.py ex0_test.txt ex00_test.txt
# copying from ex0_test.txt to ex00_test.txt
# the input is 59 bytes long
# ready, hit RETURN to continue, CTRL-C to about