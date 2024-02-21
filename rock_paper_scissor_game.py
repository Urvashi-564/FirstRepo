import random

# rules: rock wins against scissors 0,2
# scissors wins against paper2,1
# paper wins against rock2,0

user_choice = int(input("User Enter number between 0,1,2 0=rock\n1=paper\n2=scissor"))
if user_choice > 2 or user_choice < 0:
    print("invalid input")
    exit()
else:
    os_choice = random.randint(0, 2)
    table={0:'rock',1:'paper',2:'scissors'}
    print(f"computer chose {table[os_choice]}")
    print(f"you chose {table[user_choice]}")
    if user_choice == os_choice:
        print("Its a draw")
    elif 0 > user_choice > 2 and 0 > os_choice > 2:
        print("invalid input")

    elif user_choice == 0 and os_choice == 2:
        print("you won")
    elif user_choice == 2 and os_choice == 0:
        print("you lose")
    elif user_choice > os_choice:
        print("user wins you won")
    elif os_choice > user_choice:
        print("os wins,you lost the match")
