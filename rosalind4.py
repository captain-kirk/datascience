def problem4(n, k):
	
	kids = 1
	adults = 0
	total = 1

	for x in range(1,n):
		tobecomeadults = kids
		kids = adults * k
		adults = adults + tobecomeadults
		total = kids + adults
		
	print(total)

problem4(5,3)
problem4(32, 2)