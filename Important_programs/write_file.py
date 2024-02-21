# with open('prac.txt','r') as file:
#     list_of_names=file.readlines()
    # rv_file=reversed(list_of_names)
    # with open ('prac2.txt','w') as new_file:
    #     for name in rv_file:
    #         new_file.write(name)
try:
    with open('pracc.txt','r') as file:
        list_of_names=file.readlines()
except Exception as e:
    print("It failed in this block")
    print(e)
finally:
    print("hii")
print("helo")