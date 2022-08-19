num=int(input("enter the number:"))
lst=[]
while num!=" ":
    num=input("enter the another number:")
    if(num!=" "):
        lst.append(int(num))
print(lst)
b=[]
a=[]
avg=sum(lst)/len(lst)
print(avg)
for i in lst:
    if(i<avg):
        b.append(i)
    else:
        a.append(i)
print(b)
print(a)
