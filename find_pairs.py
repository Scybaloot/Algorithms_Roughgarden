pairs_A = [int(s) for s in open("pairs.txt").read().rstrip().split()]
pairs_B = [-4, -3, -2, 3, 4, 5]
total = 2

pairs_D = {}


for element in pairs_A:
	pairs_D[element] = 0

def count_pairs(pairs, total, pairs_D):

	for element in pairs:
		other_pair = total - element
		if other_pair in pairs_D:
			if other_pair != element: #make sure distinct
				return True

			# if pairs_D[other_pair] == 0 and pairs_D[element] == 0: #check if seen yet
			# 	pairs_D[other_pair] = 1 #mark as seen	
			# 	pairs_D[element] = 1 #mark as seen
			# 	no_pairs += 1 #increment

total_count = 0
for i in range(-10000,10001):
	#print i
	if count_pairs(pairs_A, i, pairs_D) == True:
		total_count += 1
		print total_count
		print "i = " , i