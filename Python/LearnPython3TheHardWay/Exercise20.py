#-------------------------------------------------------------------------------
# Purpose: functions and files
#
# Author:      Olivier Laflamme
#
# Created:     02-10-2019
# Copyright:   (c) Boschko 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

from sys import argv
script, input_file = argv #setup argv to accept the script and file as input

def print_all(f): #creats a function which reads and prints the input
    print(f.read())

def rewind(f): # create a function that sets input files to current position
    f.seek(0) #to 0 via seek

def print_a_line(line_count, f): #create funct that accepts int denoting the line to read and then
    print(line_count, f.readline()) #reads that line with f.readline
current_file = open(input_file)

# NOTE - readline() reads a single line up to the \n character but leaves the
# \n character at the end of the line, so this automatically advances the file
# position by 1 line for every time the function is called and leaves a blank
# newline in place. That why there's a line break in the output code.
# That's how this script is reading, printing and advancing each line in turn.

print("first lets print the whole file:\n")
print_all(current_file)
print("now lets rewind. kind of like a tape")
rewind(current_file)
print("lets print three lines")

current_line =1 # Sets variable 'current_line' to 1
print_a_line(current_line, current_file)

current_line=current_line+1 #Calls function 'print_a_line()' with 'current_line' and 'current_file' as param
print_a_line(current_line, current_file)

current_line = current_line +1
print_a_line(current_line, current_file)

#==========================
##    python Exercise20.py ex0_test.txt
##    first lets print the whole file:
##
##    This is line 1
##    This is line 2
##    This is line 3
##
##    now lets rewind. kind of like a tape
##    lets print three lines
##    1 This is line 1
##
##    2 This is line 2
##
##    3 This is line 3