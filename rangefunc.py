# a='urvashi sharma'
# count=len(a)
# for i in range(-1,-count-1,-1):
#     print(a[i])
#
# sum=0
# for i in range(1,101):
#     if i%2==0:
#         sum=sum+i
# print(f"sum of all even number between 100 numbers is {sum}")

def fizzbuzz():
    for i in range(1,16):
        if i%3==0 and i%5==0:
            print("fizzbuzz")
        elif i%3==0:
            print("fizz")
        elif i%5==0:
            print('buzz')
        else:
            print(i)


fizzbuzz()