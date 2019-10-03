#-------------------------------------------------------------------------------
# Purpose/Question: find in a two dimensional array
#
'''each row is sorted in ascending order from left to right, and each column is sorted in ascending order from top to bottom.
Please complete a function, enter such a two-dimensional array and an integer to determine whether the array contains the integer.
'''
# Author:      Olivier Laflamme
#
# Created:     03-10-2019
# Copyright:   (c) Boschko 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

class  Solution :
    # array 2D list
    def  Find ( self , target , array ):
        # write code here
        if  not array:
            Return
        row =  len (array)
        col =  len (array[ 0 ])

        for i in  range (row):
            for j in  range (col):
                if target == array[i][j]:
                    return  True
        return  False