#prime number program
n=int(input("enter the number:"))
prime=[]
for i in range(2,n+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)
        prime.append(i)
print("no.of.prime numbers",len(prime))



print("              ")
n=int(input("enter a number:"))
if n>1:
    for i in range(2,n):
        if(n%i==0):
            print("not a prime number")
    else:
        print("prime")
else:
    print("not a prime")
