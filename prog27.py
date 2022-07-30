#newtons method (itterations)
x=int(input("enter the number:"))
gess=x/2
while((gess**2)-(x))>=10e-12:
    gess=(gess+(x/gess))/2
print("the square root of ",x,"is",gess)
