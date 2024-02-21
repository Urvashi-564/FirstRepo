# print("Make your own dictonary")
# name=input("Enter name of your dictionary")
# word=input("input word")
# meaning=input("enter meaning or meanings of your word")
# name={}
# name[word]=meaning
# print(name)

# data={
#     'contacts':{'ram':123,'shyam':345,'bhajan':2323},
#     'departments':['maths','science','history'],
#     'teachers':{'neha':{'maths','science'},'sushma':'history'},
#     'stu_kishan':{'age':30,'class':'x','grade':'B'}
# }
#
# print(data['contacts']['bhajan'])
# data['stu_kishan']['contact_num']='898989'
# # data['stu_kishan']['contact_num']=10000
# print(data)

# my_cites=[{'city':'delhi','mumbai':'vada pao'},
#           {'masala':['haldi','mirch','namak']}]
# print(my_cites)

student=[
    {'name':'ram','classs':'10','contact':'2323','grade':'A'},
    {'name':'raj','classs':'10','contact':'6767','grade':'B'}
]

def add_student(name,classs,contact,grade):
    new_student={}
    new_student['name']=name
    new_student['classs']=classs
    new_student['contact']=contact
    new_student['grade']=grade
    student.append(new_student)
print(f"your orig dictionary {student}")
name=input("name of new student")
classs=input("classs?")
contact=input("enter contact num")
grade=input("enter grade")
add_student(name,classs,contact,grade)
print(student)