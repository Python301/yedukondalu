days=int(input("enter how many days:"))
if(days<=5):
    charge=days*2
    print("the charge in {} days is ={}".format(days,charge))
elif(days<=10):
    charge=days*3
    print("the charge in {} days is ={}".format(days,charge))
elif(days<=15):
    charge=days*4
    print("the charge in {} days is ={}".format(days,charge))
else:
    charge=days*5
    print("the charge in {} days is ={}".format(days,charge))
