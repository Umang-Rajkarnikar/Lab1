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
