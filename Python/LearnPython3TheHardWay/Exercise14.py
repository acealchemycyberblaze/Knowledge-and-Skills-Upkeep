#-------------------------------------------------------------------------------
# Purpose:prompting and passing
#
# Author:      Olivier Laflamme
#
# Created:     02-10-2019
# Copyright:   (c) Boschko 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, Im the {script} script")
print("i'd like to ask you a few qyestions")
print(f"do you like me {user_name}?")
likes=input(prompt)

print(f"where do you live {user_name}?")
lives=input(prompt)

print("what kind of computer do you have?")
computer=input(prompt)

print (f"""
So you said {likes} about liking me.
you live in {lives}. not sure where that is
and you have a {computer} computer, nice.
""")

#=============================================#
## Hi Olivier, Im the Exercise14.py script
## i;d like to ask you a few qyestions
## do you like me Olivier?
## >Yes
## where do you live Olivier?
## >Ontario
## what kind of computer do you have?
## >Lenovo
##
## So you said Yes about liking me.
## you live in Ontario. not sure where that is
## and you have a Lenovo computer, nice.