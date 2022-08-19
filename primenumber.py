#To check the number is prime or not
n=int(input("enter the number:"))
if(n>1):
    for i in range(2,n):
        if(n%i==0):
            print("given number is not prime number")
            break
        else:
            print("given number is prime")
            break
else:
    print("not prime number")
