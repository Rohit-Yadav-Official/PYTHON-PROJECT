
a=input("enter the value of list :\n")

lst=a.split()#  this is an import command for to print the list you an take input and then make it list.
#a=int(a)
print(lst)
print(type(a))
print(len(a))
print(lst)
lst.insert(0,999)# this will insert the value at the given position
lst.insert(2,888)
lst.insert(1,'geeks')# this will insert geeks at 1 position on list
print(lst)
lst.extend([6,4646,46456,456546 ,'retrt'])# extend the value of lst at the end of lst
print(lst)
lst.reverse()
print(lst)