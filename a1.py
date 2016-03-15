def product(values):
	result = 1
	for v in values:
		result = result * v
	return result

def shortest(words):
	result = words[0]
	for w in words:
		if len(w) < len(result):
			result = w
		return result

def average(numbers):
	sum = 0;
	i = 0;
	for n in numbers:
		sum = sum + n
	return sum/len(numbers)

import random
def dice():
	i = 0
	sums = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
	for k in range (2,13):
		sums[k] = 0

	while i < 10000:

		die1 = random.randint(1,6)
		die2 = random.randint(1,6)
		sums[die1 + die2] += 1
		i+=1
		
	print (sums)

def game():
	print ("Think of a number between 1 and 1000.")
	min = 1
	max = 1000
	while (min < max):
		guess = (min + max) // 2
		answer = input("Is it more than {} (y/n)? ".format(guess))
		if answer == "y":
			min = guess + 1
		elif answer.lower == "y":
			min = guess + 1
		elif answer.startswith('ye',0,2):
			min = guess + 1
		elif answer.startswith('YE', 0, 2):
			min = guess + 1
		else:
			max = guess
	# At this point min and max must be the same




game()