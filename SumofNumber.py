n=int(input("enter the number:"))
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print("the total sum of the digits is",tot)
