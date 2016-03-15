# Second Goal: Create a program to tell you: if you can make a sandwich, how many you can make

# To satisfy the second goal:
#		Continue from the first goal, and add:
#		If you have enough bread (at least 2 slices), peanut butter (at least 1), and jelly (at least 1), print a message like "I can make this many sandwiches: " and then calculate the result.
#		If you don't; you can print the same message as before
#   To calculate which ingredient you have the least of, the min() function will be useful.
#   min() will calculate the smallest number of all of the numbers in the parentheses and tell you which it is
#   For example, min(4, 83, 6) will return 4

bread = int(raw_input("How much bread do you have? "))

peanut_butter = int(raw_input ("How much peanut butter do you have? "))

jelly = int(raw_input("How much jelly do you have? "))

bread_to_make_sandwich = bread / 2 


print "So, you've %r bread, %r peanut_butter, and %r jelly. " % (bread, peanut_butter, jelly)

if bread >= 2 and peanut_butter >= 1 and jelly >= 1:
	print "You can make %r PBJ Sandwich for you" % (bread_to_make_sandwich)

else:
	print "You have %r bread, %r peanut_butter, %r jelly, we do not have enough ingredients to make pbj sandwich" % (bread, peanut_butter, jelly)