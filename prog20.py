import math
a=int(input("enter X**2 coeficient:"))
b=int(input("enter the x coeficient:"))
c=int(input("enter the constant:"))
delta=(b**2)-(4*a*c)
if(delta<0):
    print("the roots are not real")
elif(delta>=0):
    D=math.sqrt(delta)
    x1=(-b+D)/(2*a)
    x2=(-b-D)/(2*a)
    print("the roots is",x1,x2)
