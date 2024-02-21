vowels=['a','e','i','o','u']
count_num_of_vowels=0
stringg=input("Enter your string")
for char in stringg:
    if char in vowels:
        count_num_of_vowels+=1

print(count_num_of_vowels)