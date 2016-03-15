# First Goal: Create a program that can tell you whether or not you can make a peanut butter and jelly sandwich
bread = raw_input("How much bread do you have? ")
bread = int(bread)

peanut_butter = raw_input ("How much peanut butter do you have? ")
peanut_butter = int(peanut_butter)

jelly = raw_input ("How much jelly do you have? ")
jelly = int(jelly)

if bread >= 2 and peanut_butter >= 1 and jelly >= 1:
	print "I can make a peanut butter and jelly sandwich"
else:
	print "Looks like I don't have a lunch today"