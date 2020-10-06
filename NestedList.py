if __name__ == '__main__':
    python_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    marks_list = [marks for _, marks in python_students]
    marks_list = set(marks_list)
    marks_list = list(marks_list)
    marks_list.sort()
    second_lowest_grade = marks_list[1]
    students_with_criteria = [student[0] for student in python_students if student[1] == second_lowest_grade]
    print(students_with_criteria)
