#To calculate Grad of the student
marks=int(input("enter student marks:"))
if(marks>100 and marks<0):
    print("invalid input dont enter out of range and zero")
elif(marks>90):
    print("Grad of the student is outstanding")
elif(marks>80):
    print("Grad of the student is excelant")
elif(marks>60):
    print("Grad of the student is good")
elif(marks>40):
    print("Grad of the student is poor")
else:
    print("Grad of the student is fail")
