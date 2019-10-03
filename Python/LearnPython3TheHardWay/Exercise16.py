#-------------------------------------------------------------------------------
# Purpose:reading and writing files
#
# Author:      Olivier Laflamme
#
# Created:     02-10-2019
# Copyright:   (c) Boschko 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

## • close – Closes the file. Like File->Save.. in your editor.
## • read – Reads the contents of the file. You can assign the result to a variable.
## • readline – Reads just one line of a text file.
## • truncate – Empties the file. Watch out if you care about the file.
## • write('stuff') – Writes ”stuff” to the file.
## • seek(0) – Move the read/write location to the beginning of the file.

from sys import argv
script, filename = argv

print(f"we're going to erase {filename}")
print("if you dont want that, hit CTRL-C (^C)")
print("if you do want that, hit RETURN")

input("?")
print("Opening the file...")
target=open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now i'm going to ask you for three lines")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("i'm going to write these to the files")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("and finally, we close it")
target.close()

#==================
## we're going to erase ex16_test.txt
## if you dont want that, hit CTRL-C (^C)
## if you do want that, hit RETURN
## ?
## Opening the file...
## Truncating the file. Goodbye!
## Now i'm going to ask you for three lines
## line 1: this is line one being rewritten
## line 2: line 2
## line 3: and this is line 3
## i'm going to write these to the files
## and finally, we close it