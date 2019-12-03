#-------------------------------------------------------------------------------
# Purpose: Dictionaries, oh lovely Dicrionaries
#
# Author:      Olivier (Boschko) Laflamme
# Created:     03/12/2019
# Copyright:   (c) Olivier (Boschko) Laflamme 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#create a mapping staate of abreviaotions

provinces = {
    'British Colomvia': 'BC',
    'Ontatio': 'ON',
    'Quebec': 'QC',
    'Alberta': 'AB',
    'Saskatchewan': 'SK',
    'Nova Scotia': 'NS',
    'Prince Edward Island': 'PEI'
}
cities = {
    'QC': 'Shannon',
    'QC': 'Montreal',
    'ON': 'Toronto',
    'AB': 'Manitoba'
}
# add some more cities
cities['QC']='Sherbrook'
cities['ON']='Kingston'

#print out some cities
print("-" *10)
print("The province of ON has: ", cities['ON'])
print("The province of QC has: ", cities['ON'])

#print out some provinces
print("-" *10)
print("Ontarios abreviation is ", provinces['Ontario'])
# do it by using the province then cities dict
print("-" *10)

# fuck this exercise...