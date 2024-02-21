import data
import logodata
import random

score=0
result=True
print(logodata.game_logo)

while result:
    choice1=random.choice(data.data_list)
    print(f"Compare1:{choice1['name']}, a {choice1['descripton']} from {choice1['country']}")
    print(logodata.vs_logo)
    choice2=random.choice(data.data_list)
    print(f"Compare2:{choice2['name']}, a {choice2['descripton']} from {choice2['country']}")
    user_response=input("Choose 1 or 2 who is the winner")

    if choice1['follower'] > choice2['follower'] and user_response=='1':
        print(f"{choice1['name']} is correct {choice1['follower']} followers ,User won the game !!!")
        score+=1
    elif choice1['follower'] < choice2['follower'] and user_response=='2':
        print(f"{choice2['name']} is correct,,User won the game {choice2['follower']} are the followers!!!")
        score += 1
    elif  choice1['follower'] > choice2['follower'] and user_response=='2':
        print(f"{choice1['name']} is winner {choice1['follower']} is follower count ,User lost the game !!!")
        result=False
    elif  choice1['follower'] < choice2['follower'] and user_response=='1':
        print(f"{choice2['name']} is winner followers count is {choice2['follower']} ,User lost the game !!!")
        result = False
print("Final score of User is",score)