# import csv
#
# with open('My_Contacts.csv','r') as myfile:
#     reader=csv.reader(myfile, delimiter='\t')
#
#     my_dict={}
#
#     for row in reader:
#         print(row)
#         key=row[0]
#         my_dict[key]=row[1]
#
# print(my_dict)
import csv
with open('My_Contacts.csv','r') as  myfile:
    read_obj=csv.reader(myfile,delimiter='\t')
    my_dict={}
    headers=next(read_obj)
    for row in read_obj:
        key=row[0]
        my_dict[key]=row[1]
print(len(my_dict))
print(my_dict)


ans=input("Du you want to change any contact num enter y/n")
if ans=='y':
    key=input("Enter name of candidate you want to change number of")
    value=input("Enter new number")
    my_dict[key]=value

print(my_dict)
ans2=input("Do you want to add a new number enter y/n")
if ans2=='y':
    contact_name=input("name of your new contact")
    my_dict[contact_name]=contact_name
    contact_num=input("enter contact num")
    my_dict[contact_name]=contact_num
print(my_dict)