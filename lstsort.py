#sort the list of the lements to enter the elements from user
n=int(input("enter how many numbers u want:"))
list=[]
i=0
while(i<n):
    list.append(int(input("enter the number:")))
    i=i+1
print("Before sorting the list:",list)
list.sort()
print("After sorting the list:",list)
