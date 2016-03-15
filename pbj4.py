
#To satisfy the fourth goal:
#		Continue from the third goal, but this time if you have enough bread and peanut butter but no jelly, print a message that tells you that you can make a peanut butter sandwich
#		Or if you have more peanut butter and bread than jelly, that you can make a certain number of peanut butter & jelly sandwiches and a certain number of peanut butter sandwiches


bread = int(raw_input("How much bread do you have? "))

peanut_butter = int(raw_input ("How much peanut butter do you have? "))

jelly = int(raw_input("How much jelly do you have? "))

bread_to_make_sandwich = bread / 2 


print "So, you've %r bread, %r peanut_butter, and %r jelly. " % (bread, peanut_butter, jelly)

if bread == 0 and peanut_butter >= 1 and jelly >= 1: 
	print "Looks like you are missing bread"

if bread >= 1 and peanut_butter == 0 and jelly >= 1: 
	print "Looks like you are missing peanut butter"

if bread >= 1 and peanut_butter >= 1 and jelly == 0:
	print "Looks like you are missing jelly"