students, subjects = input().split(" ")
students = int(students)
subjects = int(subjects)

all_list = []

for subject in range(subjects):
    student_marks       = input().split(" ")
    student_marks_float = list(map(lambda X: float(X), student_marks))
    all_list.append(student_marks_float)

zipped = list(zip(*all_list))
print(zipped)

zipped_list = list(map(lambda x: list(x), zipped))
avg_score = list(map(lambda y: sum(y)/len(y), zipped_list))

for score in avg_score:
    print(score)
