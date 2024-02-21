def max_num():
    nums=input("enter numbers")
    final_list=nums.split()
    count=0
    for i in final_list:
        count=count + 1
    final_count=count
    for i in range(final_count):
        final_list[i]=int(final_list[i])
    # assume first number is maximum number
    maximum_num=final_list[0]
    for i in final_list:
        if  i>maximum_num:
            maximum_num=i
    print(maximum_num)
max_num()

listn=[12,13,14,56,-1]
max_num=listn[0]
for i in listn:
    if i>max_num:
        max_num=i
print(f"max num is {max_num}")