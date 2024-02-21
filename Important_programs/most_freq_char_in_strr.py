strr=input("enter string")
max_count=0
char_count=0
character=''
for char in strr:
    char_count =strr.count(char)

    if char_count>=max_count:
        max_count=char_count
        character = char
print(f"{character}  has maximum count of {max_count}")

# def most_frequent_char(input_string):
#  char_count = {}
#  for char in input_string:
#      char_count[char] = char_count.get(char, 0) + 1
#  return max(char_count, key=char_count.get)