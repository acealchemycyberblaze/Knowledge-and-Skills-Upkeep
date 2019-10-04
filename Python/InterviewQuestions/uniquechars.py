#-------------------------------------------------------------------------------
# Purpose/Question:
#
# '''Define a that takes a string as input and returns the first non-repeated (unique) character
# in the input string. If there are no unique characters return None. '''
# Author:      Olivier Laflamme
#
# Created:     03-10-2019
# Copyright:   (c) Boschko 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

def unique_char(string):
    count = {}
    for i in string:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    for j in count:
        if count[j] == 1:
            return j

print(unique_char('aabcg'))
