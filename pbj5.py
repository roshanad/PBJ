
# Fifth Goal: Create a program to tell you: if you have enough bread and peanut butter but no jelly, that you can make a peanut butter sandwich but you should take a hard, honest look at your life.  Wow, your program is kinda judgy.

# To satisfy the fifth goal:
#		Continue from the fourth goal, but this time if you don't have enough ingredients, print a message that tells you which ones you're missing.


bread = int(raw_input("How much bread do you have? "))

peanut_butter = int(raw_input ("How much peanut butter do you have? "))

jelly = int(raw_input("How much jelly do you have? "))

bread_to_make_sandwich = bread / 2 

number_sandwiches = min(bread_to_make_sandwich, peanut_butter, jelly)

number_pbj_sandwiches = min(bread_to_make_sandwich, peanut_butter)

print "So, you've %r bread, %r peanut_butter, and %r jelly. " % (bread, peanut_butter, jelly)

if bread >= number_sandwiches and peanut_butter >= number_sandwiches and jelly == 0: 
	print "It seems like you are missing jelly, we can still make peanut butter sandwich"

elif bread > number_sandwiches and peanut_butter > number_sandwiches:
	print "We can make %r peanut butter only sandwiches and %r peanut butter jelly sandwiches" % (
 		number_pbj_sandwiches, number_sandwiches)


