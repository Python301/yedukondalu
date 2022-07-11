#calculate the electricity bill
units=int(input("enter how many units:"))
if(units<=100):
    print("electricity bill is = 0")
elif(units<=200):
    bill=(100*0)+(units-100)*5
    print("electricity bill is=",bill)
else:
    bill=(100*0)+(100*5)+(units-200)*10
    print("electricity bill is=",bill)
