
def are_valid_groups(students, groups):
<<<<<<< HEAD
    result = False;

    for i in groups:
        if(len(i) == 2 or len(i) == 3)
            result = true
        else:
            result = false
            break;

    if(result):
        result = false
        for i in range(len(students)):      #Goes through list of students
            for j in groups:    #Goes through list of groups
                for k in j:     #Goes through nested list of students in groups
                    if len(j) < 3:
                        if k == students[i]:     #Checks if a student is an element inside the nested list of students
                            result = True
                            break       #exits current loop in the case that it is, so it moves on to the next student
                if result == True:
                    break
=======

    result = False

    for i in range(len(students)):  # Goes through list of students
        for j in groups:  # Goes through list of groups
            for k in j:  # Goes through nested list of students in groups
                if len(j) < 3:
                    # Checks if a student is an element inside the nested list of students
                    if k == students[i]:
                        result = True
                        break  # exits current loop in the case that it is, so it moves on to the next student
            if result == True:
                break

        if result == True:
            result = False
        else:
            
>>>>>>> 9f65dfc80c0812783bc964515edd6df188f01646

            if result == True and i != len(students)-1:
                result = False
            else:
                break
    else:
        result = false
    return result


print(are_valid_groups(["1", "2", "3"], [
      ["1", "2", "3"], ["4", "5", "6", "7", "8"]]))


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

<< << << < HEAD
== == == =

>>>>>> > ea53d82278d7105abd3bfa17de4204beaa6a1961
 result = False

  for i in range(len(students)):  # Goes through list of students
       for j in groups:  # Goes through list of groups
            for k in j:  # Goes through nested list of students in groups
                # Checks if a student is an element inside the nested list of students
                if k == students[i]:

        else:
            break
>>>>>> > 6a1008837d7ea174343ad19cf4e6e98c60613459

 result = False

  for i in range(len(students)):  # Goes through list of students
       for j in groups:  # Goes through list of groups
            for k in j:  # Goes through nested list of students in groups
                # Checks if a student is an element inside the nested list of students
                if k == students[i]:

        else:
            break

<< << << < HEAD
print(are_valid_groups([1, 2, 3], [[1, 2], [1, 3]]))
== == == =
print(are_valid_groups(["1", "2", "3"], [
      ["1", "2", "3"], ["4", "5", "6", "7", "8"]]))
>>>>>> > 6a1008837d7ea174343ad19cf4e6e98c60613459
