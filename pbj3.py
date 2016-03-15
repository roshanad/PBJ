# Third Goal: Create a program to allow you to make open-face sandwiches if you have an odd number of slices of bread ( )
bread = int(raw_input("How much bread do you have? "))

peanut_butter = int(raw_input ("How much peanut butter do you have? "))

jelly = int(raw_input("How much jelly do you have? "))

bread_to_make_sandwich = bread / 2 


print "So, you've %r bread, %r peanut_butter, and %r jelly. " % (bread, peanut_butter, jelly)

if bread % 2 == 0: 
	print "You have enough bread to make sandwich"

elif bread < 2 and peanut_butter < 1 and jelly < 1:
	print "You do not have enough ingredients to make sandwich" 

else:
	print "I can make one open-face sanwich for you" 