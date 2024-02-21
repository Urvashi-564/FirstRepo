student_marks = {
    'Neha': 92,
    'Preeti': 60,
    'Charu': 73,
    'urvi': 100
}
grades={}
for stu_name in student_marks:
    marks=student_marks[stu_name]
    if marks>90:
        grade='A'
        grades[stu_name]=grade
    elif marks<90 and marks>80:
        grade='B'
        grades[stu_name]=grade
    elif marks>=70 and marks>=60:
        grade='C'
        grades[stu_name]=grade
    elif marks<=60:
        grade='D'
        grades[stu_name]=grade
print(grades)
# key=input("Enter name of student whose grade you want to know")
#
# value=student_marks[key]
# if value>90:
#     print("A Grade")
# elif value<90 and value>80:
#     print("B grade")
# elif value <80:
#     print("fail")