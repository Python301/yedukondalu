#bonus to employee
salary=int(input("enter the salary:"))
year=int(input("enter how many years of experiance:"))
print("salary is",salary)
if(year<6):
    bonus=(salary*0.05)
    print("employee bonus is ",bonus)
elif(year>=6 and year<=10):
    bonus=(salary*0.08)
    print("employee bonus is ",bonus)
else:
    bonus=(salary*0.1)
    print("employee bonus is ",bonus)
