# Writing FABONACCI Series!!!!!!!!!
fib=[0,1]
LenSeries = int(input("Enter lenght of series:"))

if LenSeries <= 0:
    print("Please enter a positive number.")
elif LenSeries == 1:
    print(0)
else:
    for _ in range(2,LenSeries):
        fib.append(fib[-1]+fib[-2])
    for i in fib:
        print(i)


#fabonaci series
n=int(input("enter the no of terms:"))
f=0
s=1
if(n<=0):
    print("the required series is",f)
else:
    print(f,s,end=" ")
    for i in range(2,n):
        next=f+s
        print(next,end=" ")
        f=s
        s=next
