def are_valid_groups(numbers, groups):
	for num in numbers:
		for group in groups:
			for sub in group:
				if num == sub:
					final = True
					break
				else:
					final = False
	return final

					 
 		
