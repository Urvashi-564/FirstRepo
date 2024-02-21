height=int(input("enter height of child in feet"))
bill=0
if height>3:
    print("you can ride now please check age")
    age=int(input("enter age of your child"))
    if  age<12:
        bill=bill+150

    elif  age in range (12,19):
        bill=bill+250
    else:
        bill=bill+500
    want_pic = input("want photo answer y/n")
    if want_pic == 'y':
       bill=bill+50
    print(f"you total amount is {bill}")
else:
    print("Can't ride")