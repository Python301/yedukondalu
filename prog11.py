#find maximum number from 3 values
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))
if(a>b and a>c):
    print("the minimum number is",a)
if(b>a and b>c):
    print("the minimum number is",b)
if(c>a and c>b):
    print("the minimum number is",c)
else:
    print("program completed successfully")
