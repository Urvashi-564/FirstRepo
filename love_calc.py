bfname=input("Enter your boyfriend's name")
gfname=input("Enter your GF name")
bfname=bfname.lower()
gfname=gfname.lower()
count_t_name=bfname.count('t')+gfname.count('t')
count_r_name=bfname.count('r')+gfname.count('r')
count_u_name=bfname.count('u')+gfname.count('u')
count_e_name=bfname.count('e')+gfname.count('e')
first_part_count = count_t_name+count_r_name+count_u_name+count_e_name
count_l_name=bfname.count('l')+gfname.count('l')
count_o_name=bfname.count('o')+gfname.count('o')
count_v_name=bfname.count('v')+gfname.count('v')
count_e_name=bfname.count('e')+gfname.count('e')
second_part_count=count_l_name+count_o_name+count_v_name+count_e_name
print(f"total love percentge is {first_part_count}{second_part_count}%")
love_score=str(first_part_count)+str(second_part_count)
if int(love_score) >90:
    print("awesome")
elif  int(love_score)<10:
    print("better luck")
else:
    print("good couple")