class Teacher:
    school_name = 'sfs'

    def __init__(self, teacher_name, t_dept):
        self.teacher_name = teacher_name
        self.t_dept = t_dept

    def teach(self):
        print("Teacher name is %s and dept is %s" % (self.teacher_name, self.t_dept))


tt = Teacher('Miss mary', 'science')
tt.teach()
