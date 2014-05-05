def count_three_fives(min,max):
	tally = 0
	for i in range(min,max + 1):
		if (i % 3 == 0) & (i % 5 == 0):
		#	print i 
		#	print "fifteen"
			tally += 15
		elif (i % 3) == 0:
		#	print i
		#	print "three"
			tally += 3
		elif (i % 5) == 0:
		#	print i
		#	print "five"
			tally += 5
		else: 
		#	print i
		#	print "normal"
			tally += 1
	print tally

count_three_fives(3,117)
