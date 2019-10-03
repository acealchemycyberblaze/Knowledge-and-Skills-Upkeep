#-------------------------------------------------------------------------------
# Purpose/Question: replace the spaces
#
'''
Topic: Implement a function that replaces spaces in a string with "%20".
For example, when the string is We Are Happy., the replaced string is We%20Are%20Happy.
'''
# Author:      Olivier Laflamme
#
# Created:     03-10-2019
# Copyright:   (c) Boschko 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

class  Solution :
    # s source string
    def  replaceSpace ( self , s ):
        # write code here
        return s.replace( '  ' , ' %20 ' )