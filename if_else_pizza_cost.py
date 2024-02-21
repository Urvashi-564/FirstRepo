type_of_pizza = input("What type of Pizza you want Sir options are \n 1:Small\n 2:Medium\n 3:Large")
bill = 0
if type_of_pizza == "Small":
    bill = bill + 100
    print(f"basic price of your pizza is {bill}")

elif type_of_pizza == "Medium":
    bill = bill + 200
    print(f"basic price of your pizza is {bill}")

else:
    bill = bill + 500
    print(f"basic price of your pizza is {bill}")
peporroni = input("do you want peporoni \n1:Y \n 2:N")
if peporroni == "Y":
    if type_of_pizza == "Small":
        bill = bill + 30
    else:
        bill = bill + 50
extra_Cheese = input("Do you want EXTRA CHEESE \n1:Y \n 2:N")
if extra_Cheese == "Y":
    bill = bill + 20

print(f"final bill is {bill}")
