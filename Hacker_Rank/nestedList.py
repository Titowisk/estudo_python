# https://www.hackerrank.com/challenges/nested-list/problem

student_score_list = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# student_score_list = [["student1", xx.xx], ["student2", yy,yy]...]

    
# lowest score student from student_score_list
def min_score(array):
    lowest_score_student = ""
    for i in range(len(student_score_list)):
        if not lowest_score_student:
            lowest_score_student = student_score_list[i] # lowest_score_student = ['student', xx.xx]
        
        if lowest_score_student[1] >= student_score_list[i][1]:
            lowest_score_student = student_score_list[i]
    return lowest_score_student

# removes the first lowest_score_student and its equals
lowest_score_student = min_score(student_score_list)
while True:
    condition = False
    for student_score in student_score_list:    # student_score = ['student', xx.xx]           
        if lowest_score_student[1] == student_score[1]:
            condition = True
            student_score_list.remove(student_score)
    if not condition:
        break
        
# create a list with the second_lowest_student_score and its equals   
all_lowest_score_students = []
second_lowest_score_student = min_score(student_score_list)
while True:
    condition = False
    for student_score in student_score_list:    # student_score = ['student', xx.xx]           
        if second_lowest_score_student[1] == student_score[1]:
            condition = True
            all_lowest_score_students.append(student_score)
            student_score_list.remove(student_score)
    if not condition:
        break

# print each student with the same second_lowest_score in alphabetical order
for student_score in sorted(all_lowest_score_students):
    print(student_score[0])