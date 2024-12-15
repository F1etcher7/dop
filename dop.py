from tokenize import group

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students =  {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_grades = [sum(group)/len(group) for group in grades]
print((average_grades))
students_list = list(students)
students_list.sort()
print(students_list)
zipped = zip(students_list, average_grades)
grades_students = dict(zipped)
print(grades_students)