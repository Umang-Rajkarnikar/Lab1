
def are_valid_groups(students, groups):
<<<<<<< HEAD
=======
    result = False;

    for i in range(len(students)):      #Goes through list of students
        for j in groups:    #Goes through list of groups
            for k in j:     #Goes through nested list of students in groups
                if k == students[i]:     #Checks if a student is an element inside the nested list of students
                    result = True
                    break       #exits current loop in the case that it is, so it moves on to the next student

            if result == True:
                break

        if result == True and i != len(students)-1:
            result = False
        else:
            break

    return result

print(are_valid_groups(["1","2","3"],[["1","2","3"],["4","5","6","7","8"]]))
























# def are_valid_groups(students, groups):
#     result = false;
#
#     for i in groups:
#         if()
#
#     for i in range(len(students)):      #Goes through list of students
#         for j in groups:    #Goes through list of groups
#             for k in j:     #Goes through nested list of students in groups
#                 if k == students[i]:     #Checks if a student is an element inside the nested list of students
#                     result = true
#                     break       #exits current loop in the case that it is, so it moves on to the next student
#
#             if result == true:
#                 break
#
#         if result == true and i != len(students)-1:
#             result = false
#         else:
#             break
#
#     return result
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


>>>>>>> ea53d82278d7105abd3bfa17de4204beaa6a1961
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


print(are_valid_groups(["1", "2", "3"], [
      ["1", "2", "3"], ["4", "5", "6", "7", "8"]]))
