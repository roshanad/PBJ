number = int(raw_input("Please enter a number "))

count = 1

for number in range(count, number): 
	if number % 3 == 0 and number % 5 == 0:
		print "FizzBuzz"
	elif number % 3 == 0: 
		print "Fizz"
	elif number % 5 == 0:
		print "Buzz"
	else: 
		print number
count = count + 1  
