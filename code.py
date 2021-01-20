
def are_valid_groups(students, groups):
<<<<<<< HEAD
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
=======

    result = False

    for i in range(len(students)):  # Goes through list of students
        for j in groups:  # Goes through list of groups
            for k in j:  # Goes through nested list of students in groups
                # Checks if a student is an element inside the nested list of students
                if k == students[i]:
                    result = True
                    break  # exits current loop in the case that it is, so it moves on to the next student

            if result == True:
                break

        if result == True and i != len(students)-1:
            result = False
        else:
            break
>>>>>>> 673b18957e87bdc7d1d17a91ef7d92a3ac486af1


print(are_valid_groups([1, 2, 3], [[1, 2, 3], [4, 5, 6, 7, 8]]))
