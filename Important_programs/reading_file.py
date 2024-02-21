my_file=open("prac.txt")
# print(my_file.read(5))#it will read 5 chracters
# my_file.close()

# for i in range(6):
#     print(my_file.readline())

# line=my_file.readline()
# while line != '':
#     print(line)
#     line = my_file.readline()
listt=my_file.readlines()
for line in listt:
    print(line)
my_file.close()