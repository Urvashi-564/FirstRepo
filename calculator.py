# # num1 = int(input("Enter your first number"))
# # operator = input("Choose operator between:\n+\n -\n*\n/")
# # num2 = int(input("Enter your second number"))
# def add(num1, num2):
#     print("Addition result is", num1 + num2)
#     result=num1 + num2
#     return result
#
#
# def subtract(num1, num2):
#     print("Subtraction result is", num1 - num2)
#     result=num1 - num2
#     return result
#
#
# def multiply(num1, num2):
#     print("multiply result is", num1 * num2)
#     result=num1 * num2
#     return result
#
#
# def division(num1, num2):
#     print("division result is", num1 / num2)
#     result=num1 / num2
#     return result
#
#
#
# want_to_continue=True
# while want_to_continue is True:
#     num1 = int(input("Enter your first number"))
#     operator = input("Choose operator between:\n+\n -\n*\n/")
#     num2 = int(input("Enter your second number"))
#
#     if operator == '+':
#         result=add(num1, num2)
#         continuee = input(f"Do you want to continue with {result} press y or n to start new calculation or x to exit")
#         if continuee=='x':
#             want_to_continue = False
#         elif continuee == 'y':
#             num1=result
#             operator = input("Choose operator between:\n+\n -\n*\n/")
#             num2 = int(input("Enter your second number"))
#         elif continuee == "n":
#             num1 = int(input("Enter your first number"))
#             operator = input("Choose operator between:\n+\n -\n*\n/")
#             num2 = int(input("Enter your second number"))
#     elif operator == '-':
#         subtract(num1, num2)
#     elif operator == '*':
#         multiply(num1, num2)
#     elif operator == '/':
#         division(num1, num2)
#
#
import os
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
# we are creating dictionary where keys are operators and values are functions
operators_dict={
    '+':add,
    '-':sub,
    '*':mul,
    '/':div
}
def calculator():
    a=float(input('Enter First Number'))
    for ops in operators_dict:
        print(ops)
    continue_flag=True
    while continue_flag:
        op_symbol=input("Pick a symbol")
        b=float(input('Enter Second Number'))
        calculator_function=operators_dict[op_symbol]
        output=calculator_function(a,b)
        print(f"{a} {op_symbol} {b} ={output}")
        continuee = input(f"Do you want to continue with {output} press y or n to start new calculation or x to exit")
        if continuee=='y':
            a=output
        elif continuee=='n':
            os.system('cls')
            continue_flag=False
            calculator()
        else:
            continue_flag=False
            print("byee!!")

calculator()