#convert the binary number into decimal number
num=list(input("enter the binary number:"))
val=0
for i in range(len(num)):
    digit=num.pop()
    if(digit=="1"):
        val=val+pow(2,i)
print("the decimal number is:",val)
print("***********another method**********")
num=input("enter a binary number:")
x=0
j=0
for i in range(len(num)-1,-1,-1):
    a=(2**j)*int(num[i])
    x=x+a
    j=j+1
print("the decimal number is:",x)
