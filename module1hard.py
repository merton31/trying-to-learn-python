grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = sorted(students)
average_grades = [sum(grades)/len(grades) for grades in grades]
final_list = dict(zip(students_list, average_grades))
print(final_list)