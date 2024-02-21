
# create empty set
set2=set()
set2.add('Neha')
mylist=['Pushpa','Priya','Pooja']
for item in mylist:
    set2.add(item)
set1=set()
mysecondlist=['Ram','Shaym','Priya']
for item in mysecondlist:
    set1.add(item)

print(set1.union(set2))
set3={'mandeep','raju'}
set5=['1',2,3]
# print(set1|set2|set3)
print(set3.union(set5))
print(set3.difference(set5))
print(set2-set5)