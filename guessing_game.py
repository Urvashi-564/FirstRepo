import random

EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5
def guess(count,rangee):
    print(f"You have {count} attempts to guess a number")
    counter=count
    for i in range(rangee):
        guessed_num=int(input("Make a guess"))
        if guessed_num<number:
            print("Your guessed number is too low")
            counter -= 1
            print(f"you have only {counter} attempts left")
            if  counter == 0:
                print("You lose")
                break
        elif guessed_num>number:
            print("Your guessed number is too high")
            counter -= 1
            print(f"you have only {counter} attempts left")
            if  counter == 0:
                print("You lose")
                break
        elif guessed_num==number:
            print("you won")

print("Let me think a number between 1 to 50")
number=random.randint(1,50)
print(number)
level=input("Choose the level of difficulty 1)easy\n2)hard")
if level =='easy':
    guess(EASY_LEVEL_ATTEMPTS,10)
elif level=='hard':
    guess(HARD_LEVEL_ATTEMPTS,5)