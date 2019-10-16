#-------------------------------------------------------------------------------
# Purpose/Question: Regular Expression fun with re module
#
# Author:      Olivier Laflamme
#
# Created:     15-10-2019
# Copyright:   (c) Boschko 2019
# Licence:     MIT
#-------------------------------------------------------------------------------
import re

content = 'Xiaoshuaib has 100 bananas'
res = re.match( '^Xi.*?(\d+)\s.*s$' , content)
print (res.group( 1 ))


content = 'Xiaoshuaib has 100 bananas'
res = re.match( '^Xi.*(\d+)\s.*s$' , content)
print (res.group( 1 ))

Content = """Xiaoshuaib has 100
bananas"""
res = re.match( '^Xi.*?(\d+)\s.*s$' , content , re.S)
print (res.group( 1 ))

content = """Xiaoshuaib has 100
bananas"""
res = re.search( 'Xi.*?(\d+)\s.*s' , content , re.S)
print (res.group( 1 ) )

Content = """Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;"""
res = re.findall( 'Xi.*?(\d+)\s.*? s;' , content , re.S)
print (res)

content = """Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;"""
content = re.sub( '\d+' , '250' , content)
print (content )

content = "Xiaoshuaib has 100 bananas"
res = re.match( '^Xi.*?(\d+)\s.*s$' , content , re.S)
res = re.match(pattern , content)
print (res. Group( 1 ))
