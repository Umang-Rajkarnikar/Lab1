<<<<<<< HEAD
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

					 
 		
=======
def are_valid_groups(students, groups):
    for i in students:
        for j in groups:
            for k in j:
                if k == i:
                    yes = True
                    break
                else:
                    yes = False
                    continue
            break

    return yes


print(are_valid_groups([1, 2, 3], [[1, 2], [1, 3]]))
>>>>>>> c0830ba4d7983e6fff7204f1e45b8c8d9890f505
