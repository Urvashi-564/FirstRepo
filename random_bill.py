import random
list_of_friends=input("Enter names of your friends")

namees=list_of_friends.split(",")
name=random.choice(namees)
print(namees)
print(f"{name} will pay-->")
print("type of input we took",(type(list_of_friends)))
print("type of namees after we split we took",(type(namees)))

