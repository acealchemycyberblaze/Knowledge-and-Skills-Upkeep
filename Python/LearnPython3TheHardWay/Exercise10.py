#-------------------------------------------------------------------------------
# Purpose:what was that?
#
# Author:      Olivier Laflamme
#
# Created:     02-10-2019
# Copyright:   (c) Boschko 2019
# Licence:     MIT
#-------------------------------------------------------------------------------
tabby_cat = "\tI'm tabbed in"
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat"
fat_cat = """
I'll  do a list
\t* Cat Food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

## \\       Backslash (\)
## \'       Single-quote (’)
## \"       Double-quote (”)
## \a       ASCII bell (BEL)
## \b       ASCII backspace (BS)
## \f       ASCII formfeed (FF)
## \n       ASCII linefeed (LF)
## \N{name} Character named name in the Unicode database (Unicode only)
## \r       Carriage Return (CR)
## \t       Horizontal Tab (TAB)
## \uxxxx   Character with 16-bit hex value xxxx
## \Uxxxxxxxx Character with 32-bit hex value xxxxxxxx
## \v       ASCII vertical tab (VT)
## \000     Character with octal value 000
## \xhh     Character with hex value hh