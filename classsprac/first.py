from classsprac import second


class Student(second):
    school_name = 'sfs'

    def __init__(self, stu_name, stu_class, stu_age):
        self.stu_name = stu_name
        self.stu_class = stu_class
        self.stu_age = stu_age
        second.__init__(self,teacher_name, t_dept)

    def greet(self):
        print(f"Hey {self.stu_name} welcome to {Student.school_name}")



st = Student('MAHESH', '5', 5)
st.greet()
# print(second.Teacher.school_name)
