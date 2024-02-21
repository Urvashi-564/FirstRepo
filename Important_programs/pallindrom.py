orig_str=input("Enter string")
reversed_str=''.join(reversed(orig_str))
print(reversed_str)
if orig_str == reversed_str:
    print("its a pallindrome")

else:
    print('not')